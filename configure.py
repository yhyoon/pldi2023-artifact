import os
import sys
import platform
import getpass
import subprocess
from tempfile import NamedTemporaryFile
import re


def get_linux_version():
    # trial 1: via command lsb_release
    result_data = subprocess.run(['lsb_release', '-i', '-r'], stdout=subprocess.PIPE)
    if result_data.returncode == 0:
        id_matched = re.search(r'Distributor ID:\s+(\w+)', result_data.stdout.decode('utf-8')).group(1)
        version_matched = re.search(r'Release:\s+(\d+.\d+)', result_data.stdout.decode('utf-8')).group(1)
        if id_matched and version_matched:
            major_str, minor_str = version_matched.split('.')
            return id_matched.lower(), int(major_str), int(minor_str)

    # trial 2: via /etc/lsb-release
    try:
        with open('/etc/lsb-release', 'rt') as f:
            data = f.read()
            id_matched = re.search(r'DISTRIB_ID=(\w+)', data).group(1)
            version_matched = re.search(r'DISTRIB_RELEASE=(\d+.\d+)', data).group(1)
            if id_matched and version_matched:
                major_str, minor_str = version_matched.split('.')
                return id_matched.lower(), int(major_str), int(minor_str)
    except FileNotFoundError:
        pass

    # trial 3: via /etc/os-release
    try:
        with open('/etc/os-release', 'rt') as f:
            data = f.read()
            id_matched = re.search(r'ID=(\w+)', data).group(1)
            version_matched = re.search(r'VERSION_ID="(\d+.\d+)"', data).group(1)
            if id_matched and version_matched:
                major_str, minor_str = version_matched.split('.')
                return id_matched.lower(), int(major_str), int(minor_str)
    except FileNotFoundError:
        pass

    # trial 4: via /etc/issue
    try:
        with open('/etc/issue', 'rt') as f:
            data = f.read()
            id_matched = re.search(r'(\w+) (\d+.\d+)', data).group(1)
            version_matched = re.search(r'(\w+) (\d+.\d+)', data).group(2)
            if id_matched and version_matched:
                major_str, minor_str = version_matched.split('.')
                return id_matched.lower(), int(major_str), int(minor_str)
    except FileNotFoundError:
        pass

    # fail
    return "unknown", 0, 0


# return os and arch
# os: mac | ubuntu | linux (windows is not supported, linux = other linux distros than ubuntu)
# arch: x86 | arm
# (mac && arm = apple silicon)
def detect_system_kind():
    if sys.platform.startswith('win'):
        print('Error: Windows is not supported')
        sys.exit(1)

    if platform.processor() == 'arm' or platform.processor() == 'aarch64':
        arch_kind = 'arm'
        print(f'Warning: Some parts(e.g., running Probe) are not yet supported in {platform.processor()}')
    else:
        arch_kind = 'x86'

    if sys.platform == 'darwin':
        # mac os
        os_kind = 'mac'
        if arch_kind == 'arm':
            # m1
            print(f'Detected System: Apple Silicon({os_kind}, {arch_kind})')
        else:
            # intel
            print(f'Detected System: Apple Intel({os_kind}, {arch_kind})')

        # check if xcode is installed
        result_data = subprocess.run(['xcode-select', '-p'], stdout=subprocess.PIPE)
        if result_data.returncode != 0:
            print('Error: Xcode is not installed')
            print('Please install Xcode from App Store and run "xcode-select --install" in terminal')
            sys.exit(1)

        # check if brew is installed
        result_data = subprocess.run(['which', 'brew'], stdout=subprocess.PIPE)
        if result_data.returncode != 0:
            print('Error: Homebrew is not installed')
            print('Please install Homebrew from https://brew.sh/')
            sys.exit(1)

    elif 'linux' in sys.platform:
        id, major, minor = get_linux_version()
        if id == 'ubuntu':
            os_kind = 'ubuntu'
            print(f'Detected System: {os_kind}{major}.{minor} {arch_kind}')

            ubuntu_version = f'{major}.{minor}'
            if major < 20:
                print('Warning: Ubuntu version ' + ubuntu_version + ' is not tested')
        elif id != 'unknown':
            os_kind = 'linux'
            print(f'Detected System: {os_kind}{major}.{minor} {arch_kind}')
            print('Warning: this linux distribution is not tested')
        else:
            print('Unknown platform ' + sys.platform)
            sys.exit(1)
    else:
        print('Unknown platform ' + sys.platform)
        sys.exit(1)

    return os_kind, arch_kind


