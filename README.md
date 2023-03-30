# Artifacts for "Inductive Program Synthesis via Iterative Forward-Backward Abstract Interpretation"

NOTE: We have changed the tool name from "AbsSynth" to "Simba" in the final version,
but this change is not applied in this artifact yet. So its name is still `AbsSynth`.
Final de-anonymized version of this artifact will contain the revised tool.

The artifacts include the main tool(AbsSynth), the other baseline solvers(Duet, Probe), benchmarks and evaluation scripts.

## Virtual Machine Image

We provide a [VirtualBox VM image](https://zenodo.org/record/7710618/files/pldi2023artifact_VM.zip?download=1) to address the difficulty
of setting up the execution environment for the artifact.
The image includes all the necessary components to immediately run the artifact.
You can skip the [Dependencies](#dependencies) and [Build](#build) part
and just jump to the [Running](#running) part.
However, due to limitations of the virtual machine,
it may not achieve the performance number reported in the paper.

* Tested on VM Player: [VirtualBox 7.0](https://www.virtualbox.org/wiki/Downloads)
* Tested on Host: macOS Ventura 13.1 with 2.3GHz QuadCore Intel Core i7
* Guest OS: Ubuntu 22.04.5 LTS 64bit Server
* Guest arch: `x86_64`
* Username: abssynth
* Password: synthesis2023

The artifact is in directory `~/pldi2023-artifact`.

## Docker Image

We also provide a [Docker](https://www.docker.com/) Image as an alternative to VM image.
Install [Docker Desktop](https://www.docker.com/products/docker-desktop/), download zipped docker image file and run with:
```sh
$ gzip -d <gzipped_docker_image_file>.tar.gz
$ docker load -i <extracted_docker_image_file>.tar
# time-consuming process...

# if you are in Intel x86_64 environment
$ docker run -it pldi2023-artifact-23:v1
(in-container) $ ./artifact batch ... 

# if you are in Apple Silicon(M1, M2, etc.) envirionment
# NOTE: less performance because this container will run on Apple Rosetta emulator
$ docker run -it --platform=linux/amd64 pldi2023-artifact-23:v1
(in-container) $ ./artifact batch ...
```

* Tested on Host:
  + macOS Ventura 13.1 with 2.3GHz QuadCore Intel Core i7
  + macOS Ventura 13.1 with Apple M1 (MacBook Pro 2020)
* Guest Arch: `x86_64`

## Limitation about test environment

### 1. OS and Architecture

Choose one of these list for test environment:
1. Best performance, but some tools and libs are installed into your environment
  + Ubuntu-20.04 or later with arch `x86_64`
  + MacOS with arch `x86_64`(Intel)
2. Safe and (relatively)easy, but cannot show full performance
  + Use provided docker image using docker desktop
  + Use provided VM Image using VirtualBox
3. If those `Best` or `Safe and Easy` items are not available
  + Use provided docker image using docker.io or any other container engine (we hope it works, but not tested)
  + MacOS with arch `arm64`(Apple Silicon) (in this case, testing `Probe` is not available)
  + Other Unix OS with `x86_64` (not tested, provided build scripts will not working)

* Build and run of `abs_synth` is tested on:
  + macOS Ventura arch `x86_64`
  + macOS Ventura arch `arm64`
  + ubuntu-20.04+ arch `x86_64`

### 2. Probe in `arm64`

`Probe` tightly depends on `cvc4` which is not available in `arm64`, so it cannot be tested on that environment.
If you are not interested in comparing `abs_synth` to `probe`,
you can skip the related dependencies(`java`, `coursier`, `sbt`, `cvc4`, etc.)
and run the test for the other tools.

### 3. Duet in `macOS` `monterey` or later

Build `Duet` maybe failed on `macOS` `monterey` or later because of build failure of dependency z3.4.8.1.
z3.4.8.1 depends on python2 which is removed from `monterey`.
You can avoid this issue by installing z3.4.8.14 instead of 4.8.1. (`opam switch duet 4.08.0` ; `eval $(opam config env)` ; `opam install --yes z3.4.8.14` ; `make`)

### 4. Additional tools for Mac

If you want to run this artifact manually on macOS, you need install [Xcode Command Line Tools](https://mac.install.guide/commandlinetools/4.html) and [Homebrew](https://brew.sh/index) before the following detailed steps.

If you don't want to install these tools or the other dependency libraries, it's recommended to use VM Image or Docker Image we provided.

## Dependencies and Build
This artifact requires following tools and libraries to build and run.

### TL;DR
In short:
```sh
$ cd pldi2023-artifact
$ python3 -m pip install --user virtualenv
$ python3 -m virtualenv .env --python=python3.10
$ source .env/bin/activate
$ python3 configure.py
```

If you are using `linux` system, it is important that you have sudoer permission in your environment for `sudo apt-get install SOMETHING`. When you encounter this situation for the first time, you will be prompted to input your password. Therefore, please note that this process is not completely noninteractive.

It is also important to keep in mind that all packages and libraries will be directly installed into your environment, which could potentially affect your existing system. Therefore, it is strongly advised that you proceed with caution.

### Dependencies

* `python3`: for running build and evaluation scripts
The build and evaluation script is written in [Python3](https://www.python.org/downloads/)
Version 3.10 or later is recommended.

* `curl`: for running some build commands(linux)
```sh
$ sudo apt-get install -y curl # for linux
```

* `libgmp-dev`(https://gmplib.org/): for z3 solver (`abs_synth`, `duet`)
```sh
$ sudo apt-get install -y libgmp-dev # for linux
$ brew install gmp # for mac
```
* `opam`(https://opam.ocaml.org/): for ocaml compiler (`abs_synth`, `duet`)
```sh
$ sudo apt-get install -y opam  # for linux
$ brew install opam  # for mac
$
$ opam init --auto-setup --disable-sandboxing --yes
$

```

* `openjdk`(Linux - https://openjdk.org/): for java compiler (`probe`)
```sh
$ sudo apt-get install -y openjdk-11-jdk # for linux
$
$ brew install openjdk # for mac
```

* `scala`, `sbt`(https://www.scala-lang.org/download/): for scala compiler (`probe`)
```sh
# java must be installed before this step
$ curl -fLo coursier https://github.com/coursier/launchers/raw/master/coursier && chmod +x coursier && ./coursier setup --yes  # for linux
$
$ brew install sbt  # for mac
```

* `cvc4`(https://cvc4.github.io/downloads.html): solver (`probe`)
```sh
$ # for linux case 1: if available
$ sudo apt-get install cvc4
$
$ # for linux case 2: if apt-get install is not working
$ cd probe
$ wget https://github.com/CVC4/CVC4/releases/download/1.8/cvc4-1.8-x86_64-linux-opt
$ ln -s cvc4-1.8-x86_64-linux-opt cvc4
$ cd .. 
$
$ # for mac
$ brew tap cvc4/cvc4
$ brew install cvc4/cvc4/cvc4
```

* `pandas` `matplotlib`: for running evaluation scripts (all)
```sh
$ python3 -m pip install pandas matplotlib  # common
```

### Build
Tested on :
* Ubuntu 20.04.5 LTS 64bit Server
* Ubuntu 22.04.5 LTS 64bit Server
* macOS Ventura 13.1 (Intel Core Mac)
* macOS Ventura 13.1 (Apple Silicon M1 Mac):
  + only abs_synth builds in default
  + cannot use probe
  + for duet, `opam install ocamlbuild containers containers-data z3.4.8.14 core batteries ocamlgraph && make` instead of `./build`

Run the following commands:
```sh
$ cd abs_synth
$ ./first_build.sh
$ cd ..
$
$ cd duet
$ ./build
$ cd ..
$
$ cd probe
$ sbt assembly
$ cd ..
```

## Running

### Reproducing the main results in the paper

```sh
$ ./artifact [-log LOG_FILE_PATH] batch [-timeout <sec>] [-p <num_cores>] [-table_out TABLE_FILE_PATH]
```
You can specify a timeout and the number of CPU cores to be used for parallel execution.
This step is time-consuming. Therefore, we strongly recommend you use enough cores to expedite the experiments.

In default, The progress will be printed to standard output.
You can specify an alternative log file path with `-log` option.

All the tables (such as Figure 3.(c)) also will be printed to standard output.
You can specify an alternative output file path with `-table_out`option.

All the plot figures (problem solved plot, cactus plot, etc.) will be stored
in the `pldi2023-artifact/figure` directory.

After running the above commands, you can re-draw the tables and figures without re-running solvers by the following command:
```sh
$ ./artifact stat [-main_table] [-detail_table] [-ablation_table] [-plot] [-table_out TABLE_FILE_PATH
```

## Reproducing the results for the chosen 20 benchmark problems (Table 1 in the paper)
```sh
$ ./artifact [-log LOG_FILE_PATH] batch -chosen [-timeout <sec>] [-p <num_cores>] [-table_out TABLE_FILE_PATH] 
```

This command will produce Table 1. If you have run the command for the main results, the table will be immediately shown.
Otherwise, it will run each solver for each benchmark in turn.  

### Running specific solvers & benchmarks

You can evaluate your interested solvers and benchmark sets as follows:
```sh
$ ./artifact [-log LOG_FILE_PATH] run -solvers [SOLVER_LIST] -benches [BENCH_LIST] [-timeout <sec>] [-p <num_cores>]
```

SOLVER_LIST is a list of solver names which are one of {abs_synth, duet, probe, abs_synth_bf, abs_synth_fonly, abs_synth_smt}.  
BENCH_LIST is a list of benchmark set names which are on of {hd, deobfusc, crypto, lobster}. 

Each result will be stored into directory `pldi2023-artifact/result`
in csv format.

You can aggregate all the result files into single csv file by:

```sh
$ ./artifact aggregation [-csv_out CSV_FILE_PATH]
```


### Running AbsSynth for other SyGuS problems
You can run AbsSynth to solve other synthesis problems as follows:
```sh
$ abs_synth/abs_synth.exe <options> [a SyGuS input file]
```
The tool is also available in a separate GitHub repository(Anonymized).

You may find the options available by:
```sh
$ abs_synth/abs_synth.exe -help
```

For example, to solve the problem described in `bench/bitvec/hd/hd-17-d5-prog.sl`,
```sh
$ abs_synth/abs_synth.exe bench/bitvec/hd/hd-17-d5-prog.sl
````
You will get the following output:
```sh
(define-fun f ( (x (BitVec 64))) (BitVec 64) (bvand (bvneg (bvand (bvnot x) (bvneg x))) x))
****************** statistics *******************
size : 8
time : 1.24 sec
final max component size : 6
final component pool size : 4617
**************************************************
```

The first line shows a desirable solution (f is the target synthesis function), and the other lines show some useful statistics.

For more detailed progress log and statistics, use option `-log` as follows:
```sh
$ abs_synth/abs_synth.exe -log stdout bench/bitvec/hd/hd-17-d5-prog.sl
$ abs_synth/abs_synth.exe -log solving-hd-17-d5.log bench/bitvec/hd/hd-17-d5-prog.sl
````
