import argparse
import random

import common_util
from common_util import *
import run
import print_stat


def build_clean_dest_dirs(target: str):
    dest_dirs = list()

    if target == "all":
        dest_dirs.append(result_root_path)
    elif target == "simba":
        dest_dirs.append(os.path.join(result_root_path, "simba"))
    elif target == "duet":
        dest_dirs.append(os.path.join(result_root_path, "duet"))
    elif target == "probe":
        dest_dirs.append(os.path.join(result_root_path, "probe"))
    elif target == "deobfusc":
        dest_dirs.append(os.path.join(result_root_path, "simba", "bitvec", "deobfusc"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "bitvec", "deobfusc"))
        dest_dirs.append(os.path.join(result_root_path, "probe", "bitvec", "deobfusc"))
    elif target == "hd":
        dest_dirs.append(os.path.join(result_root_path, "simba", "bitvec", "hd"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "bitvec", "hd"))
        dest_dirs.append(os.path.join(result_root_path, "probe", "bitvec", "hd"))
    elif target == "bitvec-cond":
        dest_dirs.append(os.path.join(result_root_path, "simba", "bitvec-cond"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "bitvec-cond"))
        dest_dirs.append(os.path.join(result_root_path, "probe", "bitvec-cond"))
    elif target == "crypto":
        dest_dirs.append(os.path.join(result_root_path, "simba", "circuit", "crypto"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "circuit", "crypto"))
    elif target == "lobster":
        dest_dirs.append(os.path.join(result_root_path, "simba", "circuit", "lobster"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "circuit", "lobster"))
    else:
        print(f"unknown clean target {target}", file=sys.stderr)

    return dest_dirs


def do_clean(target, yes):
    dest_dirs = build_clean_dest_dirs(target)
    dest_files = list()

    for dest_dir in dest_dirs:
        dest_files_in_dir = list()
        traverse(dest_dir,
                 lambda f: os.path.split(f)[1].endswith(".result.txt"),
                 lambda x, index: dest_files_in_dir.append(x))
        if len(dest_files_in_dir) > 0:
            print(f"Going to delete {len(dest_files_in_dir)} results in {dest_dir}")

        dest_files.extend(dest_files_in_dir)

    if len(dest_files) > 0:
        print(f"Going to delete {len(dest_files)} results in total")

        ok = False
        if yes:
            ok = True
        else:
            answer = input("Agree?[y/N]")
            if answer == 'y' or answer == 'Y':
                ok = True

        if ok:
            # do actual clean
            cnt_index = 1
            for dest_file in dest_files:
                os.remove(dest_file)
                print(f"[{cnt_index}]Deleted {dest_file}")
                cnt_index += 1
        else:
            print("Canceled")
    else:
        print("Nothing to delete")


def prepare_result_dirs():
    for solver in [*solver_names, *ablation_names, *ex_cut_names]:
        os.makedirs(os.path.join(result_root_path, solver, "bitvec", "deobfusc"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "bitvec", "hd"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "circuit", "crypto"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "circuit", "lobster"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "bitvec-cond"), exist_ok=True)

    os.makedirs(os.path.join(artifact_root_path, "figures"), exist_ok=True)