def opam_config_make_env():
    result = os.environ.copy()

    env_script = subprocess.run(['opam', 'config', 'env'], stdout=subprocess.PIPE)
    # split with \n and ;
    env_script_out_lines = re.split(r';|\n', env_script.stdout.decode('utf-8'))
    for line in env_script_out_lines:
        if line.strip().startswith('export'):
            # ignore
            pass
        elif '=' in line:
            k, v = line.strip().split('=')
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            elif v.startswith("'") and v.endswith("'"):
                v = v[1:-1]

            result[k] = v

    return result


def opam_switch_exists(switch_name):
    if subprocess.run(['opam', 'switch', 'show'], stdout=subprocess.PIPE).stdout.decode('utf-8') == switch_name:
        return True

    if subprocess.run(['opam', 'switch', 'list'], stdout=subprocess.PIPE).stdout.decode('utf-8').find(
            f" {switch_name} ") != -1:
        return True

    return False


def install_dependencies(os_kind, arch_kind):
    if getpass.getuser() == 'root':
        sudo_opt = []
    else:
        sudo_opt = ['sudo']

    # gmp, opam, jdk
    if os_kind == 'mac':
        if arch_kind == 'x86':
            print('Installing dependencies(gmp, opam, openjdk) with Homebrew... (this may take a while)')
            retcode = subprocess.call(['brew', 'install', 'gmp', 'opam', 'openjdk'])
            if retcode != 0:
                print('Error: brew failed')
                sys.exit(1)
        else:
            # Probe is not supported, we don't need jdk
            print('Installing dependencies(gmp, opam) with Homebrew... (this may take a while)')
            retcode = subprocess.call(['brew', 'install', 'gmp', 'opam'])
            if retcode != 0:
                print('Error: brew failed')
                sys.exit(1)
    else:
        print('Installing dependencies(curl, gmp, opam, openjdk) with apt-get... (this may take a while)')
        retcode = subprocess.call(
            [*sudo_opt, 'apt-get', 'install', '--yes', 'curl', 'libgmp-dev', 'opam', 'openjdk-11-jdk'])
        if retcode != 0:
            print('Error: apt-get failed')
            sys.exit(1)

    # opam init
    print('Initializing opam... (this may take a while)')
    retcode = subprocess.call(['opam', 'init', '--auto-setup', '--disable-sandboxing', '--yes'])
    if retcode != 0:
        print('Error: opam init failed')
        sys.exit(1)

    # scala build system
    if os_kind == 'mac':
        if arch_kind == 'arm':
            print('Skip installing sbt for Apple Silicon')
        else:
            print('Installing sbt with Homebrew... (this may take a while)')
            retcode = subprocess.call(['brew', 'install', 'sbt'])
            if retcode != 0:
                print('Error: brew failed')
                sys.exit(1)
    else:
        # linux
        if arch_kind == 'arm':
            print('Skip installing sbt for ARM')
        else:
            print('Installing sbt with coursier... (this may take a while)')
            curl_result = subprocess.run(['curl', '-fL', 'https://github.com/coursier/launchers/raw/master/coursier'],
                                         stdout=subprocess.PIPE)
            coursier = NamedTemporaryFile(delete=False)
            coursier.write(curl_result.stdout)
            os.chmod(coursier.name, 0o755)
            coursier.close()
            cs_result = subprocess.run([coursier.name, 'setup', '--yes'])
            os.unlink(coursier.name)
            if cs_result.returncode != 0:
                print('Error: coursier failed')
                sys.exit(1)
            os.environ['PATH'] = os.environ['PATH'] + ':' + os.path.expanduser('~/.local/share/coursier/bin')

    # cvc4
    if arch_kind == 'arm':
        print('Skip installing cvc4 for ARM')
    else:
        if os_kind == 'mac':
            print('Installing cvc4 with Homebrew... (this may take a while)')
            retcode = subprocess.call(['brew', 'tap', 'cvc4/cvc4'])
            if retcode != 0:
                print('Error: brew tap failed')
                sys.exit(1)
            retcode = subprocess.call(['brew', 'install', 'cvc4/cvc4/cvc4'])
            if retcode != 0:
                print('Error: brew install cvc4 failed')
                sys.exit(1)
        else:
            # linux
            print('Installing cvc4 with apt-get... (this may take a while)')
            retcode = subprocess.call([*sudo_opt, 'apt-get', 'install', '--yes', 'cvc4'])
            if retcode != 0:
                print('Error: apt-get install cvc4 failed')
                sys.exit(1)

    # prepare opam switch - duet
    if opam_switch_exists("duet"):
        print('opam switch for duet already exists')
    else:
        if os_kind == 'mac' and arch_kind == 'arm':
            print('Warn: Recommended ocaml version for Duet is 4.08.0, but it is not supported on Apple Silicon. '
                  'Use 4.12.0(the lowest version supported on Apple Silicon) instead. '
                  'Also, z3.4.8.1 is not supported on ocaml 4.12.0, so we use z3.4.8.14 instead. '
                  'The result may be different from the paper.')
            retcode = subprocess.call(['opam', 'switch', 'create', 'duet', '4.12.0', '--yes'])
            if retcode != 0:
                print('Error: opam switch create 4.08.0 failed')
                sys.exit(1)
        else:
            retcode = subprocess.call(['opam', 'switch', 'create', 'duet', '4.08.0', '--yes'])
            if retcode != 0:
                print('Error: opam switch create 4.08.0 failed')
                sys.exit(1)

    # prepare opam switch - simba
    if opam_switch_exists("simba"):
        print('opam switch for simba already exists')
    else:
        retcode = subprocess.call(['opam', 'switch', 'create', 'simba', '4.12.0', '--yes'])
        if retcode != 0:
            print('Error: opam switch create 4.12.0 failed')
            sys.exit(1)

    # install python packages for evaluation script
    print('Installing python packages for evaluation script...')
    retcode = subprocess.call(['python3', '-m', 'pip', 'install', 'pandas', 'matplotlib'])
    if retcode != 0:
        print('Error: pip install failed')
        sys.exit(1)


