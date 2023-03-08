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
                                f'({" | ".join(solver_names)})')
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
        print_stat.draw_all(args.table_out)
    elif args.command == 'batch':
        for bench in ["crypto", "lobster", "hd", "deobfusc"]:
            for solver in ["abs_synth", "duet", "probe"]:
                log_write_with_time(f"===== BATCH: run {solver} on {bench} =====")
                run.run_test(solver, bench, args.chosen, args.overwrite, args.timeout, args.thread_count)
            if args.ablation:
                for solver in ["abs_synth_bf", "abs_synth_smt", "abs_synth_smt_noback"]:
                    log_write_with_time(f"===== BATCH: run {solver} on {bench} =====")
                    run.run_test(solver, bench, args.chosen, args.overwrite, args.timeout, args.thread_count)
        print_stat.draw_all(args.table_out)
    elif args.command is None:
        print(f"Command Name is Required (run | stat | batch | clean)", file=sys.stderr)
    else:
        print(f"Not Supported Command {args.command}", file=sys.stderr)


if __name__ == '__main__':
    main()


# clear
# run blah blah
# stat blah blah
