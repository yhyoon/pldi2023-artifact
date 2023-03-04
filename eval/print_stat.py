from typing import Optional, Tuple, List, Dict, FrozenSet

import argparse
import re
import matplotlib.pyplot as plt
import pandas as pd

import common_util
from common_util import *


def gen_problem_list() -> Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]]:
    deobfusc_list = list()
    hd_list = list()
    crypto_list = list()
    lobster_list = list()
    pbe_bitvec_list = list()

    traverse(bench_name_to_dir["deobfusc"],
             lambda f: f.endswith(".sl"),
             lambda f, index: deobfusc_list.append(os.path.splitext(os.path.split(f)[1])[0])
             )
    traverse(bench_name_to_dir["hd"],
             lambda f: f.endswith(".sl"),
             lambda f, index: hd_list.append(os.path.splitext(os.path.split(f)[1])[0])
             )
    traverse(bench_name_to_dir["crypto"],
             lambda f: f.endswith(".sl"),
             lambda f, index: crypto_list.append(os.path.splitext(os.path.split(f)[1])[0])
             )
    traverse(bench_name_to_dir["lobster"],
             lambda f: f.endswith(".sl"),
             lambda f, index: lobster_list.append(os.path.splitext(os.path.split(f)[1])[0])
             )
    traverse(bench_name_to_dir["pbe-bitvec"],
             lambda f: f.endswith(".sl"),
             lambda f, index: pbe_bitvec_list.append(os.path.splitext(os.path.split(f)[1])[0])
             )
    return {
        "deobfusc": (deobfusc_list, frozenset(deobfusc_list), pd.DataFrame({"problem": deobfusc_list})),
        "hd": (hd_list, frozenset(hd_list), pd.DataFrame({"problem": hd_list})),
        "crypto": (crypto_list, frozenset(crypto_list), pd.DataFrame({"problem": crypto_list})),
        "lobster": (lobster_list, frozenset(lobster_list), pd.DataFrame({"problem": lobster_list})),
        "pbe-bitvec": (pbe_bitvec_list, frozenset(pbe_bitvec_list), pd.DataFrame({"problem": pbe_bitvec_list})),
    }


def parse_csv_result(line: str) -> Tuple[str, str, str, Optional[float], Optional[int], Optional[str]]:
    try:
        solver, problem, sol_time_str, sol_size_str, sol = line.strip().split(sep=",")
        try:
            if sol == "timeout":
                sol_type = "timeout"
                sol_time = None
                sol_size = None
                sol = None
            elif sol == "fail_with_max_size":
                sol_type = "nosol"
                sol_time = float(sol_time_str)
                sol_size = None
                sol = None
            elif sol == "failure":
                sol_type = "failure"
                sol_time = None
                sol_size = None
                sol = None
            else:
                sol_type = "success"
                sol_time = float(sol_time_str)
                sol_size = int(sol_size_str)
        except:
            log_write_with_time(f"tokenized but bad format: {solver}, {problem}, {sol_time_str}, {sol_size_str}, {sol}")
            raise
    except:
        log_write_with_time(f"bad comma-separated data: {line}")
        raise

    return solver, problem, sol_type, sol_time, sol_size, sol


def read_all() -> pd.DataFrame:
    solver_list: List[str] = list()
    problem_list: List[str] = list()
    sol_type_list: List[str] = list()
    sol_time_list: List[Optional[float]] = list()
    sol_size_list: List[Optional[int]] = list()
    sol_list: List[Optional[str]] = list()

    def read_and_add(f, index):
        with open(f, "rt") as fin:
            for line in fin.readlines():
                if len(line.strip()) == 0:
                    pass
                else:
                    solver, problem, sol_type, sol_time, sol_size, sol = parse_csv_result(line)
                    solver_list.append(solver)
                    problem_list.append(problem)
                    sol_type_list.append(sol_type)
                    sol_time_list.append(sol_time)
                    sol_size_list.append(sol_size)
                    sol_list.append(sol)

    log_write_with_time(f"read all data in {result_root_path}...")
    traverse(result_root_path,
             is_target=lambda path: os.path.split(path)[1].endswith(".result.txt"),
             target_handler=read_and_add)

    df = pd.DataFrame({"solver": solver_list,
                       "problem": problem_list,
                       "sol_type": sol_type_list,
                       "time": sol_time_list,
                       "size": sol_size_list,
                       "solution": sol_list})

    log_write_with_time(f"done. read {len(df.index)} elements.")
    return df


def build_time_cmp_table(key_df, abs_df, duet_df, probe_df=None):
    accum_df = key_df.join(abs_df.rename(columns={'time': 'abs'})['abs'], on='problem')
    accum_df = accum_df.join(duet_df.rename(columns={'time': 'duet'})['duet'], on='problem')

    if probe_df is not None:
        accum_df = accum_df.join(probe_df.rename(columns={'time': 'probe'})['probe'], on='problem')
        accum_df['win'] = accum_df[['abs', 'duet', 'probe']].idxmin(axis=1)
    else:
        accum_df['win'] = accum_df[['abs', 'duet']].idxmin(axis=1)

    return accum_df

def main():
    parser = argparse.ArgumentParser(description='print statistics')

    parser.add_argument('-log', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        dest='log_out',
                        help='test progress log print to... (default: stdout)')

    args = parser.parse_args()

    common_util.log_out = args.log_out

    problem_list = gen_problem_list()

    main_df = read_all()

    # table of each solver
    abs_synth_df = main_df[main_df["solver"] == "abs_synth"].set_index("problem")
    duet_df = main_df[main_df["solver"] == "duet"].set_index("problem")
    probe_df = main_df[main_df["solver"] == "probe"].set_index("problem")

    # comparison table for counting best solver
    hd_cmp_df = build_time_cmp_table(problem_list["hd"][2], abs_synth_df, duet_df, probe_df)
    deobfusc_cmp_df = build_time_cmp_table(problem_list["deobfusc"][2], abs_synth_df, duet_df, probe_df)
    lobster_cmp_df = build_time_cmp_table(problem_list["lobster"][2], abs_synth_df, duet_df)
    crypto_cmp_df = build_time_cmp_table(problem_list["crypto"][2], abs_synth_df, duet_df)
    pbe_bv_cmp_df = build_time_cmp_table(problem_list["pbe-bitvec"][2], abs_synth_df, duet_df)


if __name__ == '__main__':
    main()