def build_all_solvers(os_kind, arch_kind):
    succeeded_solvers = []

    # Probe
    if arch_kind == 'arm':
        print('Skip building Probe for Apple Silicon')
    else:
        print('Building Probe...')
        subprocess.call(['tar', '-xzf', 'probe.f43ed83.fix.tar.gz'])
        # sbt assembly
        # check sbt exists
        retcode = subprocess.call(['which', 'sbt'])
        if retcode != 0:
            print('Error: sbt not found')
            sys.exit(1)

        retcode = subprocess.call(['sbt', 'assembly'], cwd=os.path.join(os.path.split(__file__)[0], 'probe'))
        if retcode != 0:
            print('Warn: sbt assembly failed')
            print('Keep going...')
        else:
            succeeded_solvers.append('probe')

    opam_ver_seq = subprocess.run(['opam', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip().split(
        ".")
    if int(opam_ver_seq[0]) >= 2 and int(opam_ver_seq[1]) >= 1:
        opam_install_cmd_head = ['opam', 'install', '--confirm-level=unsafe-yes']
    else:
        opam_install_cmd_head = ['opam', 'install', '--yes']

    # Duet
    print('Building Duet...')
    subprocess.call(['tar', '-xzf', 'duet.627199a.tar.gz'])
    subprocess.call(['opam', 'switch', 'duet'])
    duet_env = opam_config_make_env()
    if os_kind == 'mac' and arch_kind == 'arm':
        opam_pkgs_duet = ['ocamlbuild', 'containers', 'containers-data', 'z3.4.8.14', 'core', 'batteries', 'ocamlgraph']
    else:
        opam_pkgs_duet = ['ocamlbuild', 'containers', 'containers-data', 'z3.4.8.1', 'core.v0.13.0', 'batteries.3.0.0',
                          'ocamlgraph.1.8.8']
    retcode = subprocess.call([*opam_install_cmd_head, *opam_pkgs_duet],
                              env=duet_env)
    if retcode != 0:
        print('Warn: install opam package for duet (maybe) failed')
        check_result = subprocess.run(['opam', 'list', '-i', 'z3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check_result.stdout.decode('utf-8').find("No matches") != -1 or check_result.stderr.decode('utf-8').find(
                "No matches") != -1:
            print('retry install z3.4.8.14 instead of 4.8.1')
            subprocess.call([*opam_install_cmd_head, 'z3.4.8.14'],
                            env=duet_env)
        print('Keep going...')

    retcode = subprocess.call(['ocamlbuild', '-use-ocamlfind', 'src/main.native'],
                              cwd=os.path.join(os.path.split(__file__)[0], 'duet'),
                              env=duet_env)
    if retcode != 0:
        print('Warn: build duet failed')
        print('Keep going...')
    else:
        succeeded_solvers.append('duet')

    # Simba
    print('Building Simba...')
    subprocess.call(['tar', '-xzf', 'simba.7d0b304.tar.gz'])
    subprocess.call(['opam', 'switch', 'simba'])
    simba_env = opam_config_make_env()
    opam_pkgs_simba = ['dune', 'merlin', 'ocaml-lsp-server', 'dune-build-info', 'batteries', 'ocamlgraph',
                       'core_kernel', 'yojson', 'containers-data', 'containers', 'z3.4.8.14']
    retcode = subprocess.call([*opam_install_cmd_head, *opam_pkgs_simba],
                              env=simba_env)
    if retcode != 0:
        print('Warn: install opam package for simba (maybe) failed')
        print('Keep going...')

    retcode = subprocess.call(['dune', 'build'],
                              cwd=os.path.join(os.path.split(__file__)[0], 'simba'),
                              env=simba_env)
    if retcode != 0:
        print('Warn: build simba failed')
    else:
        # dune install --prefix=_install
        subprocess.call(['dune', 'install', '--prefix=_install'],
                        cwd=os.path.join(os.path.split(__file__)[0], 'simba'),
                        env=simba_env)
        # cp _install/bin/simba simba.exe
        subprocess.call(['cp', '_install/bin/simba', 'simba.exe'],
                        cwd=os.path.join(os.path.split(__file__)[0], 'simba'),
                        env=simba_env)
        succeeded_solvers.append('simba')

    if len(succeeded_solvers) > 0:
        print('Build succeeded solvers: {}'.format(', '.join(succeeded_solvers)))
    else:
        print('Build failed')
        sys.exit(1)

    if len(succeeded_solvers) < 3:
        print('Bulid failed solvers: {}'.format(', '.join({'probe', 'duet', 'simba'} - set(succeeded_solvers))))
        print(
            'You can run ./artifact command to run the artifact evaluation for the solvers that are built successfully')
    else:
        print('All solvers are built successfully')
        print('You can run ./artifact command to run the artifact evaluation')


def main(argv):
    # check system

    # system_kind is one of {'mac-intel', 'mac-apple-silicon', 'ubuntu', 'linux'}
    os_kind, arch_kind = detect_system_kind()

    install_dependencies(os_kind, arch_kind)
    build_all_solvers(os_kind, arch_kind)


if __name__ == '__main__':
    main(sys.argv[1:])
