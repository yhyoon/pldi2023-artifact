from typing import Optional, Tuple, List, Dict, FrozenSet

import argparse
import re
import matplotlib.pyplot as plt
import pandas as pd

import common_util
from common_util import *


def gen_problems() -> Tuple[Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]], Dict[str, str]]:
    problem_map: Dict[str, str] = dict()
    problem_list_map: Dict[str, List[str]] = {
        "deobfusc": list(),
        "hd": list(),
        "crypto": list(),
        "lobster": list(),
        "pbe-bitvec": list(),
    }

    def add_to(bench_name: str, problem_file_path: str):
        problem_name = os.path.splitext(os.path.split(problem_file_path)[1])[0]
        problem_list_map[bench_name].append(problem_name)
        problem_map[problem_name] = bench_name

    for b in ["deobfusc", "hd", "crypto", "lobster", "pbe-bitvec"]:
        traverse(bench_name_to_dir[b],
                 lambda f: f.endswith(".sl"),
                 lambda f, index: add_to(b, f)
                 )

    return {b: (problem_list_map[b], frozenset(problem_list_map[b]), pd.DataFrame({"problem": problem_list_map[b]}).set_index('problem'))
            for b in ["deobfusc", "hd", "crypto", "lobster", "pbe-bitvec"]}, problem_map


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
            elif sol == "failure" or sol_size_str.endswith(")"):
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


def read_all(problem_list: Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]], problem_bench_map: Dict[str, str]) -> pd.DataFrame:
    solver_list: List[str] = list()
    bench_list: List[str] = list()
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
                    bench_list.append(problem_bench_map[problem])
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
                       "bench": bench_list,
                       "problem": problem_list,
                       "sol_type": sol_type_list,
                       "time": sol_time_list,
                       "size": sol_size_list,
                       "solution": sol_list})

    log_write_with_time(f"done. read {len(df.index)} elements.")
    return df


def build_time_cmp_table(key_df, abs_df, duet_df, probe_df=None) -> pd.DataFrame:
    accum_df: pd.DataFrame = key_df.join(abs_df.rename(columns={'time': 'abs'})['abs'])
    accum_df: pd.DataFrame = accum_df.join(duet_df.rename(columns={'time': 'duet'})['duet'])

    if probe_df is not None:
        accum_df: pd.DataFrame = accum_df.join(probe_df.rename(columns={'time': 'probe'})['probe'])
        accum_df['win'] = accum_df[['abs', 'duet', 'probe']].idxmin(axis=1)
    else:
        accum_df['win'] = accum_df[['abs', 'duet']].idxmin(axis=1)

    return accum_df.sort_index()


def main():
    parser = argparse.ArgumentParser(description='print statistics')

    parser.add_argument('-log', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        dest='log_out',
                        help='test progress log print to... (default: stdout)')

    args = parser.parse_args()

    common_util.log_out = args.log_out

    problem_list, problem_bench_map = gen_problems()

    main_df = read_all(problem_list, problem_bench_map)

    # table of each solver
    abs_synth_df = main_df[main_df["solver"] == "abs_synth"].set_index("problem")
    duet_df = main_df[main_df["solver"] == "duet"].set_index("problem")
    probe_df = main_df[main_df["solver"] == "probe"].set_index("problem")
    solver_to_df: Dict[str, pd.DataFrame] = {
        solver: main_df[main_df["solver"] == solver].set_index("problem")
        for solver in ["abs_synth", "duet", "probe"]
    }
    solver_bench_to_df: Dict[str, Dict[str, pd.DataFrame]] = {
        solver: {
            bench: solver_to_df[solver][solver_to_df[solver]["bench"] == bench]
            for bench in ["deobfusc", "hd", "lobster", "crypto", "pbe-bitvec"]
        }
        for solver in ["abs_synth", "duet", "probe"]
    }

    # comparison table for counting best solver
    hd_cmp_df = build_time_cmp_table(problem_list["hd"][2], abs_synth_df, duet_df, probe_df)
    deobfusc_cmp_df = build_time_cmp_table(problem_list["deobfusc"][2], abs_synth_df, duet_df, probe_df)
    lobster_cmp_df = build_time_cmp_table(problem_list["lobster"][2], abs_synth_df, duet_df)
    crypto_cmp_df = build_time_cmp_table(problem_list["crypto"][2], abs_synth_df, duet_df)
    pbe_bv_cmp_df = build_time_cmp_table(problem_list["pbe-bitvec"][2], abs_synth_df, duet_df)

    # main summary table
    figure_3_c = {
        "solved": {
            solver: {
                bench: solver_bench_to_df[solver][bench]["time"].count()
                for bench in ["deobfusc", "hd", "lobster", "crypto", "pbe-bitvec"]
            }
            for solver in ["abs_synth", "duet", "probe"]
        },
        "time_avg": {
            solver: {
                bench: solver_bench_to_df[solver][bench]["time"].mean()
                for bench in ["deobfusc", "hd", "lobster", "crypto", "pbe-bitvec"]
            }
            for solver in ["abs_synth", "duet", "probe"]
        },
        "time_med": {
            solver: {
                bench: solver_bench_to_df[solver][bench]["time"].median()
                for bench in ["deobfusc", "hd", "lobster", "crypto", "pbe-bitvec"]
            }
            for solver in ["abs_synth", "duet", "probe"]
        },
        "size_avg": {
            solver: {
                bench: solver_bench_to_df[solver][bench]["size"].mean()
                for bench in ["deobfusc", "hd", "lobster", "crypto", "pbe-bitvec"]
            }
            for solver in ["abs_synth", "duet", "probe"]
        },
        "size_med": {
            solver: {
                bench: solver_bench_to_df[solver][bench]["size"].median()
                for bench in ["deobfusc", "hd", "lobster", "crypto", "pbe-bitvec"]
            }
            for solver in ["abs_synth", "duet", "probe"]
        }
    }
    print(figure_3_c)


if __name__ == '__main__':
    main()
