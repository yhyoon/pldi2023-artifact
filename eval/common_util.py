from typing import Callable, Any
import os
import sys
import time
import threading

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
    "pbe-bitvec":   os.path.join(bench_root_path, "pbe-bitvec"),
}

bench_names = [
    "deobfusc", "hd", "crypto", "lobster", "pbe-bitvec"
]

solver_names = [
    "abs_synth", "duet", "probe"
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

tbl1_rand_chosen_bench = frozenset((
    *tbl1_rand_chosen_hd_problems,
    *tbl1_rand_chosen_deob_problems,
    *tbl1_rand_chosen_lobster_problems,
    *tbl1_rand_chosen_crypto_problems
))

result_root_path = os.path.join(artifact_root_path, "result")


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
