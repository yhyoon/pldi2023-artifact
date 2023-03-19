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


class SolverAbsSynth(Solver):
    # command: ./abs_synth.exe [target_name]

    def name(self) -> str:
        return "abs_synth"

    def executable(self) -> str:
        return os.path.join(artifact_root_path, "abs_synth", "abs_synth.exe")

    def params(self, target: str) -> List[str]:
        file_name = os.path.split(target)[1]
        problem_name = os.path.splitext(file_name)[0]
        return ["-report_json", os.path.join(self.result_path(), problem_name + "." + self.name() + ".json"), target]

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


class SolverAbsSynthBF(SolverAbsSynth):
    # command: ./abs_synth.exe -pruning bruteforce [target_name]
    def name(self) -> str:
        return "abs_synth_bf"

    def params(self, target: str) -> List[str]:
        file_name = os.path.split(target)[1]
        problem_name = os.path.splitext(file_name)[0]
        return ["-pruning", "bruteforce", "-report_json", os.path.join(self.result_path(), problem_name + "." + self.name() + ".json"), target]


class SolverAbsSynthSMT(SolverAbsSynth):
    # command: ./abs_synth.exe -pruning solver [target_name]
    def name(self) -> str:
        return "abs_synth_smt"

    def params(self, target: str) -> List[str]:
        file_name = os.path.split(target)[1]
        problem_name = os.path.splitext(file_name)[0]
        return ["-pruning", "solver", "-report_json", os.path.join(self.result_path(), problem_name + "." + self.name() + ".json"), target]


class SolverAbsSynthForwardOnly(SolverAbsSynth):
    # command: ./abs_synth.exe -pruning solver [target_name]
    def name(self) -> str:
        return "abs_synth_fonly"

    def params(self, target: str) -> List[str]:
        file_name = os.path.split(target)[1]
        problem_name = os.path.splitext(file_name)[0]
        return ["-no_backward", "-report_json", os.path.join(self.result_path(), problem_name + "." + self.name() + ".json"), target]


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
        if target.startswith(bench_name_to_dir["bitvec"]):
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
    "abs_synth": SolverAbsSynth(),
    "abs_synth_bf": SolverAbsSynthBF(),
    "abs_synth_smt": SolverAbsSynthSMT(),
    "abs_synth_fonly": SolverAbsSynthForwardOnly(),
    "duet": SolverDuet(),
    "probe": SolverProbe(),
}