def main():
    prepare_result_dirs()

    parser = argparse.ArgumentParser(description='artifact commands')
    parser.add_argument('-log', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                        dest='log_out',
                        help='test progress log print to... (default: stdout)')

    subparsers = parser.add_subparsers(dest='command')

    # command 1: clean
    subparser = subparsers.add_parser('clean', help='Clean All Result Files (BE CAREFUL: cannot undo)')
    subparser.add_argument('target', type=str, metavar='TARGET',
                           help=f'all | ({"|".join(solver_names)}) | ({"|".join(bench_names)})')
    subparser.add_argument('--yes', action='store_true',
                           help='do clean without asking(BE CAREFUL! we strongly recommend to do back-up before clean)')

    # command 2: run
    subparser = subparsers.add_parser('run', help='Run Solvers on Benchmarks')
    subparser.add_argument('-solvers', type=str, metavar='NAME', nargs='+', required=True,
                           dest='solver_list',
                           help='list solvers to be evaluated'
                                f'({" | ".join([*solver_names, *ablation_names])})')
    subparser.add_argument('-benches', type=str, metavar='NAME', nargs='+', required=True,
                           dest='bench_list',
                           help='benchmarks to be evaluated'
                                f'({" | ".join(bench_names)})')
    subparser.add_argument('-chosen', action='store_true',
                           help='run chosen subset of benchmarks (Table 1 in paper)')
    subparser.add_argument('-p', type=int, metavar='NUM', nargs='?', default=1,
                           dest='thread_count',
                           help='run in parallel process using NUM threads (default: 1)')
    subparser.add_argument('-timeout', type=int, metavar='NUM', nargs='?', default=3600,
                           dest='timeout',
                           help='timeout for each problem in seconds (default: 3600)')
    subparser.add_argument('-overwrite', action='store_true',
                           help='force run solver even if there already exists result file for the benchmark'
                                '(default: skip if result exists)')

    # command 3: stat
    subparser = subparsers.add_parser('stat', help='Print Statistics of Run Result')
    subparser.add_argument('-main_table', action='store_true',
                           help='print Figure 3.(c) (main summary table) in the paper')
    subparser.add_argument('-detail_table', action='store_true',
                           help='print Table 1 (detail results of chosen subset) in the paper')
    subparser.add_argument('-random_table', action='store_true',
                           help='print table for detail results of randomly chosen subset (not in the paper)')
    subparser.add_argument('-cmp_table', type=str, metavar='NAME', nargs='+', default=[],
                           dest='cmp_bench_names',
                           help='list benchmark names to compare solvers'
                                f'({" | ".join(bench_names)})')
    subparser.add_argument('-ablation_table', action='store_true',
                           help='print Figure 4.(b) (ablation summary table) in the paper')
    subparser.add_argument('-plot', action='store_true',
                           help='draw and store all the plots(Figure 2, Figure 3.(a)(b), Figure 4.(a) in the paper')
    subparser.add_argument('-all', action='store_true', default=False,
                           help='activate all flag options to draw all figures and tables')
    subparser.add_argument('-table_out', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                           help='print statistics table to... (default: stdout)')

    # command 4: batch
    subparser = subparsers.add_parser('batch', help='Run Every Solvers to Every Benchmarks and Print Statistics'
                                                    '(WARNING: this command is very very time-consuming)')
    subparser.add_argument('-chosen', action='store_true',
                           help='run chosen subset of benchmarks (Table 1 in paper), cannot be used with -random')
    subparser.add_argument('-random', action='store_true',
                           help='run random subset of benchmarks (similar to Table 1 in paper, but different on each run), cannot be used with -chosen')
    subparser.add_argument('-ablation', action='store_true',
                           help='run variation solvers of simba for ablation study too (Figure 4 in paper)')
    subparser.add_argument('-p', type=int, metavar='NUM', nargs='?', default=1,
                           dest='thread_count',
                           help='run in parallel process using NUM threads (default: 1)')
    subparser.add_argument('-timeout', type=int, metavar='NUM', nargs='?', default=3600,
                           dest='timeout',
                           help='timeout for each problem in seconds (default: 3600)')
    subparser.add_argument('-overwrite', action='store_true',
                           help='force run solver even if there already exists result file for the benchmark'
                                '(default: skip existing result)')
    subparser.add_argument('-table_out', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                           help='print statistics table to... (default: stdout)')

    # command 5: aggregation
    subparser = subparsers.add_parser('aggregation',
                                      help='Put all results into single csv file')
    subparser.add_argument('-csv_out', type=str, metavar='FILE', nargs='?', default="all_result.csv",
                           help='store aggregated csv file to... (default: all_result.csv)')

    args = parser.parse_args()

    if args.log_out is not None:
        common_util.log_out = args.log_out

    if args.command == 'clean':
        do_clean(args.target, args.yes)
    elif args.command == 'run':
        for solver in args.solver_list:
            for bench in args.bench_list:
                log_write_with_time(f"===== run {solver} on {bench} =====")
                run.run_test(solver, bench, args.chosen, args.overwrite, args.timeout, args.thread_count)
    elif args.command == 'stat':
        random_subset = None
        if args.random_table:
            rand_chosen_hd_problems = random.sample(problem_map["hd"][0], 5)
            rand_chosen_deob_problems = random.sample(problem_map["deobfusc"][0], 5)
            rand_chosen_crypto_problems = random.sample(problem_map["crypto"][0], 5)
            rand_chosen_lobster_problems = random.sample(problem_map["lobster"][0], 5)
            rand_chosen_cond_problems = random.sample(problem_map["bitvec-cond"][0], 5)
            random_subset = {
                "hd": rand_chosen_hd_problems,
                "deobfusc": rand_chosen_deob_problems,
                "crypto": rand_chosen_crypto_problems,
                "lobster": rand_chosen_lobster_problems,
                "bitvec-cond": rand_chosen_cond_problems,
            }

        print_stat.draw_all(args.main_table, args.detail_table, random_subset, args.cmp_bench_names, args.ablation_table, args.plot,
                            all_on=args.all,
                            table_out=args.table_out)
    elif args.command == 'batch':
        if args.chosen and args.random:
            raise Exception("Cannot use -chosen and -random at the same time")

        bench_subset: Optional[Dict[str, List[str]]] = None
        if args.chosen:
            bench_subset = tbl1_rand_chosen_bench
        elif args.random:
            rand_chosen_hd_problems = random.sample(problem_map["hd"][0], 5)
            rand_chosen_deob_problems = random.sample(problem_map["deobfusc"][0], 5)
            rand_chosen_crypto_problems = random.sample(problem_map["crypto"][0], 5)
            rand_chosen_lobster_problems = random.sample(problem_map["lobster"][0], 5)
            rand_chosen_cond_problems = random.sample(problem_map["bitvec-cond"][0], 5)
            bench_subset = {
                "hd": rand_chosen_hd_problems,
                "deobfusc": rand_chosen_deob_problems,
                "crypto": rand_chosen_crypto_problems,
                "lobster": rand_chosen_lobster_problems,
                "bitvec-cond": rand_chosen_cond_problems,
            }

        for bench in ["crypto", "lobster", "hd", "deobfusc", "bitvec-cond"]:
            for solver in solver_names:
                log_write_with_time(f"===== BATCH: run {solver} on {bench} =====")
                run.run_test(solver, bench, bench_subset, args.overwrite, args.timeout, args.thread_count)
            if args.ablation:
                for solver in ablation_names:
                    log_write_with_time(f"===== BATCH: run {solver} on {bench} =====")
                    run.run_test(solver, bench, bench_subset, args.overwrite, args.timeout, args.thread_count)
        print_stat.draw_all(not args.chosen and not args.ablation, args.chosen, bench_subset if args.random else None, [], args.ablation, not args.chosen,
                            all_on=False,
                            table_out=args.table_out)
    elif args.command == 'aggregation':
        with open(args.csv_out, "wt") as fout:
            def read_and_write(f, index):
                with open(f, "rt") as fin:
                    for line in fin.readlines():
                        if len(line.strip()) == 0:
                            pass
                        else:
                            solver_name, problem, sol_type, sol_time, sol_size, sol = print_stat.parse_csv_result(line)
                            bench_name = problem_bench_map[problem]
                            if sol_type == "success":
                                fout.write(f"{solver_name},{bench_name},{problem},{sol_type},{sol_time},{sol_size},{sol}\n")
                            elif sol_time is not None:
                                fout.write(f"{solver_name},{bench_name},{problem},{sol_type},{sol_time},n/a,n/a\n")
                            else:
                                fout.write(f"{solver_name},{bench_name},{problem},{sol_type},n/a,n/a,n/a\n")

            fout.write("solver,bench,problem,sol_type,time,size,sol\n")
            traverse(result_root_path,
                     is_target=lambda path: os.path.split(path)[1].endswith(".result.txt"),
                     target_handler=read_and_write)
    elif args.command is None:
        print(f"Command Name is Required (run | stat | batch | clean)", file=sys.stderr)
    else:
        print(f"Not Supported Command {args.command}", file=sys.stderr)


if __name__ == '__main__':
    main()


# clear
# run blah blah
# stat blah blah
