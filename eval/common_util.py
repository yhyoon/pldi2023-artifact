from typing import Callable, Any, Tuple, Dict, List, FrozenSet, Optional
import os
import sys
import time
import threading
import pandas as pd


log_out = sys.stdout
log_lock = threading.Lock()


def log_write_internal(s):
    if s.endswith('\n'):
        log_out.write(s)
    else:
        log_out.write(s + '\n')
    log_out.flush()


def log_write_with_time(s: str):
    with log_lock:
        for line in s.splitlines():
            prefix_time = time.strftime("%Y-%m-%d %H:%M:%S")
            log_write_internal(prefix_time + f"[{threading.current_thread().name}]" + line)


def traverse(current_path: str,
             is_target: Callable[[str], bool],
             target_handler: Callable[[str, int], Any],
             index: int = 0) -> int:
    if os.path.isdir(current_path):
        for f in os.listdir(current_path):
            index = traverse(os.path.join(current_path, f), is_target, target_handler, index)
    elif os.path.isfile(current_path) and is_target(current_path):
        target_handler(current_path, index)
        index += 1
    return index


artifact_root_path = os.path.dirname(os.path.dirname(__file__))

bench_root_path = os.path.join(artifact_root_path, "bench")

bench_name_to_dir = {
    "all":          bench_root_path,
    "bitvec":       os.path.join(bench_root_path, "bitvec"),
    "deobfusc":     os.path.join(bench_root_path, "bitvec", "deobfusc"),
    "hd":           os.path.join(bench_root_path, "bitvec", "hd"),
    "circuit":      os.path.join(bench_root_path, "circuit"),
    "crypto":       os.path.join(bench_root_path, "circuit", "crypto"),
    "lobster":      os.path.join(bench_root_path, "circuit", "lobster"),
}

bench_names = [
    "deobfusc", "hd", "crypto", "lobster",
]

no_cond_bench_names = [
    "deobfusc", "hd", "crypto", "lobster",
]

solver_names = [
    "abs_synth", "duet", "probe"
]

ablation_names = [
    "abs_synth_bf", "abs_synth_smt", "abs_synth_fonly"
]

tbl1_rand_chosen_hd_problems = [
    "hd-03-d5-prog",
    "hd-07-d0-prog",
    "hd-14-d5-prog",
    "hd-19-d1-prog",
    "hd-20-d1-prog"
]
tbl1_rand_chosen_deob_problems = [
    "target_9",
    "target_119",
    "target_385",
    "target_410",
    "target_449"
]
tbl1_rand_chosen_lobster_problems = [
    "hd09.eqn_sygus_iter_45_0",
    "longest_1bit-opt.eqn_sygus_iter_63_1",
    "longest_1bit-opt.eqn_sygus_iter_75_1",
    "p03.eqn_sygus_iter_38_2",
    "p09.eqn_sygus_iter_49_1"
]
tbl1_rand_chosen_crypto_problems = [
    "CrCy_2-P6_2-P6",
    "CrCy_5-P9-D5-sIn",
    "CrCy_8-P12-D5-sIn4",
    "CrCy_8-P12-D7-sIn5",
    "CrCy_10-sbox2-D5-sIn11"
]

tbl1_rand_chosen_bench: Dict[str, List[str]] = {
    "hd": tbl1_rand_chosen_hd_problems,
    "deobfusc": tbl1_rand_chosen_deob_problems,
    "lobster": tbl1_rand_chosen_lobster_problems,
    "crypto": tbl1_rand_chosen_crypto_problems,
}


def _gen_problems() -> Tuple[Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]], Dict[str, str]]:
    building_problem_map: Dict[str, str] = dict()
    building_problem_list_map: Dict[str, List[str]] = {
        "deobfusc": list(),
        "hd": list(),
        "crypto": list(),
        "lobster": list(),
    }

    def add_to(bench_name: str, problem_file_path: str):
        problem_name = os.path.splitext(os.path.split(problem_file_path)[1])[0]
        building_problem_list_map[bench_name].append(problem_name)
        building_problem_map[problem_name] = bench_name

    for b in bench_names:
        traverse(bench_name_to_dir[b],
                 lambda f: f.endswith(".sl"),
                 lambda f, index: add_to(b, f)
                 )

    return {b: (building_problem_list_map[b],
                frozenset(building_problem_list_map[b]),
                pd.DataFrame({"problem": building_problem_list_map[b]}).set_index('problem')
                )
            for b in bench_names}, building_problem_map


(problem_map, problem_bench_map) = _gen_problems()


result_root_path = os.path.join(artifact_root_path, "result")


def result_path(solver_name: str) -> str:
    return os.path.join(result_root_path, solver_name)


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

    for solver in [*solver_names, *ablation_names]:
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
    for solver in [*solver_names, *ablation_names]:
        if all(tbl[solver][bench]["no_result"] == 0 for bench in bench_names):
            lines.append(f"{solver}: DONE")
        elif all(tbl[solver][bench]["no_result"] == len(problem_map[bench][1]) for bench in bench_names):
            lines.append(f"{solver}: NO_RESULT")
        else:
            lines.append(f"{solver}:")
            for bench in bench_names:
                if tbl[solver][bench]["no_result"] == 0:
                    lines.append(f"  {bench}:[{len(problem_map[bench][1])}/{len(problem_map[bench][1])}] DONE")
                elif tbl[solver][bench]["no_result"] == len(problem_map[bench][1]):
                    lines.append(f"  {bench}: NO_RESULT")
                else:
                    lines.append(f"  {bench}:[{len(problem_map[bench][1]) - tbl[solver][bench]['no_result']}/{len(problem_map[bench][1])}]")
                    for ci in counter_items:
                        if tbl[solver][bench][ci] > 0:
                            lines.append(f"    {ci}: {tbl[solver][bench][ci]}")

    return lines

