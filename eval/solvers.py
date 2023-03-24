from typing import Optional
import re

from common_util import *
import timeout_runner


class Solver:
    def name(self) -> str:
        raise NotImplementedError("solver.name")

    def executable(self) -> str:
        raise NotImplementedError("solver.executable")

    def result_path(self) -> str:
        return result_path(self.name())

    def additional_env(self) -> Optional[Dict[str, str]]:
        return None

    def params(self, target: str) -> List[str]:
        raise NotImplementedError("solver.params")

    def extract_result(self, handle: timeout_runner.TimeoutRunner) -> Tuple[str, str, str]:
        raise NotImplementedError("solver.extract_result")

    def solvable(self, bench: str) -> bool:
        return True


class SolverSimba(Solver):
    # command: ./simba.exe [target_name]

    def name(self) -> str:
        return "simba"

    def executable(self) -> str:
        return os.path.join(artifact_root_path, "simba", "simba.exe")

    def params(self, target: str) -> List[str]:
        json_path = self.result_path() + os.sep + os.path.splitext(target[len(bench_root_path):])[0] + ".json"
        return ["-report_json", json_path, target]

    def extract_result(self, handle: timeout_runner.TimeoutRunner) -> Tuple[str, str, str]:
        result_string = handle.captured_stderr
        result_time_ms = handle.get_elapsed_time()
        max_size_error: bool = re.search(r"hit bottom.up limit", result_string, re.MULTILINE) is not None

        error_string = "failure"
        if max_size_error:
            error_string = "fail_with_max_size"

        result_definition_search = re.search(r"^\(define-fun.+\)$", result_string, re.MULTILINE)
        result_definition = result_definition_search.group(0) if result_definition_search is not None else error_string
        result_size_search = re.search(r"^size : (\d+)$", result_string, re.MULTILINE)
        result_size = int(result_size_search.group(1)) if result_size_search is not None else error_string
        return str(result_time_ms), str(result_size), result_definition


class SolverSimbaBF(SolverSimba):
    # command: ./simba.exe -pruning bruteforce [target_name]
    def name(self) -> str:
        return "simba_bf"

    def solvable(self, bench: str) -> bool:
        return bench != "pbe-bitvec"

    def params(self, target: str) -> List[str]:
        json_path = self.result_path() + os.sep + os.path.splitext(target[len(bench_root_path):])[0] + ".json"
        return ["-pruning", "bruteforce", "-report_json", json_path, target]


class SolverSimbaSMT(SolverSimba):
    # command: ./simba.exe -pruning solver [target_name]
    def name(self) -> str:
        return "simba_smt"

    def solvable(self, bench: str) -> bool:
        return bench != "pbe-bitvec"

    def params(self, target: str) -> List[str]:
        json_path = self.result_path() + os.sep + os.path.splitext(target[len(bench_root_path):])[0] + ".json"
        return ["-pruning", "solver", "-report_json", json_path, target]


class SolverSimbaForwardOnly(SolverSimba):
    # command: ./simba.exe -pruning solver [target_name]
    def name(self) -> str:
        return "simba_fonly"

    def solvable(self, bench: str) -> bool:
        return bench != "pbe-bitvec"

    def params(self, target: str) -> List[str]:
        json_path = self.result_path() + os.sep + os.path.splitext(target[len(bench_root_path):])[0] + ".json"
        return ["-no_backward", "-report_json", json_path, target]


class SolverSimbaEx05(SolverSimba):
    # command: ./simba.exe -ex_cut 5 [target_name]
    def name(self) -> str:
        return "simba_ex05"

    def solvable(self, bench: str) -> bool:
        return bench == "deobfusc"

    def params(self, target: str) -> List[str]:
        json_path = self.result_path() + os.sep + os.path.splitext(target[len(bench_root_path):])[0] + ".json"
        return ["-ex_cut", "5", "-report_json", json_path, target]


class SolverSimbaEx10(SolverSimba):
    # command: ./simba.exe -ex_cut 10 [target_name]
    def name(self) -> str:
        return "simba_ex10"

    def solvable(self, bench: str) -> bool:
        return bench == "deobfusc"

    def params(self, target: str) -> List[str]:
        json_path = self.result_path() + os.sep + os.path.splitext(target[len(bench_root_path):])[0] + ".json"
        return ["-ex_cut", "10", "-report_json", json_path, target]


class SolverSimbaEx15(SolverSimba):
    # command: ./simba.exe -ex_cut 15 [target_name]
    def name(self) -> str:
        return "simba_ex15"

    def solvable(self, bench: str) -> bool:
        return bench == "deobfusc"

    def params(self, target: str) -> List[str]:
        json_path = self.result_path() + os.sep + os.path.splitext(target[len(bench_root_path):])[0] + ".json"
        return ["-ex_cut", "15", "-report_json", json_path, target]


