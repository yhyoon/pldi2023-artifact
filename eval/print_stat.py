from typing import Optional, Tuple, List, Dict, FrozenSet

import argparse
import matplotlib.pyplot as plt
import numpy
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

    for b in bench_names:
        traverse(bench_name_to_dir[b],
                 lambda f: f.endswith(".sl"),
                 lambda f, index: add_to(b, f)
                 )

    return {b: (problem_list_map[b],
                frozenset(problem_list_map[b]),
                pd.DataFrame({"problem": problem_list_map[b]}).set_index('problem')
                )
            for b in bench_names}, problem_map


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


def read_all(problem_list: Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]],
             problem_bench_map: Dict[str, str]) -> pd.DataFrame:
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


def build_time_cmp_table(problem_df, abs_df, duet_df, probe_df=None) -> pd.DataFrame:
    accum_df: pd.DataFrame = problem_df.join(abs_df.rename(columns={"time": "abs"})["abs"])
    accum_df: pd.DataFrame = accum_df.join(duet_df.rename(columns={"time": "duet"})["duet"])

    if probe_df is not None:
        accum_df: pd.DataFrame = accum_df.join(probe_df.rename(columns={"time": "probe"})["probe"])
        accum_df["win"] = accum_df[["abs", "duet", "probe"]].idxmin(axis=1)
    else:
        accum_df["win"] = accum_df[["abs", "duet"]].idxmin(axis=1)

    return accum_df.sort_index()


# draw figures: cactus
def draw_cactus(bench_name: str, file_name: str, all_problem_count, tds, *, mark_every=None, xtick_step=None):
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
    figure.savefig(os.path.join(artifact_root_path, "figures", f"cactus_{file_name}.png"), transparent=True)
    log_write_with_time(f"created cactus_{file_name}.png")


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
                        ax.text(i, accum_cnt + 40, s=str(cnt),
                                fontsize=18, weight='heavy', ha='center', va='top')
                    else:
                        ax.text(i, accum_cnt + 20, s=str(cnt),
                                fontsize=18, weight='heavy', ha='center', va='top')
                else:
                    ax.text(i, (accum_cnt - cnt) + cnt // 2, s=str(cnt),
                            fontsize=18, weight='heavy', ha='center', va='center')
        else:
            ax.bar_label(cur_br, fontsize=18, weight='heavy', label_type='center')
        prev_smalls = next_smalls

    for i, sum_cnt in enumerate(sum_cnts):
        ax.text(i, max(sum_cnts) + 50, s=str(sum_cnt),
                fontsize=16, weight='heavy', ha='center',
                bbox={'boxstyle': 'square', 'facecolor': 'white', 'edgecolor': 'black'})
    figure.legend(loc='upper center', ncol=2, frameon=False)
    figure.savefig(os.path.join(artifact_root_path, "figures", f"bar_{kind}.png"), transparent=True)
    log_write_with_time(f"created bar_{kind}.png")


