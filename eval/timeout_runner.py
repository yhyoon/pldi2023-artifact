import sys
import os
import argparse
import time
import subprocess
from typing import List, Optional, Tuple, Dict


class TimeoutRunner:
    cmd: str
    cmd_args: List[str]
    timeout: int
    env: Optional[Dict[str, str]]
    start_perf_time_ns: int
    end_perf_time_ns: Optional[int]
    proc: subprocess.Popen
    success_in_timeout: bool
    killed_by_timeout: bool
    captured_stdout: Optional[str]
    captured_stderr: Optional[str]

    def __init__(self, cmd: str, cmd_args: List[str], timeout: int, env: Dict[str, str] = None) -> None:
        self.cmd = cmd
        self.cmd_args = cmd_args[:]
        self.timeout = timeout
        if env is not None:
            self.env = dict()
            self.env.update(os.environ.copy())
            self.env.update(env)
        else:
            self.env = None
        self.captured_stdout = None
        self.captured_stderr = None
        self.success_in_timeout = False
        self.killed_by_timeout = False

        full_cmd = list()
        full_cmd.append(cmd)
        full_cmd.extend(cmd_args)
        self.end_perf_time_ns = None
        self.start_perf_time_ns = time.perf_counter_ns()
        self.proc = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=self.env)

    def get_pid(self) -> int:
        return self.proc.pid

    def wait_for_result(self) -> Tuple[Optional[str], Optional[str]]:
        try:
            (self.captured_stdout, self.captured_stderr) = self.proc.communicate(None, self.timeout)
            self.end_perf_time_ns = time.perf_counter_ns()
            self.success_in_timeout = True
        except subprocess.TimeoutExpired:
            self.proc.kill()
            (self.captured_stdout, self.captured_stderr) = self.proc.communicate()
            self.killed_by_timeout = True

        return self.captured_stdout, self.captured_stderr

    def get_elapsed_time(self) -> float:
        if self.end_perf_time_ns is None:
            raise ValueError("get_elapsed_time from process over timeout")
        else:
            return (self.end_perf_time_ns - self.start_perf_time_ns) / 1000000000


def main():
    parser = argparse.ArgumentParser(description='run command in subprocess with timeout using Popen')
    parser.add_argument('-timeout', metavar='TIME', type=str, nargs=1, required=True,
                        help='timeout with a measure in h/m/s order (ex: 10s, 6m30s, 1h30m)')
    parser.add_argument('cmds', metavar='COMMAND', type=str, nargs=argparse.REMAINDER,
                        help='actual command and parameters (required)')

    args = parser.parse_args()

    timeout_sec = 0
    timeout_str: str = args.timeout
    if 'h' in timeout_str:
        i = timeout_str.index('h')
        timeout_sec += 3600 * int(timeout_str[0:i])
        timeout_str = timeout_str[i + 1:]
    if 'm' in timeout_str:
        i = timeout_str.index('m')
        timeout_sec += 60 * int(timeout_str[0:i])
        timeout_str = timeout_str[i + 1:]
    if 's' in timeout_str:
        i = timeout_str.index('s')
        timeout_sec += int(timeout_str[0:i])

    handle = TimeoutRunner(args.cmds[0], args.cmds[1:], timeout_sec)
    print(f"run cmd [[{' '.join(sys.argv[1:])}]] [pid={handle.get_pid()}] in {args.timeout}(={timeout_sec}sec)")
    handle.wait_for_result()

    if handle.killed_by_timeout:
        print(f"    exceeded timeout(1 sec) => send kill to process [{handle.get_pid()}]")
    else:
        print(f"    terminated after {handle.get_elapsed_time()} sec ")

    print("### stdout ###")
    print(handle.captured_stdout)
    print("### ###### ###")
    print("### stderr ###")
    print(handle.captured_stderr)
    print("### ###### ###")


if __name__ == '__main__':
    main()
