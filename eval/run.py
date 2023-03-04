from typing import List, Tuple, Dict

import argparse
import re

import common_util
from common_util import *
import timeout_runner


class Solver:
    name: str
    executable: str
    result_path: str

    def params(self, target: str) -> List[str]:
        raise NotImplementedError("solver.params")

    def extract_result(self, handle: timeout_runner.TimeoutRunner) -> Tuple[str, str, str]:
        raise NotImplementedError("solver.extract_result")

    def solvable(self, bench: str) -> bool:
        return True


class SolverAbsSynth(Solver):
    # command: ./abs_synth.exe [target_name]

    def __init__(self):
        self.name = "abs_synth"
        self.executable = os.path.join(artifact_root_path, "abs_synth", "abs_synth.exe")
        self.result_path = os.path.join(artifact_root_path, "result", "abs_synth")

    def params(self, target: str) -> List[str]:
        return [target]

    def extract_result(self, handle: timeout_runner.TimeoutRunner) -> Tuple[str, str, str]:
        result_string = handle.captured_stderr
        result_time_ms = handle.get_elapsed_time()
        max_size_error: bool = re.search(r"hit bottom-up limit", result_string, re.MULTILINE) is not None

        error_string = "failure"
        if max_size_error:
            error_string = "fail_with_max_size"

        result_definition_search = re.search(r"^\(define-fun.+\)$", result_string, re.MULTILINE)
        result_definition = result_definition_search.group(0) if result_definition_search is not None else error_string
        result_size_search = re.search(r"^size : (\d+)$", result_string, re.MULTILINE)
        result_size = int(result_size_search.group(1)) if result_size_search is not None else error_string
        return str(result_time_ms), str(result_size), result_definition


class SolverDuet(Solver):
    # command for bv: ./main.native -fastdt -ex_all -max_size 10000 -init_comp_size 3 [target_name]
    # command for circuit: ./main.native -max_size 128 -max_height 16 -init_comp_size 1 [target_name]

    def __init__(self):
        self.name = "duet"
        self.executable = "./duet/main.native"
        self.result_path = os.path.join(artifact_root_path, "result", "duet")

    def params(self, target: str) -> List[str]:
        if target.startswith(bench_name_to_dir["bitvec"]):
            return ["-fastdt", "-ex_all", "-max_size", "10000", "-init_comp_size", "3", target]
        elif target.startswith(bench_name_to_dir["circuit"]):
            return ["-max_size", "128", "-max_height", "16", "-init_comp_size", "1", target]
        elif target.startswith(bench_name_to_dir["pbe-bitvec"]):
            return ["-max_size", "128", "-max_height", "16", "-init_comp_size", "1", target]
        else:
            return [target]

    def extract_result(self, handle: timeout_runner.TimeoutRunner) -> Tuple[str, str, str]:
        result_string = handle.captured_stderr
        result_time_ms = handle.get_elapsed_time()
        max_size_error: bool = re.search(r"Consider increasing the max", result_string, re.MULTILINE) is not None

        error_string = "failure"
        if max_size_error:
            error_string = "fail_with_max_size"

        result_definition_search = re.search(r"^\(define-fun.+\)$", result_string, re.MULTILINE)
        result_definition = result_definition_search.group(0) if result_definition_search is not None else error_string
        result_size_search = re.search(r"^size : (\d+)$", result_string, re.MULTILINE)
        result_size = int(result_size_search.group(1)) if result_size_search is not None else error_string
        return str(result_time_ms), str(result_size), result_definition


class SolverProbe(Solver):
    # command: java -cp probe-assembly-0.1.jar sygus/ProbeMain [target_name]

    def __init__(self):
        self.name = "probe"
        self.executable = "java"
        self.result_path = os.path.join(artifact_root_path, "result", "probe")

    def params(self, target: str) -> List[str]:
        return ["-cp", os.path.join("probe", "target", "scala-2.12", "probe-assembly-0.1.jar"), "sygus/ProbeMain", target]

    def extract_result(self, handle: timeout_runner.TimeoutRunner) -> Tuple[str, str, str]:
        result_lines = handle.captured_stdout.splitlines()
        result_string = handle.captured_stdout.splitlines()[-1] if len(result_lines) > 0 else ""  # last_line
        result_time_ms = handle.get_elapsed_time()

        row = result_string.split(",")
        if len(row) == 5:
            result_definition = row[1]
            result_size = row[3]
            return str(result_time_ms), str(result_size), result_definition
        else:
            log_write_with_time("  !run failure!")
            log_write_with_time("  ===stdout===")
            log_write_with_time(handle.captured_stdout)
            log_write_with_time("  ===stderr===")
            log_write_with_time(handle.captured_stderr)
            return str(result_time_ms), "failure", "failure"

    def solvable(self, bench: str) -> bool:
        return bench in {"bitvec", "deobfusc", "hd", "pbe-bitvec"}


solvers: Dict[str, Solver] = {
    "abs_synth": SolverAbsSynth(),
    "duet": SolverDuet(),
    "probe": SolverProbe(),
}