# figure 2: overall cactus plots
def draw_plots(problem_list: Dict[str, Tuple[List[str], FrozenSet[str], pd.DataFrame]],
               solver_bench_to_df: Dict[str, Dict[str, pd.DataFrame]]):
    draw_cactus("Lobster", "lobster", len(problem_list["lobster"][0]), [
        {'time_df': solver_bench_to_df["duet"]["lobster"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["abs_synth"]["lobster"]["time"].sort_values(ignore_index=True),
         'label': "ABSSYNTH", 'color': 'b', 'marker': 'o'},
    ], xtick_step=41)

    draw_cactus("Crypto", "crypto", len(problem_list["crypto"][0]), [
        {'time_df': solver_bench_to_df["duet"]["crypto"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["abs_synth"]["crypto"]["time"].sort_values(ignore_index=True),
         'label': "ABSSYNTH", 'color': 'b', 'marker': 'o'},
    ])

    draw_cactus("Hacker's Delight", "hd", len(problem_list["hd"][0]), [
        {'time_df': solver_bench_to_df["duet"]["hd"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["probe"]["hd"]["time"].sort_values(ignore_index=True),
         'label': "PROBE", 'color': 'r', 'marker': 'v'},
        {'time_df': solver_bench_to_df["abs_synth"]["hd"]["time"].sort_values(ignore_index=True),
         'label': "ABSSYNTH", 'color': 'b', 'marker': 'o'},
    ], xtick_step=4)

    draw_cactus("Deobfuscation", "deob", len(problem_list["deobfusc"][0]), [
        {'time_df': solver_bench_to_df["duet"]["deobfusc"]["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': solver_bench_to_df["probe"]["deobfusc"]["time"].sort_values(ignore_index=True),
         'label': "PROBE", 'color': 'r', 'marker': 'v'},
        {'time_df': solver_bench_to_df["abs_synth"]["deobfusc"]["time"].sort_values(ignore_index=True),
         'label': "ABSSYNTH", 'color': 'b', 'marker': 'o'},
    ], xtick_step=50)

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
                solver_bench_to_df["abs_synth"]["hd"],
                solver_bench_to_df["abs_synth"]["deobfusc"]
            ])["time"].sort_values(ignore_index=True),
         'label': "ABSSYNTH", 'color': 'b', 'marker': 'o'}
    ])

    draw_cactus("CIRCUIT (LOBSTER+CRYPTO)", "bool", len([*problem_list["lobster"][0], *problem_list["crypto"][0]]), [
        {'time_df': pd.concat(
            [
                solver_bench_to_df["duet"]["crypto"],
                solver_bench_to_df["duet"]["lobster"]
            ])["time"].sort_values(ignore_index=True),
         'label': "DUET", 'color': 'g', 'marker': '^'},
        {'time_df': pd.concat(
            [
                solver_bench_to_df["abs_synth"]["crypto"],
                solver_bench_to_df["abs_synth"]["lobster"]
            ])["time"].sort_values(ignore_index=True),
         'label': "ABSSYNTH", 'color': 'b', 'marker': 'o'},
    ])


# figure 3.(a), 3.(b): solved count and fastest count
def draw_bars(solver_bench_to_df: Dict[str, Dict[str, pd.DataFrame]],
              bench_cmp_map: Dict[str, pd.DataFrame]):
    bar_colors = ['gold', '#96b4fa']

    # stacked bar1 - bitvec cnt
    draw_stack_bar("bv_cnt", "# Solved Benchmarks", ["ABSSYNTH", "DUET", "PROBE"], ["DEOBUSC", "HD"], bar_colors,  [
        [solver_bench_to_df[solver][bench]["time"].count() for solver in solver_names]
        for bench in ["deobfusc", "hd"]
    ])

    # stacked bar2 - circuit cnt
    draw_stack_bar("circuit_cnt", "# Solved Benchmarks", ["ABSSYNTH", "DUET"], ["LOBSTER", "CRYPTO"], bar_colors, [
        [solver_bench_to_df[solver][bench]["time"].count() for solver in ["abs_synth", "duet"]]
        for bench in ["lobster", "crypto"]
    ])

    # stacked bar3 - bitvec fastest
    hd_win = bench_cmp_map["hd"]["win"].value_counts()
    deob_win = bench_cmp_map["deobfusc"]["win"].value_counts()
    draw_stack_bar("bv_fast", "# Fastest Solved Benchmarks", ["ABSSYNTH", "DUET", "PROBE"], ["DEOBFUSC", "HD"], bar_colors, [
        [deob_win.get("abs", 0), deob_win.get("duet", 0), deob_win.get("probe", 0)],
        [hd_win.get("abs", 0), hd_win.get("duet", 0), hd_win.get("probe", 0)],
    ])

    # stacked bar4 - circuit fastest
    lobster_win = bench_cmp_map["lobster"]["win"].value_counts()
    crypto_win = bench_cmp_map["crypto"]["win"].value_counts()
    draw_stack_bar("circuit_fast", "# Fastest Solved Benchmarks", ["ABSSYNTH", "DUET"], ["LOBSTER", "CRYPTO"], bar_colors, [
        [lobster_win.get("abs", 0), lobster_win.get("duet", 0)],
        [crypto_win.get("abs", 0), crypto_win.get("duet", 0)],
    ])


