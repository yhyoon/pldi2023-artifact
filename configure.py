import os
import sys
import platform
import getpass
import subprocess
import re


def detect_system_kind():
    if sys.platform.startswith('win'):
        print('Error: Windows is not supported')
        sys.exit(1)
    elif sys.platform == 'darwin':
        # mac os
        if platform.processor() == 'arm':
            # m1
            system_kind = 'mac-apple-silicon'
            print('Detected System: ' + system_kind)
            print('Warning: Some parts(e.g., running Probe) are not yet supported in Apple Silicon')
        else:
            system_kind = 'mac-intel'
            print('Detected System: ' + system_kind)
        
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
        if 'ubuntu' in platform.version().lower():
            system_kind = 'ubuntu'
            print('Detected System: ' + system_kind)

            result_data = subprocess.run(['hostnamectl'], stdout=subprocess.PIPE)
            result_out = result_data.stdout.decode('utf-8').splitlines()
            for line in result_out:
                if line.strip().startswith('Operating System:'):
                    ubuntu_version = re.search(r'Ubuntu (\d+.\d+)', line).group(1)
                    print('Detected Ubuntu version: ' + ubuntu_version)
                    if not ubuntu_version.startswith('20.') and not ubuntu_version.startswith('22.'):
                        print('Warning: Ubuntu version ' + ubuntu_version + ' is not tested')                    
        else:
            system_kind = 'linux'
            print('Detected System: ' + system_kind)
            print('Warning: this linux distribution is not tested: ' + sys.platform)
    else:
        print('Unknown platform ' + sys.platform)
        sys.exit(1)
    
    return system_kind


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

    if subprocess.run(['opam', 'switch', 'list'], stdout=subprocess.PIPE).stdout.decode('utf-8').find(f" {switch_name} ") != -1:
        return True

    return False


def install_dependencies(system_kind):
    if getpass.getuser() == 'root':
        sudo_opt = []
    else:
        sudo_opt = ['sudo']

    # gmp, opam, jdk
    if system_kind == 'mac-intel':
        print('Installing dependencies(gmp, opam, openjdk) with Homebrew... (this may take a while)')
        retcode = subprocess.call(['brew', 'install', 'gmp', 'opam', 'openjdk'])
        if retcode != 0:
            print('Error: brew failed')
            sys.exit(1)
    elif system_kind == 'mac-apple-silicon':
        # Probe is not supported, we don't need jdk
        print('Installing dependencies(gmp, opam) with Homebrew... (this may take a while)')
        retcode = subprocess.call(['brew', 'install', 'gmp', 'opam'])
        if retcode != 0:
            print('Error: brew failed')
            sys.exit(1)
    else:
        print('Installing dependencies(curl, gmp, opam, openjdk) with apt-get... (this may take a while)')
        retcode = subprocess.call([*sudo_opt, 'apt-get', 'install', '--yes', 'curl', 'libgmp-dev', 'opam', 'openjdk-11-jdk'])
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
    if system_kind == 'mac-apple-silicon':
        print('Skip installing sbt for Apple Silicon')
    elif system_kind == 'mac-intel':
        print('Installing sbt with Homebrew... (this may take a while)')
        retcode = subprocess.call(['brew', 'install', 'sbt'])
        if retcode != 0:
            print('Error: brew failed')
            sys.exit(1)
    else:
        # linux
        print('Installing sbt with coursier... (this may take a while)')
        curl_result = subprocess.run(['curl', '-fLo', 'coursier', 'https://github.com/coursier/launchers/raw/master/coursier'], stdout=subprocess.PIPE)
        cs_result = subprocess.run(['bash', '-s', '--', 'setup', '--yes'], input=curl_result.stdout)
        if cs_result.returncode != 0:
            print('Error: coursier failed')
            sys.exit(1)

    # cvc4
    if system_kind == 'mac-apple-silicon':
        print('Skip installing cvc4 for Apple Silicon')
    elif system_kind == 'mac-intel':
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
        if system_kind == 'mac-apple-silicon':
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

    # prepare opam switch - abssynth
    if opam_switch_exists("abs_synth"):
        print('opam switch for abs_synth already exists')
    else:
        retcode = subprocess.call(['opam', 'switch', 'create', 'abs_synth', '4.12.0', '--yes'])
        if retcode != 0:
            print('Error: opam switch create 4.12.0 failed')
            sys.exit(1)

    # install python packages for evaluation script
    print('Installing python packages for evaluation script...')
    retcode = subprocess.call(['python3', '-m', 'pip', 'install', 'pandas', 'matplotlib'])
    if retcode != 0:
        print('Error: pip install failed')
        sys.exit(1)