def write_result(out_path: str, solver: Solver, problem_name: str, result_time: str, result_size: str, result_sol: str):
    # if abs_synth solved pldi2023-artifact/bench/bitvec/hd/hd-01-d1-prog.sl
    # -> result file: pldi2023-arrtifact/result/abs_synth/bitvec/hd/hd-01-d1-prog.result.txt
    with open(out_path, "wt") as out:
        # csv format
        # solver, problem_name, time, size, solution
        out.write(f"{solver.name},{problem_name},{result_time},{result_size},{result_sol}\n")


def pop_target_and_run(solver: Solver, targets: List[List[str]], targets_lock, targets_len, timeout_in_sec, overwrite):
    while True:
        with targets_lock:
            if len(targets) == 0:
                log_write_with_time(f"No more targets, stop this thread {threading.current_thread()}")
                return

            target_cnt = targets_len - len(targets) + 1
            target = targets.pop(0)

        target_file_path = target[-1]  # last arg is sl file name
        target_file_name = os.path.split(target_file_path)[1]
        problem_name = os.path.splitext(target_file_name)[0]
        out_path = solver.result_path + os.sep + os.path.splitext(target_file_path[len(bench_root_path):])[0] + ".result.txt"

        if os.path.isfile(out_path) and not overwrite:
            log_write_with_time(f"  [Target {target_cnt}/{targets_len}] is already evaluated => skip")
        else:
            handle = timeout_runner.TimeoutRunner(solver.executable, target, timeout_in_sec)
            log_write_with_time(f"  [Target {target_cnt}/{targets_len}]"
                                f" run command[pid={handle.get_pid()}] for {handle.timeout} sec: "
                                f"{solver.executable} {' '.join(target)}")
            handle.wait_for_result()

            if handle.killed_by_timeout:
                log_write_with_time(f"    [Target {target_cnt}/{targets_len}]"
                                    f" exceeded timeout({handle.timeout} sec) => "
                                    f"send kill to process [{handle.get_pid()}] args={' '.join(target)}")
                write_result(out_path, solver, problem_name, "timeout", "timeout", "timeout")
            else:
                sol_time, sol_size, sol = solver.extract_result(handle)
                log_write_with_time(f"RESULT_SUMMARY: {solver.name},{problem_name},{sol_time},{sol_size},{sol}")
                write_result(out_path, solver, problem_name, sol_time, sol_size, sol)


def run_test(solver_name: str, bench: str, chosen: bool, overwrite: bool, timeout_in_sec: int, thread_count: int):
    solver = solvers[solver_name]

    if not solver.solvable(bench):
        log_write_with_time(f"{solver.name} cannot solve {bench}")
        return

    target_files: List[str] = list()

    def is_target(path):
        file_name = os.path.split(path)[1]
        problem_name, ext = os.path.splitext(file_name)
        if ext == ".sl":
            if chosen:
                return problem_name in tbl1_rand_chosen_bench
            else:
                return True
        else:
            return False

    traverse(bench_name_to_dir[bench], is_target, lambda x, index: target_files.append(x))

    target_files.sort()
    targets: List[List[str]] = [solver.params(target_file) for target_file in target_files]

    targets_len = len(targets)
    targets_lock = threading.Lock()

    threads = []
    if thread_count > 1:
        log_write_with_time(f"Run tests in parallel with {thread_count} threads")

    for i in range(0, thread_count):
        log_write_with_time(f"Activate Thread{i}")
        t = threading.Thread(target=pop_target_and_run,
                             name=f"Thread{i}",
                             args=(solver, targets, targets_lock, targets_len, timeout_in_sec, overwrite))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def main():
    parser = argparse.ArgumentParser(description='run evaluation')

    parser.add_argument('solver', type=str,
                        help='solver name(abs_synth | duet | probe)')
    parser.add_argument('bench', type=str,
                        help='target bench name (bitvec | deobfusc | hd | circuit | crypto | lobster | pbe-bitvec)')
    parser.add_argument('-chosen', action='store_true',
                        help='run randomly chosen set of benchmarks (Table 1 in paper)')
    parser.add_argument('-p', type=int, metavar='NUM', nargs='?', default=1,
                        dest='thread_count',
                        help='run in parallel process using NUM threads (default: 1)')
    parser.add_argument('-timeout', type=int, metavar='NUM', nargs='?', default=3600,
                        dest='timeout',
                        help='timeout for each problem in seconds (default: 3600)')
    parser.add_argument('-overwrite', action='store_true',
                        help='force run solver even if there already exists result file for the benchmark'
                             '(default: skip existing result)')
    parser.add_argument('-log', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        dest='log_out',
                        help='test progress log print to... (default: stdout)')

    args = parser.parse_args()

    common_util.log_out = args.log_out

    run_test(args.solver, args.bench, args.chosen, args.overwrite, args.timeout, args.thread_count)


if __name__ == '__main__':
    main()
