from typing import Callable, Any, Tuple, Dict, List, FrozenSet
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
    "bitvec-cond":   os.path.join(bench_root_path, "bitvec-cond"),
}

bench_names = [
    "deobfusc", "hd", "crypto", "lobster", "bitvec-cond",
]

no_cond_bench_names = [
    "deobfusc", "hd", "crypto", "lobster",
]

solver_names = [
    "simba", "duet", "probe"
]

ablation_names = [
    "simba_bf", "simba_smt", "simba_fonly"
]

ex_cut_names = [
    "simba_ex05", "simba_ex10", "simba_ex15"
]

tbl1_rand_chosen_hd_problems = [
    "hd-03-d5-prog",
    "hd-07-d0-prog",
    "hd-14-d5-prog",
    "hd-19-d1-prog",
    "hd-20-d1-prog",
]
tbl1_rand_chosen_deob_problems = [
    "target_9",
    "target_119",
    "target_385",
    "target_410",
    "target_449",
]
tbl1_rand_chosen_lobster_problems = [
    "hd09.eqn_sygus_iter_45_0",
    "longest_1bit-opt.eqn_sygus_iter_63_1",
    "longest_1bit-opt.eqn_sygus_iter_75_1",
    "p03.eqn_sygus_iter_38_2",
    "p09.eqn_sygus_iter_49_1",
]
tbl1_rand_chosen_crypto_problems = [
    "CrCy_2-P6_2-P6",
    "CrCy_5-P9-D5-sIn",
    "CrCy_8-P12-D5-sIn4",
    "CrCy_8-P12-D7-sIn5",
    "CrCy_10-sbox2-D5-sIn11",
]
tbl1_rand_chosen_bvcond_problems = [
    "133_1000",
    "23_10",
    "60_100",
    "icfp_gen_10.7",
    "icfp_gen_14.1",
]

tbl1_rand_chosen_bench = frozenset((
    *tbl1_rand_chosen_hd_problems,
    *tbl1_rand_chosen_deob_problems,
    *tbl1_rand_chosen_lobster_problems,
    *tbl1_rand_chosen_crypto_problems,
    *tbl1_rand_chosen_bvcond_problems,
))


def _gen_problems() -> Tuple[Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]], Dict[str, str]]:
    building_problem_map: Dict[str, str] = dict()
    building_problem_list_map: Dict[str, List[str]] = {
        "deobfusc": list(),
        "hd": list(),
        "crypto": list(),
        "lobster": list(),
        "bitvec-cond": list(),
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