def draw_tex_tables(table_out, main_summary, table_1):
    stat_summary = ''.join([f"""
\\resizebox{{\\textwidth}}{{!}}{{%
\\small
\\begin{{tabular}}{{c|r|r|r|r|r|r|r|r|r|r|r|r|r|r|r}} \\hline
Benchmark  &
    \\multicolumn{{3}}{{c|}}{{\\# Solved}}	&
        \\multicolumn{{3}}{{c|}}{{Time (Average)}} &
            \\multicolumn{{3}}{{c}} {{Time (Median)}} &
                \\multicolumn{{3}}{{|c|}}{{Size (Average)}} &
                    \\multicolumn{{3}}{{c}} {{Size (Median)}} \\\\ \cline{{2-16}}
category\! &
    \\textsc{{{{\\bf A}}bsSynth}} & \\textsc{{{{\\bf D}}uet}} & \\textsc{{{{\\bf P}}robe}} &
        \\textsc{{{{\\bf A}}}} & \\textsc{{{{\\bf D}}}} & \\textsc{{{{\\bf P}}}} &
            \\textsc{{{{\\bf A}}}} & \\textsc{{{{\\bf D}}}} & \\textsc{{{{\\bf P}}}} &
                \\textsc{{{{\\bf A}}}} & \\textsc{{{{\\bf D}}}} & \\textsc{{{{\\bf P}}}} &
                    \\textsc{{{{\\bf A}}}} & \\textsc{{{{\\bf D}}}} & \\textsc{{{{\\bf P}}}} \\\\
\hline \hline
\\textsc{{HD}} \\! &\n"""
    f"    {' & '.join([str(main_summary['solved'][solver]['hd']) for solver in solver_names])} &\n"
    f"        {' & '.join(['{:.1f}'.format(main_summary['time_avg'][solver]['hd']) for solver in solver_names])} &\n"
    f"            {' & '.join(['{:.1f}'.format(main_summary['time_med'][solver]['hd'].item()) for solver in solver_names])} &\n"
    f"                {' & '.join(['{:.1f}'.format(main_summary['size_avg'][solver]['hd']) for solver in solver_names])} &\n"
    f"                    {' & '.join(['{:.0f}'.format(main_summary['size_med'][solver]['hd'].item()) for solver in solver_names])} &\n"
    "\\\\[0.3mm]\n"
    "\\textsc{Deobfusc} \! &\n"
    f"    {' & '.join([str(main_summary['solved'][solver]['deobfusc']) for solver in solver_names])} &\n"
    f"        {' & '.join(['{:.1f}'.format(main_summary['time_avg'][solver]['deobfusc']) for solver in solver_names])} &\n"
    f"            {' & '.join(['{:.1f}'.format(main_summary['time_med'][solver]['deobfusc'].item()) for solver in solver_names])} &\n"
    f"                {' & '.join(['{:.1f}'.format(main_summary['size_avg'][solver]['deobfusc']) for solver in solver_names])} &\n"
    f"                    {' & '.join(['{:.0f}'.format(main_summary['size_med'][solver]['deobfusc'].item()) for solver in solver_names])} &\n"
    "\\\\[0.3mm]\n"
    "\\textsc{Lobster}\! &\n"
    f"    {' & '.join([*[str(main_summary['solved'][solver]['lobster']) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"        {' & '.join([*['{:.1f}'.format(main_summary['time_avg'][solver]['lobster']) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"            {' & '.join([*['{:.1f}'.format(main_summary['time_med'][solver]['lobster'].item()) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"                {' & '.join([*['{:.1f}'.format(main_summary['size_avg'][solver]['lobster']) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"                    {' & '.join([*['{:.0f}'.format(main_summary['size_med'][solver]['lobster'].item()) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    "\\\\[0.3mm]\n"
    "\\textsc{Crypto}\! &\n"
    f"    {' & '.join([*[str(main_summary['solved'][solver]['crypto']) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"        {' & '.join([*['{:.1f}'.format(main_summary['time_avg'][solver]['crypto']) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"            {' & '.join([*['{:.1f}'.format(main_summary['time_med'][solver]['crypto'].item()) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"                {' & '.join([*['{:.1f}'.format(main_summary['size_avg'][solver]['crypto']) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    f"                    {' & '.join([*['{:.0f}'.format(main_summary['size_med'][solver]['crypto'].item()) for solver in ['abs_synth', 'duet']], '-'])} &\n"
    "\\\\[0.3mm]\n"
    "\\hline\n"
    "{\\bf Overall} \! &\n"
    f"    {{\\bf {main_summary['solved']['abs_synth']['overall']}}} &\n"
    f"    {{\\bf {main_summary['solved']['duet']['overall']}}} &\n"
    f"    {{\\bf {main_summary['solved']['probe']['overall']}}} &\n"
    f"        {{\\bf {'{:.1f}'.format(main_summary['time_avg']['abs_synth']['overall'])}}} &\n"
    f"        {{\\bf {'{:.1f}'.format(main_summary['time_avg']['duet']['overall'])}}} &\n"
    f"        {{\\bf {'{:.1f}'.format(main_summary['time_avg']['probe']['overall'])}}} &\n"
    f"            {{\\bf {'{:.1f}'.format(main_summary['time_med']['abs_synth']['overall'].item())}}} &\n"
    f"            {{\\bf {'{:.1f}'.format(main_summary['time_med']['duet']['overall'].item())}}} &\n"
    f"            {{\\bf {'{:.1f}'.format(main_summary['time_med']['probe']['overall'].item())}}} &\n"
    f"                {{\\bf {'{:.1f}'.format(main_summary['size_avg']['abs_synth']['overall'])}}} &\n"
    f"                {{\\bf {'{:.1f}'.format(main_summary['size_avg']['duet']['overall'])}}} &\n"
    f"                {{\\bf {'{:.1f}'.format(main_summary['size_avg']['probe']['overall'])}}} &\n"
    f"                    {{\\bf {'{:.0f}'.format(main_summary['size_med']['abs_synth']['overall'].item())}}} &\n"
    f"                    {{\\bf {'{:.0f}'.format(main_summary['size_med']['duet']['overall'].item())}}} &\n"
    f"                    {{\\bf {'{:.0f}'.format(main_summary['size_med']['probe']['overall'].item())}}} &\n"
    "\\hline\n"
    "\\end{tabular}}\n"])

    table_out.write(stat_summary)


def draw_txt_tables(table_out, main_summary, table_1):
    summary_lines = [
        "{:12s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "Benchmark".center(12, " "),
            "# Solved".center(24, " "),
            "Time(Average)".center(20, " "), "Time(Median)".center(20, " "),
            "Size(Average)".center(20, " "), "Size(Median)".center(20, " ")
        ),
        "{:12s}|| {:10s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}| {:6s}|{:6s}|{:6s}|".format(
            "category".center(12, " "),
            "AbsSynth".center(10, " "), "Duet".center(6, " "), "Probe".center(6, " "),
            "A".center(6, " "), "D".center(6, " "), "P".center(6, " "),
            "A".center(6, " "), "D".center(6, " "), "P".center(6, " "),
            "A".center(6, " "), "D".center(6, " "), "P".center(6, " "),
            "A".center(6, " "), "D".center(6, " "), "P".center(6, " "),
        ),
        "{:12s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "".center(12, "-"),
            "".center(24, "-"),
            "".center(20, "-"), "".center(20, "-"), "".center(20, "-"), "".center(20, "-")
        ),
        "{:12s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}|".format(
            "HD".center(12, " "),
            *[main_summary['solved'][solver]['hd'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['hd'] for solver in solver_names],
            *[main_summary['time_med'][solver]['hd'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['hd'] for solver in solver_names],
            *[main_summary['size_med'][solver]['hd'] for solver in solver_names],
        ),
        "{:12s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}|".format(
            "DEOBFUSC".center(12, " "),
            *[main_summary['solved'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['time_med'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['deobfusc'] for solver in solver_names],
            *[main_summary['size_med'][solver]['deobfusc'] for solver in solver_names],
        ),
        "{:12s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}|".format(
            "LOBSTER".center(12, " "),
            *[main_summary['solved'][solver]['lobster'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['lobster'] for solver in solver_names],
            *[main_summary['time_med'][solver]['lobster'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['lobster'] for solver in solver_names],
            *[main_summary['size_med'][solver]['lobster'] for solver in solver_names],
        ),
        "{:12s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}|".format(
            "CRYPTO".center(12, " "),
            *[main_summary['solved'][solver]['crypto'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['crypto'] for solver in solver_names],
            *[main_summary['time_med'][solver]['crypto'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['crypto'] for solver in solver_names],
            *[main_summary['size_med'][solver]['crypto'] for solver in solver_names],
        ),
        "{:12s}|| {:24s}| {:20s}| {:20s}| {:20s}| {:20s}|".format(
            "".center(12, "-"),
            "".center(24, "-"),
            "".center(20, "-"), "".center(20, "-"), "".center(20, "-"), "".center(20, "-")
        ),
        "{:12s}|| {:>10d}|{:>6d}|{:>6d}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}| {:>6.1f}|{:>6.1f}|{:>6.1f}|".format(
            "Overall".center(12, " "),
            *[main_summary['solved'][solver]['overall'] for solver in solver_names],
            *[main_summary['time_avg'][solver]['overall'] for solver in solver_names],
            *[main_summary['time_med'][solver]['overall'] for solver in solver_names],
            *[main_summary['size_avg'][solver]['overall'] for solver in solver_names],
            *[main_summary['size_med'][solver]['overall'] for solver in solver_names],
        )
    ]

    table_out.write("\n".join(summary_lines))
    table_out.write("\n")

    detail_lines = [

    ]


def draw_all(table_format: str, table_out):
    problem_list, problem_bench_map = gen_problems()

    main_df = read_all(problem_list, problem_bench_map)

    # table of each solver
    solver_to_df: Dict[str, pd.DataFrame] = {
        solver: main_df[main_df["solver"] == solver].set_index("problem").sort_index()
        for solver in solver_names
    }
    abs_synth_df = solver_to_df["abs_synth"]
    duet_df = solver_to_df["duet"]
    probe_df = solver_to_df["probe"]

    solver_bench_to_df: Dict[str, Dict[str, pd.DataFrame]] = {
        solver: {
            bench: solver_to_df[solver][solver_to_df[solver]["bench"] == bench]
            for bench in ["deobfusc", "hd", "lobster", "crypto", "pbe-bitvec"]
        }
        for solver in ["abs_synth", "duet", "probe"]
    }

    plt.rcParams.update({
        "legend.fontsize": "16",
        "figure.figsize": (9, 6),
        "figure.dpi": 150,
        "axes.labelsize": "16",
        "axes.titlesize": "30",
        "lines.linewidth": "2",
        "xtick.labelsize": "14",
        "ytick.labelsize": "14"
    })

    def solver_problem_detail(solver: str, problem: str, col_name: str):
        df = solver_bench_to_df[solver][problem_bench_map[problem]]
        try:
            return df.loc[problem][col_name]
        except KeyError:
            return numpy.nan

    # comparison table for counting best solver
    hd_cmp_df = build_time_cmp_table(problem_list["hd"][2], abs_synth_df, duet_df, probe_df)
    deobfusc_cmp_df = build_time_cmp_table(problem_list["deobfusc"][2], abs_synth_df, duet_df, probe_df)
    lobster_cmp_df = build_time_cmp_table(problem_list["lobster"][2], abs_synth_df, duet_df)
    crypto_cmp_df = build_time_cmp_table(problem_list["crypto"][2], abs_synth_df, duet_df)
    pbe_bv_cmp_df = build_time_cmp_table(problem_list["pbe-bitvec"][2], abs_synth_df, duet_df, probe_df)
    bench_cmp_map: Dict[str, pd.DataFrame] = {
        "hd": hd_cmp_df,
        "deobfusc": deobfusc_cmp_df,
        "lobster": lobster_cmp_df,
        "crypto": crypto_cmp_df,
        "pbe-bitvec": pbe_bv_cmp_df,
    }

    # figure 3.(c): main summary table: item(solved|time_avg|time_med|size_avg|size_med) |-> solver |-> bench |-> value
    main_summary = {
        "solved": {
            solver: {
                **{
                    bench: solver_bench_to_df[solver][bench]["time"].count()
                    for bench in bench_names
                },
                "overall": solver_to_df[solver]["time"].count()
            }
            for solver in solver_names
        },
        "time_avg": {
            solver: {
                **{
                    bench: solver_bench_to_df[solver][bench]["time"].mean()
                    for bench in bench_names
                },
                "overall": solver_to_df[solver]["time"].mean()
            }
            for solver in solver_names
        },
        "time_med": {
            solver: {
                **{
                    bench: solver_bench_to_df[solver][bench]["time"].median()
                    for bench in bench_names
                },
                "overall": solver_to_df[solver]["time"].median()
            }
            for solver in solver_names
        },
        "size_avg": {
            solver: {
                **{
                    bench: solver_bench_to_df[solver][bench]["size"].mean()
                    for bench in bench_names
                },
                "overall": solver_to_df[solver]["size"].mean()
            }
            for solver in solver_names
        },
        "size_med": {
            solver: {
                **{
                    bench: solver_bench_to_df[solver][bench]["size"].median()
                    for bench in bench_names
                },
                "overall": solver_to_df[solver]["size"].median()
            }
            for solver in solver_names
        },
    }

    # table 1: randomly chosen detail table: solver |-> bench |-> time, size
    table_1 = {
        solver: {
            problem: {
                "time": solver_problem_detail(solver, problem, "time"),
                "size": solver_problem_detail(solver, problem, "size"),
            }
            for problem in [
                *tbl1_rand_chosen_hd_problems,
                *tbl1_rand_chosen_deob_problems,
                *tbl1_rand_chosen_lobster_problems,
                *tbl1_rand_chosen_crypto_problems
            ]
        }
        for solver in solver_names
    }

    draw_txt_tables(table_out, main_summary, table_1)
    # if table_format == "tex":
    #     draw_tex_tables(table_out, main_summary, table_1)
    # else:
    #     draw_txt_tables(table_out, main_summary, table_1)
    draw_bars(solver_bench_to_df, bench_cmp_map)
    draw_plots(problem_list, solver_bench_to_df)


def main():
    parser = argparse.ArgumentParser(description='print statistics')

    parser.add_argument('-log', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        dest='log_out',
                        help='test progress log print to... (default: stdout)')
    parser.add_argument('-table_format', type=str, metavar='FORMAT', default="txt",
                        help='statistics table format (txt | tex) (default: txt)')
    parser.add_argument('-table_out', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        help='print statistics table to... (default: stdout)')

    args = parser.parse_args()

    common_util.log_out = args.log_out

    draw_all(args.table_format, args.table_out)


if __name__ == '__main__':
    main()
