from typing import Optional, NamedTuple

import argparse
import itertools
import json
import matplotlib.pyplot as plt
import numpy
import random

import solvers
import common_util
from common_util import *


AllDfs = NamedTuple('AllDfs',
                    main_df=pd.DataFrame,
                    solver_to_df=Dict[str, pd.DataFrame],
                    solver_bench_to_df=Dict[str, Dict[str, pd.DataFrame]],
                    bench_to_cmp_df=Dict[str, pd.DataFrame])


ResultRow = NamedTuple('ResultRow', [('solver_name', str),
                                     ('problem', str),
                                     ('sol_type', str),
                                     ('time', Optional[float]),
                                     ('size', Optional[int]),
                                     ('sol', Optional[str])])


def parse_csv_result(line: str) -> ResultRow:
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

    return ResultRow(solver, problem, sol_type, sol_time, sol_size, sol)


def read_all() -> pd.DataFrame:
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
                    row = parse_csv_result(line)
                    solver_list.append(row.solver_name)
                    bench_list.append(problem_bench_map[row.problem])
                    problem_list.append(row.problem)
                    sol_type_list.append(row.sol_type)
                    sol_time_list.append(row.time)
                    sol_size_list.append(row.size)
                    sol_list.append(row.sol)

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


def build_time_cmp_table(problem_df, simba_df, duet_df, probe_df=None) -> pd.DataFrame:
    accum_df: pd.DataFrame = problem_df.join(
        simba_df.rename(columns={"time": "simba", "size": "simba_size"})[["simba", "simba_size"]]
    )
    accum_df: pd.DataFrame = accum_df.join(
        duet_df.rename(columns={"time": "duet", "size": "duet_size"})[["duet", "duet_size"]]
    )

    if probe_df is not None:
        accum_df: pd.DataFrame = accum_df.join(
            probe_df.rename(columns={"time": "probe", "size": "probe_size"})[["probe", "probe_size"]]
        )
        accum_df["fastest"] = accum_df[["simba", "duet", "probe"]].idxmin(axis=1)
    else:
        accum_df["fastest"] = accum_df[["simba", "duet"]].idxmin(axis=1)

    return accum_df.sort_index()


def health_check_solver_bench(s, b) -> List[Tuple[str, str]]:
    # health check
    status_tbl = solvers.all_result_status_tbl()
    required_pairs = list()
    for solver in s:
        for bench in b:
            if status_tbl[solver][bench]["no_result"] > 0 and solvers.solver_map[solver].solvable(bench):
                required_pairs.append((solver, bench))
    return required_pairs


def health_check_solver_problem(s, p) -> List[Tuple[str, str]]:
    required_pairs = list()
    for solver_name in s:
        for problem in p:
            if solvers.result_status(solver_name, problem) == "no_result" and solvers.solver_map[solver_name].solvable(problem_bench_map[problem]):
                required_pairs.append((solver_name, problem))
    return required_pairs


# draw figures: cactus
def draw_cactus(bench_name: str, file_name: str, all_problem_count, tds, *, mark_every=None, xtick_step=None, y_size=None):
    if y_size is not None:
        figure = plt.figure(figsize=(9, y_size))
    else:
        figure = plt.figure()
    ax: plt.axes.Axes = figure.subplots()
    ax.set_title(bench_name, fontsize=24)
    ax.set_xlabel(f"# Solved instances (total = {all_problem_count})")
    ax.set_ylabel("Total Solving Time (s)")

    if xtick_step is None:
        xtick_step = all_problem_count // 8

    if mark_every is None:
        mark_every = xtick_step // 4

    for td in tds:
        cum_time_df = td['time_df'].cumsum()
        ax.plot(
            cum_time_df,
            label=td['label'] + f' (solved = {cum_time_df.count()})',
            color=td['color'],
            marker=td['marker'],
            markersize=10,
            markevery=mark_every,
            fillstyle='none'
        )

    if any(ytick > 100000 for ytick in ax.get_yticks()):
        ax.tick_params(axis='both', which='major', labelsize=14)
    else:
        ax.tick_params(axis='both', which='major', labelsize=16)

    ax.legend(loc='upper left')
    figure.savefig(os.path.join(artifact_root_path, "figures", f"cactus_{file_name}.png"),
                   transparent=True)
    log_write_with_time(f"created figures/cactus_{file_name}.png")


def draw_stack_bar(kind: str, ylabel: str, tool_lbls: List[str], bench_lbls: List[str], colors: List[str],
                   cnts_list: List[List[int]]):
    sum_cnts = [sum(x) for x in zip(*cnts_list)]
    figure = plt.figure()
    ax: plt.axes.Axes = figure.subplots()
    ax.set_ylabel(ylabel)
    ax.set_ylim((0, max(sum_cnts) + 100))
    for ytickline in ax.get_yticklines():
        ytickline.set(color='grey', alpha=0.3)

    ax.set_axisbelow(True)
    ax.grid(axis='y', color='grey', alpha=0.3)

    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    prev_cnts = None
    accum_cnts = None
    prev_smalls = None
    for bench_lbl, cnts, color in zip(bench_lbls, cnts_list, colors):
        if prev_cnts is None:
            cur_br = ax.bar(tool_lbls, cnts, color=color, label=bench_lbl)
            accum_cnts = cnts[:]
            prev_smalls = []
        else:
            cur_br = ax.bar(tool_lbls, cnts, color=color, bottom=prev_cnts, label=bench_lbl)
            accum_cnts = [sum(x) for x in zip(accum_cnts, cnts)]
        prev_cnts = cnts

        next_smalls = list()
        if any(cnt < 25 for cnt in cnts):
            # custom label
            for i, (cnt, accum_cnt) in enumerate(zip(cnts, accum_cnts)):
                if cnt < 25:
                    next_smalls.append(i)
                    if i in prev_smalls:
                        ax.text(i, accum_cnt + 64, s=str(cnt),
                                fontsize=24, weight='heavy', ha='center', va='top')
                    else:
                        ax.text(i, accum_cnt + 25, s=str(cnt),
                                fontsize=24, weight='heavy', ha='center', va='top')
                else:
                    ax.text(i, (accum_cnt - cnt) + cnt // 2, s=str(cnt),
                            fontsize=24, weight='heavy', ha='center', va='center')
        else:
            ax.bar_label(cur_br, fontsize=24, weight='heavy', label_type='center')
        prev_smalls = next_smalls

    for i, sum_cnt in enumerate(sum_cnts):
        ax.text(i, max(sum_cnts) + 50, s=str(sum_cnt),
                fontsize=24, weight='heavy', ha='center',
                bbox={'boxstyle': 'square', 'facecolor': 'white', 'edgecolor': 'black'})
    figure.legend(loc='upper center', ncol=2, frameon=False)
    figure.savefig(os.path.join(artifact_root_path, "figures", f"bar_{kind}.png"),
                   transparent=True)
    log_write_with_time(f"created figures/bar_{kind}.png")