def build_all_solvers(system_kind):
    succeeded_solvers = []

    # Probe
    if system_kind == 'mac-apple-silicon':
        print('Skip building Probe for Apple Silicon')
    else:
        print('Building Probe...')
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

    # Duet
    print('Building Duet...')
    subprocess.call(['opam', 'switch', 'duet'])
    duet_env = opam_config_make_env()
    if system_kind == 'mac-apple-silicon':
        opam_pkgs_duet = ['ocamlbuild', 'containers', 'containers-data', 'z3.4.8.14', 'core', 'batteries', 'ocamlgraph']
    else:
        opam_pkgs_duet = ['ocamlbuild', 'containers', 'containers-data', 'z3.4.8.1', 'core.v0.13.0', 'batteries.3.0.0', 'ocamlgraph.1.8.8']
    retcode = subprocess.call(['opam', 'install', '--confirm-level=unsafe-yes', *opam_pkgs_duet],
                              env=duet_env)
    if retcode != 0:
        print('Warn: install opam package for duet (maybe) failed')
        check_result = subprocess.run(['opam', 'list', '-i', 'z3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check_result.stdout.decode('utf-8').find("No matches") != -1 or check_result.stderr.decode('utf-8').find("No matches") != -1:
            print('retry install z3.4.8.14 instead of 4.8.1')
            subprocess.call(['opam', 'install', '--confirm-level=unsafe-yes', 'z3.4.8.14'],
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

    # AbsSynth
    print('Building AbsSynth...')
    subprocess.call(['opam', 'switch', 'abs_synth'])
    abs_synth_env = opam_config_make_env()
    opam_pkgs_abs_synth = ['dune', 'merlin', 'ocaml-lsp-server', 'dune-build-info', 'batteries', 'ocamlgraph', 'core_kernel', 'yojson', 'containers-data', 'containers', 'z3.4.8.14']
    retcode = subprocess.call(['opam', 'install', '--confirm-level=unsafe-yes', *opam_pkgs_abs_synth],
                   env=abs_synth_env)
    if retcode != 0:
        print('Warn: install opam package for abs_synth (maybe) failed')
        print('Keep going...')

    retcode = subprocess.call(['dune', 'build'],
                                cwd=os.path.join(os.path.split(__file__)[0], 'abs_synth'),
                                env=abs_synth_env)
    if retcode != 0:
        print('Warn: build abs_synth failed')
    else:
        # dune install --prefix=_install
        subprocess.call(['dune', 'install', '--prefix=_install'],
                                    cwd=os.path.join(os.path.split(__file__)[0], 'abs_synth'),
                                    env=abs_synth_env)
        # cp _install/bin/abs_synth abs_synth.exe
        subprocess.call(['cp', '_install/bin/abs_synth', 'abs_synth.exe'],
                                    cwd=os.path.join(os.path.split(__file__)[0], 'abs_synth'),
                                    env=abs_synth_env)
        succeeded_solvers.append('abs_synth')

    if len(succeeded_solvers) > 0:
        print('Build succeeded solvers: {}'.format(', '.join(succeeded_solvers)))
    else:
        print('Build failed')
        sys.exit(1)

    if len(succeeded_solvers) < 3:
        print('Bulid failed solvers: {}'.format(', '.join(set(['probe', 'duet', 'abs_synth']) - set(succeeded_solvers))))
        print('You can run ./artifact command to run the artifact evaluation for the solvers that are built successfully')
    else:
        print('All solvers are built successfully')
        print('You can run ./artifact command to run the artifact evaluation')


def main(argv):
    # check system
    
    # system_kind is one of {'mac-intel', 'mac-apple-silicon', 'ubuntu', 'linux'}
    system_kind = detect_system_kind()

    install_dependencies(system_kind)
    build_all_solvers(system_kind)


if __name__ == '__main__':
    main(sys.argv[1:])
