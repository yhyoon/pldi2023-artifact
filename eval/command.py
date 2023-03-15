import argparse

import common_util
from common_util import *
import run
import print_stat


def build_clean_dest_dirs(target: str):
    dest_dirs = list()

    if target == "all":
        dest_dirs.append(result_root_path)
    elif target == "abs_synth":
        dest_dirs.append(os.path.join(result_root_path, "abs_synth"))
    elif target == "duet":
        dest_dirs.append(os.path.join(result_root_path, "duet"))
    elif target == "probe":
        dest_dirs.append(os.path.join(result_root_path, "probe"))
    elif target == "deobfusc":
        dest_dirs.append(os.path.join(result_root_path, "abs_synth", "bitvec", "deobfusc"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "bitvec", "deobfusc"))
        dest_dirs.append(os.path.join(result_root_path, "probe", "bitvec", "deobfusc"))
    elif target == "hd":
        dest_dirs.append(os.path.join(result_root_path, "abs_synth", "bitvec", "hd"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "bitvec", "hd"))
        dest_dirs.append(os.path.join(result_root_path, "probe", "bitvec", "hd"))
    elif target == "pbe-bitvec":
        dest_dirs.append(os.path.join(result_root_path, "abs_synth", "pbe-bitvec"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "pbe-bitvec"))
        dest_dirs.append(os.path.join(result_root_path, "probe", "pbe-bitvec"))
    elif target == "crypto":
        dest_dirs.append(os.path.join(result_root_path, "abs_synth", "circuit", "crypto"))
        dest_dirs.append(os.path.join(result_root_path, "duet", "circuit", "crypto"))
    elif target == "lobster":
        dest_dirs.append(os.path.join(result_root_path, "abs_synth", "circuit", "lobster"))
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
    for solver in [*solver_names, *ablation_names]:
        os.makedirs(os.path.join(result_root_path, solver, "bitvec", "deobfusc"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "bitvec", "hd"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "circuit", "crypto"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "circuit", "lobster"), exist_ok=True)
        os.makedirs(os.path.join(result_root_path, solver, "pbe-bitvec"), exist_ok=True)

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
    subparser.add_argument('-cmp_table', type=str, metavar='NAME', nargs='+', default=[],
                           dest='cmp_bench_names',
                           help='list benchmark names to compare solvers'
                                f'({" | ".join(bench_names)})')
    subparser.add_argument('-ablation_table', action='store_true',
                           help='print Figure 4.(b) (ablation summary table) in the paper')
    subparser.add_argument('-plot', action='store_true',
                           help='draw and store all the plots(Figure 2, Figure 3.(a)(b), Figure 4.(a) in the paper')
    subparser.add_argument('-table_out', type=argparse.FileType('w'), metavar='FILE', nargs='?', default=sys.stdout,
                           help='print statistics table to... (default: stdout)')

    # command 4: batch
    subparser = subparsers.add_parser('batch', help='Run Every Solvers to Every Benchmarks and Print Statistics'
                                                    '(WARNING: this command is very very time-consuming)')
    subparser.add_argument('-chosen', action='store_true',
                           help='run chosen subset of benchmarks (Table 1 in paper)')
    subparser.add_argument('-ablation', action='store_true',
                           help='run variation solvers of abs_synth for ablation study too (Figure 4 in paper)')
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
        print_stat.draw_all(args.main_table, args.detail_table, args.cmp_bench_names, args.ablation_table, args.plot, args.table_out)
    elif args.command == 'batch':
        for bench in ["crypto", "lobster", "hd", "deobfusc", "pbe-bitvec"]:
            for solver in solver_names:
                log_write_with_time(f"===== BATCH: run {solver} on {bench} =====")
                run.run_test(solver, bench, args.chosen, args.overwrite, args.timeout, args.thread_count)
            if args.ablation:
                for solver in ablation_names:
                    log_write_with_time(f"===== BATCH: run {solver} on {bench} =====")
                    run.run_test(solver, bench, args.chosen, args.overwrite, args.timeout, args.thread_count)
        print_stat.draw_all(not args.chosen and not args.ablation, args.chosen, [], args.ablation, not args.chosen, args.table_out)
    elif args.command == 'aggregation':
        with open(args.csv_out, "wt") as fout:
            def read_and_write(f, index):
                with open(f, "rt") as fin:
                    for line in fin.readlines():
                        if len(line.strip()) == 0:
                            pass
                        else:
                            solver_name, problem, sol_type, sol_time, sol_size, sol = print_stat.parse_csv_result(line)
                            if sol_type == "success":
                                fout.write(f"{solver_name},{problem},{sol_type},{sol_time},{sol_size},{sol}\n")
                            elif sol_time is not None:
                                fout.write(f"{solver_name},{problem},{sol_type},{sol_time},n/a,n/a\n")
                            else:
                                fout.write(f"{solver_name},{problem},{sol_type},n/a,n/a,n/a\n")

            fout.write("solver,problem,sol_type,time,size,sol\n")
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