# figure 2: overall cactus plots
def draw_cactus_plots(problem_list: Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]],
                      solver_bench_to_df: Dict[str, Dict[str, pd.DataFrame]]):
    required_pairs = health_check_solver_bench(["simba", "duet"], ["lobster"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_cactus("Lobster", "lobster", len(problem_list["lobster"][0]), [
        {'time_df': solver_bench_to_df["duet"]["lobster"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["simba"]["lobster"]["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'},
    ], xtick_step=41)

    required_pairs = health_check_solver_bench(["simba", "duet"], ["crypto"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_cactus("Crypto", "crypto", len(problem_list["crypto"][0]), [
        {'time_df': solver_bench_to_df["duet"]["crypto"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["simba"]["crypto"]["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'},
    ])

    required_pairs = health_check_solver_bench(solver_names, ["hd"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_cactus("Hacker's Delight", "hd", len(problem_list["hd"][0]), [
        {'time_df': solver_bench_to_df["duet"]["hd"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["probe"]["hd"]["time"].sort_values(ignore_index=True),
         'label': "PROBE", 'color': 'r', 'marker': 'v'},
        {'time_df': solver_bench_to_df["simba"]["hd"]["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'},
    ], xtick_step=4)

    required_pairs = health_check_solver_bench(solver_names, ["deobfusc"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_cactus("Deobfuscation", "deob", len(problem_list["deobfusc"][0]), [
        {'time_df': solver_bench_to_df["duet"]["deobfusc"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["probe"]["deobfusc"]["time"].sort_values(ignore_index=True),
         'label': "PROBE", 'color': 'r', 'marker': 'v'},
        {'time_df': solver_bench_to_df["simba"]["deobfusc"]["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'},
    ], xtick_step=50)

    required_pairs = health_check_solver_bench(solver_names, ["hd", "deobfusc"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_cactus("BitVec (HD+DEOBFUSC)", "bitvec", len([*problem_list["hd"][0], *problem_list["deobfusc"][0]]), [
        {'time_df': pd.concat(
            [
                solver_bench_to_df["duet"]["hd"],
                solver_bench_to_df["duet"]["deobfusc"]
            ])["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': pd.concat(
            [
                solver_bench_to_df["probe"]["hd"],
                solver_bench_to_df["probe"]["deobfusc"]
            ])["time"].sort_values(ignore_index=True),
         'label': "PROBE", 'color': 'r', 'marker': 'v'},
        {'time_df': pd.concat(
            [
                solver_bench_to_df["simba"]["hd"],
                solver_bench_to_df["simba"]["deobfusc"]
            ])["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'}
    ])

    required_pairs = health_check_solver_bench(["simba", "duet"], ["lobster", "crypto"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")

    draw_cactus("CIRCUIT (LOBSTER+CRYPTO)", "bool", len([*problem_list["lobster"][0], *problem_list["crypto"][0]]), [
        {'time_df': pd.concat(
            [
                solver_bench_to_df["duet"]["crypto"],
                solver_bench_to_df["duet"]["lobster"]
            ])["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': pd.concat(
            [
                solver_bench_to_df["simba"]["crypto"],
                solver_bench_to_df["simba"]["lobster"]
            ])["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'},
    ])

    required_pairs = health_check_solver_bench(["simba", "duet"], ["bitvec-cond"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")

    draw_cactus("BITVEC-COND", "bitvec_cond", len(problem_list["bitvec-cond"][0]), [
        {'time_df': solver_bench_to_df["duet"]["bitvec-cond"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["simba"]["bitvec-cond"]["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'},
    ])

    required_pairs = health_check_solver_bench(["simba", *ablation_names], no_cond_bench_names)
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")

    draw_cactus("All Benchmarks", "all_ablation", len([*problem_list["hd"][0], *problem_list["deobfusc"][0], *problem_list["lobster"][0], *problem_list["crypto"][0]]), [
        {'time_df': pd.concat([
            solver_bench_to_df["simba_bf"]["hd"],
            solver_bench_to_df["simba_bf"]["deobfusc"],
            solver_bench_to_df["simba_bf"]["lobster"],
            solver_bench_to_df["simba_bf"]["crypto"],
        ])["time"].sort_values(ignore_index=True),
         'label': "BruteForce", 'color': 'g', 'marker': '^'},
        {'time_df': pd.concat([
            solver_bench_to_df["simba_smt"]["hd"],
            solver_bench_to_df["simba_smt"]["deobfusc"],
            solver_bench_to_df["simba_smt"]["lobster"],
            solver_bench_to_df["simba_smt"]["crypto"],
        ])["time"].sort_values(ignore_index=True),
         'label': "SMTSolver", 'color': 'm', 'marker': 'v'},
        {'time_df': pd.concat([
            solver_bench_to_df["simba_fonly"]["hd"],
            solver_bench_to_df["simba_fonly"]["deobfusc"],
            solver_bench_to_df["simba_fonly"]["lobster"],
            solver_bench_to_df["simba_fonly"]["crypto"],
        ])["time"].sort_values(ignore_index=True),
         'label': "ForwardOnly", 'color': 'y', 'marker': '+'},
        {'time_df': pd.concat([
            solver_bench_to_df["simba"]["hd"],
            solver_bench_to_df["simba"]["deobfusc"],
            solver_bench_to_df["simba"]["lobster"],
            solver_bench_to_df["simba"]["crypto"],
        ])["time"].sort_values(ignore_index=True),
         'label': "SIMBA", 'color': 'b', 'marker': 'o'},
    ], y_size=7)


# figure 3.(a), 3.(b): solved count and fastest count
def draw_bar_plots(solver_bench_to_df: Dict[str, Dict[str, pd.DataFrame]],
                   bench_cmp_map: Dict[str, pd.DataFrame]):
    bar_colors = ['gold', '#96b4fa']

    # stacked bar1 - bitvec cnt
    required_pairs = health_check_solver_bench(solver_names, ["deobfusc", "hd"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_stack_bar("bv_cnt", "# Solved Benchmarks", ["SIMBA", "DUET", "PROBE"], ["DEOBUSC", "HD"], bar_colors,  [
        [solver_bench_to_df[solver][bench]["time"].count() for solver in solver_names]
        for bench in ["deobfusc", "hd"]
    ])

    # stacked bar2 - bitvec fastest
    hd_win = bench_cmp_map["hd"]["fastest"].value_counts()
    deob_win = bench_cmp_map["deobfusc"]["fastest"].value_counts()
    draw_stack_bar("bv_fast", "# Fastest Solved Benchmarks", ["SIMBA", "DUET", "PROBE"], ["DEOBFUSC", "HD"], bar_colors, [
        [deob_win.get("simba", 0), deob_win.get("duet", 0), deob_win.get("probe", 0)],
        [hd_win.get("simba", 0), hd_win.get("duet", 0), hd_win.get("probe", 0)],
    ])

    # stacked bar3 - circuit cnt
    required_pairs = health_check_solver_bench(["simba", "duet"], ["lobster", "crypto"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_stack_bar("circuit_cnt", "# Solved Benchmarks", ["SIMBA", "DUET"], ["LOBSTER", "CRYPTO"], bar_colors, [
        [solver_bench_to_df[solver][bench]["time"].count() for solver in ["simba", "duet"]]
        for bench in ["lobster", "crypto"]
    ])

    # stacked bar4 - circuit fastest
    lobster_win = bench_cmp_map["lobster"]["fastest"].value_counts()
    crypto_win = bench_cmp_map["crypto"]["fastest"].value_counts()
    draw_stack_bar("circuit_fast", "# Fastest Solved Benchmarks", ["SIMBA", "DUET"], ["LOBSTER", "CRYPTO"], bar_colors, [
        [lobster_win.get("simba", 0), lobster_win.get("duet", 0)],
        [crypto_win.get("simba", 0), crypto_win.get("duet", 0)],
    ])

    # stacked bar 5 - bvcond cnt
    required_pairs = health_check_solver_bench(["simba", "duet"], ["bitvec-cond"])
    if len(required_pairs) > 0:
        log_write_with_time(f"WARN: incomplete plot. you need run {str(required_pairs)}")
    draw_stack_bar("bitvec_cond_cnt", "# Solved Benchmarks", ["SIMBA", "DUET"], ["BITVEC-COND"], ['gold'], [
        [solver_bench_to_df[solver][bench]["time"].count() for solver in ["simba", "duet"]]
        for bench in ["bitvec-cond"]
    ])

    # stacked bar6 - bvcond fastest
    bitvec_cond_win = bench_cmp_map["bitvec-cond"]["fastest"].value_counts()
    draw_stack_bar("bitvec_cond_fast", "# Fastest Solved Benchmarks", ["SIMBA", "DUET"], ["BITVEC-COND"], ['gold'], [
        [bitvec_cond_win.get("simba", 0), bitvec_cond_win.get("duet", 0)],
    ])


def draw_detail_table(dfs: AllDfs, bench_to_chosen: Dict[str, List[str]], caption, table_out):
    def solver_problem_detail(solver: str, problem: str) -> pd.Series:
        try:
            df = dfs.solver_bench_to_df[solver][problem_bench_map[problem]]
            return df.loc[problem]
        except KeyError:
            return pd.Series({"bench": problem_bench_map[problem],
                              "problem": problem,
                              "sol_type": "not_yet",
                              "time": None,
                              "size": None,
                              "solution": None})

    # table 1: randomly chosen detail table raw data
    # solver |->
    #   bench |->
    #       problem |->
    #           DataFrame row
    table_1: Dict[str, Dict[str, Dict[str, pd.Series]]] = {
        solver: {
            bench: {
                problem: solver_problem_detail(solver, problem)
                for problem in bench_to_chosen[bench]
            }
            for bench in bench_names
        }
        for solver in solver_names
    }

    def lookup_time_and_format(solver, bench, problem) -> str:
        try:
            if table_1[solver][bench][problem]["sol_type"] == "timeout":
                return "{:>9s}".format(">1h")
            elif table_1[solver][bench][problem]["sol_type"] == "failure":
                return "{:>9s}".format(">1h")
            else:
                v = table_1[solver][bench][problem]["time"]
                if v is None or numpy.isnan(v):
                    return "{:>9s}".format("-")
                else:
                    return "{:>9.2f}".format(v)
        except KeyError as exn:
            log_write_with_time(f"empty table: {solver} on {problem}: {bench}")
            return "{:>9s}".format("-")

    def lookup_size_and_format(solver, bench, problem) -> str:
        try:
            if table_1[solver][bench][problem]["sol_type"] == "timeout":
                return "{:>6s}".format("-")
            elif table_1[solver][bench][problem]["sol_type"] == "failure":
                return "{:>6s}".format("-")
            else:
                v = table_1[solver][bench][problem]["size"]
                if v is None or numpy.isnan(v):
                    return "{:>6s}".format("-")
                else:
                    return "{:>6.0f}".format(v)
        except KeyError as exn:
            log_write_with_time(f"empty table: {solver} on {problem}: {bench}")
            return "{:>6s}".format("-")

    def lookup_analysis_time(solver_name, bench, problem) -> str:
        solver = solvers.solver_map[solver_name]
        json_path = solver.result_path() + bench_name_to_dir[bench][len(bench_root_path):] + os.sep + problem + ".json"
        try:
            with open(json_path) as json_file:
                report_root = json.load(json_file)
                return "{:.2f}".format(float(report_root["prune"]["time"]))
        except FileNotFoundError:
            log_write_with_time(f"for {solver_name} {bench} {problem}, file not found: {json_path}")
            return "-"

    txt_detail_lines = [
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "".center(25, "-"),
            "".center(15, "-"), "".center(15, "-"), "".center(15, "-"), "".center(15, "-"),
        ),
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "Benchmark".center(25, " "),
            "Probe".center(15, " "),
            "Duet".center(15, " "),
            "Simba".center(15, " "),
        ),
        "{:25s}|| {:9s}{:6s}| {:9s}{:6s}| {:9s}{:6s}|".format(
            "",
            "Time".center(9, " "), "Size".center(6, " "),
            "Time".center(9, " "), "Size".center(6, " "),
            "Time".center(9, " "), "Size".center(6, " "),
        ),
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "".center(25, "-"),
            "".center(15, "-"), "".center(15, "-"), "".center(15, "-"), "".center(15, "-"),
        ),
        *[
            "{:25s}|| {:9s}{:6s}| {:9s}{:6s}| {:9s}{:6s}|".format(
                problem,
                *[
                    *[
                        lf(solver, "hd", problem)
                        for solver, lf in itertools.product(
                            ["probe", "duet", "simba"],
                            [lookup_time_and_format, lookup_size_and_format]
                        )
                    ]
                ],
            ) for problem in bench_to_chosen['hd']
        ],
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "".center(25, "-"),
            "".center(15, "-"), "".center(15, "-"), "".center(15, "-"), "".center(15, "-"),
        ),
        *[
            "{:25s}|| {:9s}{:6s}| {:9s}{:6s}| {:9s}{:6s}|".format(
                problem,
                *[
                    *[
                        lf(solver, "deobfusc", problem)
                        for solver, lf in itertools.product(
                            ["probe", "duet", "simba"],
                            [lookup_time_and_format, lookup_size_and_format]
                        )
                    ]
                ],
            ) for problem in bench_to_chosen['deobfusc']
        ],
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "".center(25, "-"),
            "".center(15, "-"), "".center(15, "-"), "".center(15, "-"), "".center(15, "-"),
        ),
        *[
            "{:25s}|| {:9s}{:6s}| {:9s}{:6s}| {:9s}{:6s}|".format(
                problem,
                *[
                    *[
                        lf(solver, "bitvec-cond", problem)
                        for solver, lf in itertools.product(
                            ["probe", "duet", "simba"],
                            [lookup_time_and_format, lookup_size_and_format]
                        )
                    ]
                ],
            ) for problem in bench_to_chosen['bitvec-cond']
        ],
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "".center(25, "-"),
            "".center(15, "-"), "".center(15, "-"), "".center(15, "-"), "".center(15, "-"),
        ),
        *[
            "{:25s}|| {:9s}{:6s}| {:9s}{:6s}| {:9s}{:6s}|".format(
                problem.replace("sygus_iter_", ""),
                *[
                    *[
                        lf(solver, "lobster", problem)
                        for solver, lf in itertools.product(
                            ["probe", "duet", "simba"],
                            [lookup_time_and_format, lookup_size_and_format]
                        )
                    ]
                ],
            ) for problem in bench_to_chosen['lobster']
        ],
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "".center(25, "-"),
            "".center(15, "-"), "".center(15, "-"), "".center(15, "-"), "".center(15, "-"),
        ),
        *[
            "{:25s}|| {:9s}{:6s}| {:9s}{:6s}| {:9s}{:6s}|".format(
                problem,
                *[
                    *[
                        lf(solver, "crypto", problem)
                        for solver, lf in itertools.product(
                            ["probe", "duet", "simba"],
                            [lookup_time_and_format, lookup_size_and_format]
                        )
                    ]
                ],
            ) for problem in bench_to_chosen['crypto']
        ],
        "{:25s}|| {:15s}| {:15s}| {:15s}|".format(
            "".center(25, "-"),
            "".center(15, "-"), "".center(15, "-"), "".center(15, "-"), "".center(15, "-"),
        ),
    ]

    all_set = set()
    for k, v in bench_to_chosen.items():
        all_set.update(v)
    # health check
    required_pairs = health_check_solver_problem(solver_names, all_set)
    if len(required_pairs) > 0:
        table_out.write(f"WARN: incomplete table. you need run {str(required_pairs)}\n")

    if caption:
        table_out.write("Table 1. Results for 25 randomly chosen benchmark problems (5 for each category).\n"
                        "Analysis times are not included in this table. You can see them by manually running\n"
                        " simba with option '-log'.\n")
    table_out.write("\n".join(txt_detail_lines))
    table_out.write("\n\n")

    tex_detail_lines = [
        "\\begin{table}",
        "  \\footnotesize",
        "  \\centering",
        "  \\caption{Results for 25 randomly chosen benchmark problems (5 for each category), ",
        "  where \\textbf{Time} gives synthesis time,",
        "  $T_{A}$ gives time spent for forward and backward analysis,",
        "  and $|P|$ shows the size of the synthesized program (measured by number of AST nodes).}",
        "  \\vspace{-0.1in}"
        "  \\label{tbl:compare_detail}",
        "  \\begin{tabular}{c|l|rr|rr|rrr}",
        "    \\toprule",
        "    Benchmark &",
        "      \\multirow{2}{*}{Benchmark} &",
        "        \\multicolumn{2}{c|}{ \\probe } & \\multicolumn{2}{c|}{ \\duet } &",
        "        \\multicolumn{3}{c}{ \\tool } \\\\",
        "    category\\! &  ",
        "      & ",
        "        \\textbf{Time} & $|P|$ & ",
        "        \\textbf{Time} & $|P|$ & ",
        "        \\textbf{Time} & $T_{A}$ & $|P|$  \\\\",
        "    \\hline",
        "    \\multirow{5}{*}{\\textsc{HD}}",
        *[
            "      & {:25s} &  {:s} & {:s} &  {:s} & {:s} &  {:s} & {:s} & {:s} \\\\".format(
                problem.replace("_", "\\_"),
                lookup_time_and_format("probe", "hd", problem),
                lookup_size_and_format("probe", "hd", problem),
                lookup_time_and_format("duet", "hd", problem),
                lookup_size_and_format("duet", "hd", problem),
                lookup_time_and_format("simba", "hd", problem),
                lookup_analysis_time("simba", "hd", problem),
                lookup_size_and_format("simba", "hd", problem),
            ) for problem in bench_to_chosen['hd']
        ],
        "    \\hline",
        "    \\multirow{5}{*}{\\textsc{Deobfusc}}",
        *[
            "      & {:25s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} \\\\".format(
                problem.replace("_", "\\_"),
                lookup_time_and_format("probe", "deobfusc", problem),
                lookup_size_and_format("probe", "deobfusc", problem),
                lookup_time_and_format("duet", "deobfusc", problem),
                lookup_size_and_format("duet", "deobfusc", problem),
                lookup_time_and_format("simba", "deobfusc", problem),
                lookup_analysis_time("simba", "deobfusc", problem),
                lookup_size_and_format("simba", "deobfusc", problem),
            ) for problem in bench_to_chosen['deobfusc']
        ],
        "    \\hline",
        "    \\multirow{5}{*}{\\textsc{BitVec-Cond}}",
        *[
            "      & {:25s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} \\\\".format(
                problem.replace("_", "\\_"),
                lookup_time_and_format("probe", "bitvec-cond", problem),
                lookup_size_and_format("probe", "bitvec-cond", problem),
                lookup_time_and_format("duet", "bitvec-cond", problem),
                lookup_size_and_format("duet", "bitvec-cond", problem),
                lookup_time_and_format("simba", "bitvec-cond", problem),
                lookup_analysis_time("simba", "bitvec-cond", problem),
                lookup_size_and_format("simba", "bitvec-cond", problem),
            ) for problem in bench_to_chosen['bitvec-cond']
        ],
        "    \\hline",
        "    \\multirow{5}{*}{\\textsc{Lobster}}",
        *[
            "      & {:25s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} \\\\".format(
                problem.replace("sygus_iter_", "").replace("_", "\\_"),
                lookup_time_and_format("probe", "lobster", problem),
                lookup_size_and_format("probe", "lobster", problem),
                lookup_time_and_format("duet", "lobster", problem),
                lookup_size_and_format("duet", "lobster", problem),
                lookup_time_and_format("simba", "lobster", problem),
                lookup_analysis_time("simba", "lobster", problem),
                lookup_size_and_format("simba", "lobster", problem),
            ) for problem in bench_to_chosen['lobster']
        ],
        "    \\hline",
        "    \\multirow{5}{*}{\\textsc{Crypto}}",
        *[
            "      & {:25s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} & {:s} \\\\".format(
                problem.replace("_", "\\_"),
                lookup_time_and_format("probe", "crypto", problem),
                lookup_size_and_format("probe", "crypto", problem),
                lookup_time_and_format("duet", "crypto", problem),
                lookup_size_and_format("duet", "crypto", problem),
                lookup_time_and_format("simba", "crypto", problem),
                lookup_analysis_time("simba", "crypto", problem),
                lookup_size_and_format("simba", "crypto", problem),
            ) for problem in bench_to_chosen['crypto']
        ],
        "    \\bottomrule",
        "  \\end{tabular}",
        "  \\vspace{-0.2in}"
        "\\end{table}"
    ]

    if caption:
        with open(os.path.join(artifact_root_path, "figures", "tbl_sample_detail.tex"), "wt") as f:
            f.write("\n".join(tex_detail_lines))
        log_write_with_time("created tbl_sample_detail.tex: randomly chosen 5 samples for each domains")


def draw_cmp_table(dfs: AllDfs, cmp_bench_names: List[str], table_out):
    for bench_name in cmp_bench_names:
        cmp_df = dfs.bench_to_cmp_df[bench_name]
        table_out.write(cmp_df.to_string())
        table_out.write("\n")


def draw_ablation_table(dfs: AllDfs, table_out):
    solver_var_to_non_ite_df = {
        solver: pd.concat([dfs.solver_bench_to_df[solver][bench] for bench in no_cond_bench_names])
        for solver in ["simba", *ablation_names]
    }

    # figure 4.(b): ablation summary table raw data
    # item(solved|time_avg|size_avg) |->
    #   solver_variation |->
    #       bench(hd|deobfusc|lobster|crypto) |->
    #           value(count|average)
    ablation_summary: Dict[str, Dict[str, Dict[str, Any]]] = {
        "solved": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["time"].count()
                    for bench in bench_names
                },
                "overall": solver_var_to_non_ite_df[solver]["time"].count()
            }
            for solver in ["simba", *ablation_names]
        },
        "time_avg": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["time"].mean() if dfs.solver_bench_to_df[solver][bench]["time"].count() > 0 else numpy.nan
                    for bench in bench_names
                },
                "overall": solver_var_to_non_ite_df[solver]["time"].mean() if solver_var_to_non_ite_df[solver]["time"].count() > 0 else numpy.nan
            }
            for solver in ["simba", *ablation_names]
        },
        "size_avg": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["size"].mean() if dfs.solver_bench_to_df[solver][bench]["size"].count() > 0 else numpy.nan
                    for bench in bench_names
                },
                "overall": solver_var_to_non_ite_df[solver]["size"].mean() if solver_var_to_non_ite_df[solver]["size"].count() > 0 else numpy.nan
            }
            for solver in ["simba", *ablation_names]
        },
    }

    ablations_in_order = ["simba", "simba_fonly", "simba_smt", "simba_bf"]

    txt_summary_lines = [
        "{:12s}|| {:27s}| {:27s}| {:27s}|".format(
            "".center(12, "-"),
            "".center(27, "-"), "".center(27, "-"), "".center(27, "-")
        ),
        "{:12s}|| {:27}| {:27}| {:27}|".format(
            "Benchmark".center(12, " "),
            "# Solved".center(27, " "),
            "Time(Average)".center(27, " "),
            "Size(Average)".center(27, " "),
        ),
        "{:12s}|| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}|".format(
            "category".center(12, " "),
            "S".center(6, " "), "F".center(6, " "), "V".center(6, " "), "B".center(6, " "),
            "S".center(6, " "), "F".center(6, " "), "V".center(6, " "), "B".center(6, " "),
            "S".center(6, " "), "F".center(6, " "), "V".center(6, " "), "B".center(6, " "),
        ),
        "{:12s}|| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}|".format(
            "".center(12, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
        ),
        "{:12s}|| {:6.0f}|{:6.0f}|{:6.0f}|{:6.0f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}|".format(
            "HD".center(12, " "),
            *[ablation_summary['solved'][solver]['hd'] for solver in ablations_in_order],
            *[ablation_summary['time_avg'][solver]['hd'] for solver in ablations_in_order],
            *[ablation_summary['size_avg'][solver]['hd'] for solver in ablations_in_order],
        ),
        "{:12s}|| {:6.0f}|{:6.0f}|{:6.0f}|{:6.0f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}|".format(
            "DEOBFUSC".center(12, " "),
            *[ablation_summary['solved'][solver]['deobfusc'] for solver in ablations_in_order],
            *[ablation_summary['time_avg'][solver]['deobfusc'] for solver in ablations_in_order],
            *[ablation_summary['size_avg'][solver]['deobfusc'] for solver in ablations_in_order],
        ),
        "{:12s}|| {:6.0f}|{:6.0f}|{:6.0f}|{:6.0f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}|".format(
            "LOBSTER".center(12, " "),
            *[ablation_summary['solved'][solver]['lobster'] for solver in ablations_in_order],
            *[ablation_summary['time_avg'][solver]['lobster'] for solver in ablations_in_order],
            *[ablation_summary['size_avg'][solver]['lobster'] for solver in ablations_in_order],
        ),
        "{:12s}|| {:6.0f}|{:6.0f}|{:6.0f}|{:6.0f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}|".format(
            "CRYPTO".center(12, " "),
            *[ablation_summary['solved'][solver]['crypto'] for solver in ablations_in_order],
            *[ablation_summary['time_avg'][solver]['crypto'] for solver in ablations_in_order],
            *[ablation_summary['size_avg'][solver]['crypto'] for solver in ablations_in_order],
        ),
        "{:12s}|| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}|".format(
            "".center(12, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
        ),
        "{:12s}|| {:6.0f}|{:6.0f}|{:6.0f}|{:6.0f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}| {:6.1f}|{:6.1f}|{:6.1f}|{:6.1f}|".format(
            "Overall".center(12, " "),
            *[ablation_summary['solved'][solver]['overall'] for solver in ablations_in_order],
            *[ablation_summary['time_avg'][solver]['overall'] for solver in ablations_in_order],
            *[ablation_summary['size_avg'][solver]['overall'] for solver in ablations_in_order],
        ),
        "{:12s}|| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|{:6s}|".format(
            "".center(12, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
            "".center(6, "-"), "".center(6, "-"), "".center(6, "-"), "".center(6, "-"),
        ),
    ]

    txt_summary_lines = [line.replace("nan", "  -") for line in txt_summary_lines]

    required_pairs = health_check_solver_bench(["simba", *ablation_names], no_cond_bench_names)
    if len(required_pairs) > 0:
        table_out.write(f"WARN: incomplete table. you need run {str(required_pairs)}\n")

    table_out.write("Fig. 4. (b) Statistics for the solving times and solution sizes."
                    "S(imba), F(orwardOnly), V(SMTSolver), B(ruteForce).\n")
    table_out.write("\n".join(txt_summary_lines))
    table_out.write("\n\n")

    tex_summary_lines = [
        "\\begin{tabular}{c|r|r|r|r|r|r|r|r}",
        #"\\begin{tabular}{c|r|r|r|r|r|r|r|r|r|r|r|r}",
        "\\hline",
        "Benchmark &",
        "  \\multicolumn{4}{c|}{\\# Solved} &",
        "    \\multicolumn{4}{c}{Time (Average)} \\\\ % &",
        #"    \\multicolumn{4}{c|}{Time (Average)} \\\\ % &",
        # "      \\multicolumn{4}{c}{Size (Average)} \\\\",
        # "        \\cline{2-13}",
        "        \\cline{2-9}",
        "category\\! &",
        "  {\\bf S} & {\\bf FW} & {\\bf SMT} & {\\bf BF} &",
        "    {\\bf S} & {\\bf FW} & {\\bf SMT} & {\\bf BF} \\\\ % &",
        # "      {\\bf S} & {\\bf F} & {\\bf V} & {\\bf B} \\\\",
        "\\hline \\hline",
        "\\textsc{HD} \\! &",
        "  {:.0f} &  {:.0f} & {:.0f} & {:.0f} &".format(*[ablation_summary['solved'][solver]['hd'] for solver in ablations_in_order]),
        "    {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm] % &".format(*[ablation_summary['time_avg'][solver]['hd'] for solver in ablations_in_order]),
        # "      {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm]".format(*[ablation_summary['size_avg'][solver]['hd'] for solver in ablations_in_order]),
        "\\textsc{Deobfusc}\\! &",
        "  {:.0f} &  {:.0f} & {:.0f} & {:.0f} &".format(*[ablation_summary['solved'][solver]['deobfusc'] for solver in ablations_in_order]),
        "    {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm] % &".format(*[ablation_summary['time_avg'][solver]['deobfusc'] for solver in ablations_in_order]),
        # "      {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm]".format(*[ablation_summary['size_avg'][solver]['deobfusc'] for solver in ablations_in_order]),
        "\\textsc{Lobster}\\! &",
        "  {:.0f} &  {:.0f} & {:.0f} & {:.0f} &".format(*[ablation_summary['solved'][solver]['lobster'] for solver in ablations_in_order]),
        "    {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm] % &".format(*[ablation_summary['time_avg'][solver]['lobster'] for solver in ablations_in_order]),
        # "      {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm]".format(*[ablation_summary['size_avg'][solver]['lobster'] for solver in ablations_in_order]),
        "\\textsc{Crypto}\\! &",
        "  {:.0f} &  {:.0f} & {:.0f} & {:.0f} &".format(*[ablation_summary['solved'][solver]['crypto'] for solver in ablations_in_order]),
        "    {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm] % &".format(*[ablation_summary['time_avg'][solver]['crypto'] for solver in ablations_in_order]),
        # "      {:.1f} &  {:.1f} & {:.1f} & {:.1f} \\\\ [0.3mm]".format(*[ablation_summary['size_avg'][solver]['crypto'] for solver in ablations_in_order]),
        "\\hline",
        "{\\bf Overall}\\! &",
        "  {{\\bf {:.0f}}} &  {{\\bf {:.0f}}} & {{\\bf {:.0f}}} & {{\\bf {:.0f}}} &".format(*[ablation_summary['solved'][solver]['overall'] for solver in ablations_in_order]),
        "    {{\\bf {:.1f}}} &  {{\\bf {:.1f}}} & {{\\bf {:.1f}}} & {{\\bf {:.1f}}} \\\\ [0.3mm] % &".format(*[ablation_summary['time_avg'][solver]['overall'] for solver in ablations_in_order]),
        # "      {{\\bf {:.1f}}} &  {{\\bf {:.1f}}} & {{\\bf {:.1f}}} & {{\\bf {:.1f}}} \\\\ [0.3mm]".format(*[ablation_summary['size_avg'][solver]['overall'] for solver in ablations_in_order]),
        "\\hline",
        "\\end{tabular}"
    ]

    tex_summary_lines = [line.replace("nan", "  -") for line in tex_summary_lines]

    with open(os.path.join(artifact_root_path, "figures", "tbl_ablation_summary.tex"), "wt") as f:
        f.write("\n".join(tex_summary_lines))
        log_write_with_time("created figures/tbl_ablation_summary.tex: statistics for ablation study")


def prepare_df() -> AllDfs:
    main_df = read_all()

    # table of each solver
    solver_to_df: Dict[str, pd.DataFrame] = {
        solver: main_df[main_df["solver"] == solver].set_index("problem").sort_index()
        for solver in [*solver_names, *ablation_names, *ex_cut_names]
    }

    solver_bench_to_df: Dict[str, Dict[str, pd.DataFrame]] = {
        solver: {
            bench: solver_to_df[solver][solver_to_df[solver]["bench"] == bench]
            for bench in ["deobfusc", "hd", "lobster", "crypto", "bitvec-cond"]
        }
        for solver in [*solver_names, *ablation_names, *ex_cut_names]
    }

    simba_df, duet_df, probe_df = solver_to_df["simba"], solver_to_df["duet"], solver_to_df["probe"]
    # comparison table for counting best solver
    hd_cmp_df = build_time_cmp_table(problem_map["hd"][2], simba_df, duet_df, probe_df)
    deobfusc_cmp_df = build_time_cmp_table(problem_map["deobfusc"][2], simba_df, duet_df, probe_df)
    lobster_cmp_df = build_time_cmp_table(problem_map["lobster"][2], simba_df, duet_df)
    crypto_cmp_df = build_time_cmp_table(problem_map["crypto"][2], simba_df, duet_df)
    bvcond_cmp_df = build_time_cmp_table(problem_map["bitvec-cond"][2], simba_df, duet_df, probe_df)
    bench_to_cmp_df: Dict[str, pd.DataFrame] = {
        "hd": hd_cmp_df,
        "deobfusc": deobfusc_cmp_df,
        "lobster": lobster_cmp_df,
        "crypto": crypto_cmp_df,
        "bitvec-cond": bvcond_cmp_df,
    }

    return AllDfs(main_df, solver_to_df, solver_bench_to_df, bench_to_cmp_df)


def show_simba_probe_size_numbers(dfs: AllDfs):
    a_p_both_solved_hd = dfs.bench_to_cmp_df["hd"].dropna(subset=['simba_size', 'probe_size'])
    a_both_mean = a_p_both_solved_hd['simba_size'].mean()
    p_both_mean = a_p_both_solved_hd['probe_size'].mean()
    a_only_hd = dfs.bench_to_cmp_df["hd"].dropna(subset=['simba_size'])
    a_only_hd = a_only_hd[a_only_hd["probe_size"].isna()]
    p_only_hd = dfs.bench_to_cmp_df["hd"].dropna(subset=['probe_size'])
    p_only_hd = p_only_hd[p_only_hd["simba_size"].isna()]
    a_only_mean, a_only_cnt = a_only_hd['simba_size'].mean(), a_only_hd['simba_size'].count()
    p_only_mean, p_only_cnt = p_only_hd['probe_size'].mean(), p_only_hd['probe_size'].count()

    log_write_with_time(f"For HD, 'simba probe both solved' problems avg size = [{a_both_mean:.1f}, {p_both_mean:.1f}]")
    log_write_with_time(f"simba only avg size = {a_only_mean:.1f} for {a_only_cnt:d}, probe only avg size = {p_only_mean:.1f} for {p_only_cnt:d}")

    a_p_both_solved_deobfusc = dfs.bench_to_cmp_df["deobfusc"].dropna(subset=['simba_size', 'probe_size'])
    a_both_mean = a_p_both_solved_deobfusc['simba_size'].mean()
    p_both_mean = a_p_both_solved_deobfusc['probe_size'].mean()
    a_only_deobfusc = dfs.bench_to_cmp_df["deobfusc"].dropna(subset=['simba_size'])
    a_only_deobfusc = a_only_deobfusc[a_only_deobfusc["probe_size"].isna()]
    p_only_deobfusc = dfs.bench_to_cmp_df["deobfusc"].dropna(subset=['probe_size'])
    p_only_deobfusc = p_only_deobfusc[p_only_deobfusc["simba_size"].isna()]

    a_only_mean, a_only_cnt = a_only_deobfusc['simba_size'].mean(), a_only_deobfusc['simba_size'].count()
    p_only_mean, p_only_cnt = p_only_deobfusc['probe_size'].mean(), p_only_deobfusc['probe_size'].count()
    log_write_with_time(f"For Deobfusc, 'simba probe both solved' problems avg size = [{a_both_mean:.1f}, {p_both_mean:.1f}]")
    log_write_with_time(f"simba only avg size = {a_only_mean:.1f} for {a_only_cnt:d}, probe only avg size = {p_only_mean:.1f} for {p_only_cnt:d}")


def show_example_gradient_test(dfs: AllDfs):
    ex05df = dfs.solver_bench_to_df["simba_ex05"]["deobfusc"]
    ex10df = dfs.solver_bench_to_df["simba_ex10"]["deobfusc"]
    ex15df = dfs.solver_bench_to_df["simba_ex15"]["deobfusc"]
    fulldf = dfs.solver_bench_to_df["simba"]["deobfusc"]

    log_write_with_time("Example count 5, 10, 15, 20 ->")
    log_write_with_time("average time {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f} ->".format(
        ex05df["time"].mean(),
        ex10df["time"].mean(),
        ex15df["time"].mean(),
        fulldf["time"].mean(),
    ))
    log_write_with_time("average size {:5.2f}, {:5.2f}, {:5.2f}, {:5.2f} ->".format(
        ex05df["size"].mean(),
        ex10df["size"].mean(),
        ex15df["size"].mean(),
        fulldf["size"].mean(),
    ))


def draw_main_table(dfs: AllDfs, table_out):
    solver_to_all_bench_df = {
        solver: pd.concat([dfs.solver_bench_to_df[solver][bench] for bench in bench_names])
        for solver in solver_names
    }

    show_simba_probe_size_numbers(dfs)
    show_example_gradient_test(dfs)

    # figure 3.(c): main summary table raw data
    # item(solved|time_avg|time_med|size_avg|size_med) |->
    #   solver |->
    #       bench(hd|deobfusc|lobster|crypto) |->
    #           value(count|average|median)
    main_summary: Dict[str, Dict[str, Dict[str, Any]]] = {
        "solved": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["time"].count()
                    for bench in bench_names
                },
                "overall": solver_to_all_bench_df[solver]["time"].count()
            }
            for solver in solver_names
        },
        "time_avg": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["time"].mean() if dfs.solver_bench_to_df[solver][bench]["time"].count() > 0 else numpy.nan
                    for bench in bench_names
                },
                "overall": solver_to_all_bench_df[solver]["time"].mean() if solver_to_all_bench_df[solver]["time"].count() > 0 else numpy.nan
            }
            for solver in solver_names
        },
        "time_med": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["time"].median()
                    for bench in bench_names
                },
                "overall": solver_to_all_bench_df[solver]["time"].median()
            }
            for solver in solver_names
        },
        "size_avg": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["size"].mean() if dfs.solver_bench_to_df[solver][bench]["size"].count() > 0 else numpy.nan
                    for bench in bench_names
                },
                "overall": solver_to_all_bench_df[solver]["size"].mean() if solver_to_all_bench_df[solver]["size"].count() > 0 else numpy.nan
            }
            for solver in solver_names
        },
        "size_med": {
            solver: {
                **{
                    bench: dfs.solver_bench_to_df[solver][bench]["size"].median()
                    for bench in bench_names
                },
                "overall": solver_to_all_bench_df[solver]["size"].median()
            }
            for solver in solver_names
        },
    }

    summary_lines = [
        "{:11s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "".center(12, "-"),
            "".center(24, "-"),
            "".center(20, "-"), "".center(20, "-"), "".center(20, "-"), "".center(20, "-")
        ),
        "{:11s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "Benchmark".center(12, " "),
            "# Solved".center(24, " "),
            "Time(Average)".center(20, " "), "Time(Median)".center(20, " "),
            "Size(Average)".center(20, " "), "Size(Median)".center(20, " ")
        ),
        "{:11s}|| {:10s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|".format(
            "category".center(12, " "),
            "Simba".center(10, " "), "Duet".center(6, " "), "Probe".center(6, " "),
            "S".center(6, " "), "D".center(6, " "), "P".center(6, " "),
            "S".center(6, " "), "D".center(6, " "), "P".center(6, " "),
            "S".center(6, " "), "D".center(6, " "), "P".center(6, " "),
            "S".center(6, " "), "D".center(6, " "), "P".center(6, " "),
        ),
        "{:11s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "".center(12, "-"),
            "".center(24, "-"),
            "".center(20, "-"), "".center(20, "-"), "".center(20, "-"), "".center(20, "-")
        ),
        "{:11s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.0f}|{:>6.0f}|{:>6.0f}|".format(
            "HD".center(12, " "),
            *[main_summary['solved'][solver]['hd'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['hd'] for solver in solver_names],
            *[main_summary['time_med'][solver]['hd'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['hd'] for solver in solver_names],
            *[main_summary['size_med'][solver]['hd'] for solver in solver_names],
        ),
        "{:11s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.0f}|{:>6.0f}|{:>6.0f}|".format(
            "DEOBFUSC".center(12, " "),
            *[main_summary['solved'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['time_med'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['size_med'][solver]['deobfusc'] for solver in solver_names],
        ),
        "{:11s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.0f}|{:>6.0f}|{:>6.0f}|".format(
            "BV-COND".center(12, " "),
            *[main_summary['solved'][solver]['bitvec-cond'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['bitvec-cond'] for solver in solver_names],
            *[main_summary['time_med'][solver]['bitvec-cond'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['bitvec-cond'] for solver in solver_names],
            *[main_summary['size_med'][solver]['bitvec-cond'] for solver in solver_names],
        ),
        "{:11s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.0f}|{:>6.0f}|{:>6.0f}|".format(
            "LOBSTER".center(12, " "),
            *[main_summary['solved'][solver]['lobster'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['lobster'] for solver in solver_names],
            *[main_summary['time_med'][solver]['lobster'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['lobster'] for solver in solver_names],
            *[main_summary['size_med'][solver]['lobster'] for solver in solver_names],
        ),
        "{:11s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.0f}|{:>6.0f}|{:>6.0f}|".format(
            "CRYPTO".center(12, " "),
            *[main_summary['solved'][solver]['crypto'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['crypto'] for solver in solver_names],
            *[main_summary['time_med'][solver]['crypto'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['crypto'] for solver in solver_names],
            *[main_summary['size_med'][solver]['crypto'] for solver in solver_names],
        ),
        "{:11s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "".center(12, "-"),
            "".center(24, "-"),
            "".center(20, "-"), "".center(20, "-"), "".center(20, "-"), "".center(20, "-")
        ),
        "{:11s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}|".format(
            "Overall".center(12, " "),
            *[main_summary['solved'][solver]['overall'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['overall'] for solver in solver_names],
            *[main_summary['time_med'][solver]['overall'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['overall'] for solver in solver_names],
            *[main_summary['size_med'][solver]['overall'] for solver in solver_names],
        ),
        "{:11s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "".center(12, "-"),
            "".center(24, "-"),
            "".center(20, "-"), "".center(20, "-"), "".center(20, "-"), "".center(20, "-")
        ),
    ]

    summary_lines = [line.replace("nan", "  -") for line in summary_lines]

    table_out.write("\n")
    # health check
    required_pairs = health_check_solver_bench(solver_names, no_cond_bench_names)
    if len(required_pairs) > 0:
        table_out.write(f"WARN: incomplete table. you need run {str(required_pairs)}")

    table_out.write("Fig. 3. (c) Statistics for the solving times and solution sizes.\n")
    table_out.write("\n".join(summary_lines))
    table_out.write("\n\n")

    tex_summary_lines = [
        "\\resizebox{\\textwidth}{!}{%",
        "\\small",
        "\\begin{tabular}{c|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r} \\hline",
        "Benchmark  &",
        "  \\multicolumn{3}{c|}{\\# Solved}	&",
        "    \\multicolumn{3}{c|}{Time (Average)} &",
        "      \\multicolumn{3}{c} {Time (Median)} &",
        "        \\multicolumn{3}{|c|}{Size (Average)} &",
        "          \\multicolumn{3}{c} {Size (Median)} \\\\ \\cline{2-16}",
        "category\\! &",
        "  \\textsc{{\\bf S}imba} & \\textsc{{\\bf D}uet} & \\textsc{{\\bf P}robe} &",
        "    \\textsc{{\\bf S}} & \\textsc{{\\bf D}} & \\textsc{{\\bf P}} &",
        "      \\textsc{{\\bf S}} & \\textsc{{\\bf D}} & \\textsc{{\\bf P}} &",
        "        \\textsc{{\\bf S}} & \\textsc{{\\bf D}} & \\textsc{{\\bf P}} &",
        "          \\textsc{{\\bf S}} & \\textsc{{\\bf D}} & \\textsc{{\\bf P}} \\\\",
        "\\hline \\hline",
        "\\textsc{HD} \\! &",
        "  {:d} & {:d} & {:d} &".format(*[main_summary['solved'][solver]['hd'] for solver in solver_names]),
        "    {:.1f} & {:.1f} & {:.1f} &".format(*[main_summary['time_avg'][solver]['hd'] for solver in solver_names]),
        "      {:.1f} & {:.1f} & {:.1f} &".format(*[main_summary['time_med'][solver]['hd'] for solver in solver_names]),
        "        {:.1f} & {:.1f} & {:.1f} &".format(*[main_summary['size_avg'][solver]['hd'] for solver in solver_names]),
        "          {:.0f} & {:.0f} & {:.0f} \\\\[0.3mm]".format(*[main_summary['size_med'][solver]['hd'] for solver in solver_names]),
        "\\textsc{Deobfusc} \\! &",
        "  {:d} & {:d} & {:d} &".format(*[main_summary['solved'][solver]['deobfusc'] for solver in solver_names]),
        "    {:.1f} & {:.1f} & {:.1f} &".format(*[main_summary['time_avg'][solver]['deobfusc'] for solver in solver_names]),
        "      {:.1f} & {:.1f} & {:.1f} &".format(*[main_summary['time_med'][solver]['deobfusc'] for solver in solver_names]),
        "        {:.1f} & {:.1f} & {:.1f} &".format(*[main_summary['size_avg'][solver]['deobfusc'] for solver in solver_names]),
        "          {:.0f} & {:.0f} & {:.0f} \\\\[0.3mm]".format(*[main_summary['size_med'][solver]['deobfusc'] for solver in solver_names]),
        "\\textsc{BitVec-Cond} \\! &",
        "  {:d} & {:d} & - &".format(*[main_summary['solved'][solver]['bitvec-cond'] for solver in ["simba", "duet"]]),
        "    {:.1f} & {:.1f} & - &".format(*[main_summary['time_avg'][solver]['bitvec-cond'] for solver in ["simba", "duet"]]),
        "      {:.1f} & {:.1f} & - &".format(*[main_summary['time_med'][solver]['bitvec-cond'] for solver in ["simba", "duet"]]),
        "        {:.1f} & {:.1f} & - &".format(*[main_summary['size_avg'][solver]['bitvec-cond'] for solver in ["simba", "duet"]]),
        "          {:.0f} & {:.0f} & - \\\\[0.3mm]".format(*[main_summary['size_med'][solver]['bitvec-cond'] for solver in ["simba", "duet"]]),
        "\\textsc{Lobster}\\! &",
        "  {:d} & {:d} & - &".format(*[main_summary['solved'][solver]['lobster'] for solver in ["simba", "duet"]]),
        "    {:.1f} & {:.1f} & - &".format(*[main_summary['time_avg'][solver]['lobster'] for solver in ["simba", "duet"]]),
        "      {:.1f} & {:.1f} & - &".format(*[main_summary['time_med'][solver]['lobster'] for solver in ["simba", "duet"]]),
        "        {:.1f} & {:.1f} & - &".format(*[main_summary['size_avg'][solver]['lobster'] for solver in ["simba", "duet"]]),
        "          {:.0f} & {:.0f} & - \\\\[0.3mm]".format(*[main_summary['size_med'][solver]['lobster'] for solver in ["simba", "duet"]]),
        "\\textsc{Crypto}\\! &",
        "  {:d} & {:d} & - &".format(*[main_summary['solved'][solver]['crypto'] for solver in ["simba", "duet"]]),
        "    {:.1f} & {:.1f} & - &".format(*[main_summary['time_avg'][solver]['crypto'] for solver in ["simba", "duet"]]),
        "      {:.1f} & {:.1f} & - &".format(*[main_summary['time_med'][solver]['crypto'] for solver in ["simba", "duet"]]),
        "        {:.1f} & {:.1f} & - &".format(*[main_summary['size_avg'][solver]['crypto'] for solver in ["simba", "duet"]]),
        "          {:.0f} & {:.0f} & - \\\\[0.3mm]".format(*[main_summary['size_med'][solver]['crypto'] for solver in ["simba", "duet"]]),
        "\\hline",
        "  {\\bf Overall} \\! &",
        "  {{\\bf {:d}}} & {{\\bf {:d}}} & {{\\bf {:d}}} &".format(*[main_summary['solved'][solver]['overall'] for solver in solver_names]),
        "    {{\\bf {:.1f}}} & {{\\bf {:.1f}}} & {{\\bf {:.1f}}} &".format(*[main_summary['time_avg'][solver]['overall'] for solver in solver_names]),
        "      {{\\bf {:.1f}}} & {{\\bf {:.1f}}} & {{\\bf {:.1f}}} &".format(*[main_summary['time_med'][solver]['overall'] for solver in solver_names]),
        "        {{\\bf {:.1f}}} & {{\\bf {:.1f}}} & {{\\bf {:.1f}}} &".format(*[main_summary['size_avg'][solver]['overall'] for solver in solver_names]),
        "          {{\\bf {:.0f}}} & {{\\bf {:.0f}}} & {{\\bf {:.0f}}} \\\\[0.3mm]".format(*[main_summary['size_med'][solver]['overall'] for solver in solver_names]),
        "\\hline",
        "\\end{tabular}}",
    ]

    tex_summary_lines = [line.replace("nan", "-") for line in tex_summary_lines]

    with open(os.path.join(artifact_root_path, "figures", "tbl_summary.tex"), "wt") as f:
        f.write("\n".join(tex_summary_lines))
        log_write_with_time("created figures/tbl_summary.tex: statistics for overall bench & tools")


def draw_all(print_main_table: bool,
             print_detail_table: bool,
             random_subset: Optional[Dict[str, List[str]]],
             cmp_bench_names: List[str],
             print_ablation_table: bool,
             print_plot: bool,
             *,
             all_on: bool,
             table_out):
    dfs = prepare_df()

    if all_on:
        print_main_table = True
        print_detail_table = True
        print_ablation_table = True
        print_plot = True

    for line in solvers.all_result_status_str():
        log_write_with_time(line)

    if print_main_table:
        draw_main_table(dfs, table_out)

    if print_detail_table:
        draw_detail_table(dfs, tbl1_rand_chosen_bench, True, table_out)

    if random_subset is not None:
        draw_detail_table(dfs, random_subset, False, table_out)

    if len(cmp_bench_names) > 0:
        draw_cmp_table(dfs, cmp_bench_names, table_out)

    if print_ablation_table:
        draw_ablation_table(dfs, table_out)

    if print_plot:
        plt.rcParams.update({
            "legend.fontsize": "20",
            "figure.figsize": (9, 6),
            "figure.dpi": 150,
            "axes.labelsize": "20",
            "axes.titlesize": "34",
            "lines.linewidth": "2",
            "xtick.labelsize": "18",
            "ytick.labelsize": "18"
        })

        draw_bar_plots(dfs.solver_bench_to_df, dfs.bench_to_cmp_df)
        draw_cactus_plots(problem_map, dfs.solver_bench_to_df)


def main():
    parser = argparse.ArgumentParser(description='print statistics')

    parser.add_argument('-log', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        dest='log_out',
                        help='test progress log print to... (default: stdout)')
    parser.add_argument('-main_table', action='store_true',
                        help='print Figure 3.(c) (main summary table) in the paper')
    parser.add_argument('-detail_table', action='store_true',
                        help='print Table 1 (detail results of chosen subset) in the paper')
    parser.add_argument('-random_table', action='store_true',
                        help='print table for detail results of randomly chosen subset (not in the paper)')
    parser.add_argument('-cmp_table', type=str, metavar='NAME', nargs='+', required=True,
                        dest='cmp_bench_names',
                        help='list benchmark names to compare solvers'
                             f'({" | ".join(bench_names)})')
    parser.add_argument('-ablation_table', action='store_true',
                        help='print Figure 4.(b) (ablation summary table) in the paper')
    parser.add_argument('-plot', action='store_true',
                        help='draw and store all the plots(Figure 2, Figure 3.(a)(b), Figure 4.(a) in the paper')
    parser.add_argument('-all', action='store_true', default=False,
                        help='activate {main, detail, ablation, plot} flag options to draw all figures and tables in the paper')
    parser.add_argument('-table_out', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        help='print tables to... (default: stdout)')

    args = parser.parse_args()

    common_util.log_out = args.log_out

    random_subset = None
    if args.random_table:
        rand_chosen_hd_problems = random.sample(problem_map["hd"][0], 5)
        rand_chosen_deob_problems = random.sample(problem_map["deobfusc"][0], 5)
        rand_chosen_crypto_problems = random.sample(problem_map["crypto"][0], 5)
        rand_chosen_lobster_problems = random.sample(problem_map["lobster"][0], 5)
        random_subset = {
            "hd": rand_chosen_hd_problems,
            "deobfusc": rand_chosen_deob_problems,
            "crypto": rand_chosen_crypto_problems,
            "lobster": rand_chosen_lobster_problems,
        }

    draw_all(args.main_table, args.detail_table, random_subset, args.cmp_bench_names, args.ablation_table, args.plot,
             all_on=args.all, table_out=args.table_out)


if __name__ == '__main__':
    main()