class SolverDuet(Solver):
    # command for bv: ./main.native -fastdt -ex_all -max_size 10000 -init_comp_size 3 [target_name]
    # command for circuit: ./main.native -max_size 128 -max_height 16 -init_comp_size 1 [target_name]

    def name(self) -> str:
        return "duet"

    def executable(self) -> str:
        return os.path.join(artifact_root_path, "duet", "main.native")

    def additional_env(self) -> Optional[Dict[str, str]]:
        import platform
        os_name = platform.system()
        if os_name == "Darwin":
            lib_path_key = "DYLD_LIBRARY_PATH"
        else:
            lib_path_key = "LD_LIBRARY_PATH"

        if lib_path_key in os.environ:
            return {lib_path_key: os.path.join(os.environ["HOME"], ".opam", "4.08.0", "lib", "z3") + ":" + os.environ[lib_path_key]}
        else:
            return {lib_path_key: os.path.join(os.environ["HOME"], ".opam", "4.08.0", "lib", "z3")}

    def params(self, target: str) -> List[str]:
        if target.startswith(bench_name_to_dir["bitvec"]) or target.startswith(bench_name_to_dir["pbe-bitvec"]):
            return ["-fastdt", "-ex_all", "-max_size", "10000", "-init_comp_size", "3", target]
        elif target.startswith(bench_name_to_dir["circuit"]):
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

    def name(self) -> str:
        return "probe"

    def executable(self) -> str:
        return "java"

    def additional_env(self) -> Optional[Dict[str, str]]:
        return {"PATH": os.path.join(artifact_root_path, "probe") + ":" + os.environ["PATH"]}

    def params(self, target: str) -> List[str]:
        return ["-cp", os.path.join("probe", "target", "scala-2.12", "probe-assembly-0.1.jar"), "sygus/ProbeMain", target]

    def extract_result(self, handle: timeout_runner.TimeoutRunner) -> Tuple[str, str, str]:
        result_lines = handle.captured_stdout.splitlines()
        result_string = handle.captured_stdout.splitlines()[-1] if len(result_lines) > 0 else ""  # last_line
        result_time_ms = handle.get_elapsed_time()

        row = result_string.split(",")
        if len(row) == 5 and not row[3].endswith(")"):  # handle error case: size ends with ")" instead of pure integer
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
        return bench in {"bitvec", "deobfusc", "hd"}


solver_map: Dict[str, Solver] = {
    "simba": SolverSimba(),
    "simba_bf": SolverSimbaBF(),
    "simba_smt": SolverSimbaSMT(),
    "simba_fonly": SolverSimbaForwardOnly(),
    "simba_ex05": SolverSimbaEx05(),
    "simba_ex10": SolverSimbaEx10(),
    "simba_ex15": SolverSimbaEx15(),
    "duet": SolverDuet(),
    "probe": SolverProbe(),
}


# no_result, timeout, failure, success
def result_status(solver_name: str, problem_name: str) -> str:
    problem_path = os.path.join(bench_name_to_dir[problem_bench_map[problem_name]], problem_name + ".sl")
    result_file_path = result_path(solver_name) + os.sep + os.path.splitext(problem_path[len(bench_root_path):])[0] + ".result.txt"
    try:
        with open(result_file_path, "rt") as fin:
            line = fin.readline()
            solver, problem, sol_time_str, sol_size_str, sol = line.strip().split(sep=",")

            if sol == "timeout":
                return "timeout"
            elif sol == "fail_with_max_size":
                return "success"
            elif sol == "failure" or sol_size_str.endswith(")"):
                return "failure"
            else:
                return "success"
    except FileNotFoundError:
        return "no_result"


# solver |-> bench |-> (success|timeout|failure|no_result) |-> count
def all_result_status_tbl() -> Dict[str, Dict[str, Dict[str, int]]]:
    tbl = dict()
    counter_items = ["success", "timeout", "failure", "no_result"]

    for solver in [*solver_names, *ablation_names, *ex_cut_names]:
        tbl[solver] = dict()
        for bench in bench_names:
            bench_counters = {ci: 0 for ci in counter_items}
            for problem in problem_map[bench][0]:
                bench_counters[result_status(solver, problem)] += 1
            tbl[solver][bench] = bench_counters

    return tbl


def all_result_status_str() -> List[str]:
    lines = list()
    counter_items = ["success", "timeout", "failure", "no_result"]

    tbl = all_result_status_tbl()
    for solver_name in [*solver_names, *ablation_names, *ex_cut_names]:
        solver = solver_map[solver_name]
        if all(not solver.solvable(bench) or tbl[solver_name][bench]["no_result"] == 0 for bench in bench_names):
            lines.append(f"{solver_name}: DONE")
        elif all(tbl[solver_name][bench]["no_result"] == len(problem_map[bench][1]) for bench in bench_names):
            lines.append(f"{solver_name}: NO_RESULT")
        else:
            lines.append(f"{solver_name}:")
            for bench in bench_names:
                if not solver.solvable(bench):
                    continue
                elif tbl[solver_name][bench]["no_result"] == 0:
                    lines.append(f"  {bench}:[{len(problem_map[bench][1])}/{len(problem_map[bench][1])}] DONE")
                elif tbl[solver_name][bench]["no_result"] == len(problem_map[bench][1]):
                    lines.append(f"  {bench}: NO_RESULT")
                else:
                    lines.append(f"  {bench}:[{len(problem_map[bench][1]) - tbl[solver_name][bench]['no_result']}/{len(problem_map[bench][1])}]")
                    for ci in counter_items:
                        if tbl[solver_name][bench][ci] > 0:
                            lines.append(f"    {ci}: {tbl[solver_name][bench][ci]}")

    return lines
