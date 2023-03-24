# Artifacts for "Inductive Program Synthesis via Iterative Forward-Backward Abstract Interpretation"

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
* Username: abssynth
* Password: synthesis2023
* Note: tool name is changed from abs_synth to simba

The artifact is in directory `~/pldi2023-artifact`.

## Dependencies
This artifact requires following tools and libraries to build and run.

### TL;DR
In one line command:
```sh
$ ./prepare_dependency.sh
```
Be aware that all packages and libraries will be installed directly into your environment, and may affect your existing system, therefore proceed with caution.

### Detail

* `libgmp-dev`(https://gmplib.org/): for z3 solver (`simba`, `duet`)
```sh
$ sudo apt install libgmp-dev # for linux
$ brew install gmp # for mac
```
* `opam`(https://opam.ocaml.org/): for ocaml compiler (`simba`, `duet`)
```sh
$ sudo apt install opam  # for linux
$ brew install opam  # for mac
```

* `java 8`(https://openjdk.org/): for java compiler (`probe`)
```sh
$ sudo apt install open-jdk-8-jdk # for linux
$ brew install openjdk@8  # for mac
```

* `scala`, `sbt`(https://www.scala-lang.org/download/): for scala compiler (`probe`)
```sh
$ curl -fL https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup  # for linux
$ brew install coursier/formulas/coursier && cs setup  # for mac
```

* `cvc4`(https://cvc4.github.io/downloads.html): solver (`probe`)
```sh
$ # for linux
$ cd probe
$ wget https://github.com/CVC4/CVC4/releases/download/1.8/cvc4-1.8-x86_64-linux-opt
$ ln -s cvc4-1.8-x86_64-linux-opt cvc4
$ cd .. 
$
$ # for mac
$ brew tap cvc4/cvc4
$ brew install cvc4/cvc4/cvc4
```

* `python3`, `pip3`, `pandas` `matplotlib`: for running evaluation scripts (all)
```sh
$ sudo apt install python3  # for linux
$ sudo apt install python3-pip
$
$ brew install python3  # for mac
$
$ pip3 install pandas matplotlib  # common
```

* `probe`: a baseline solver
```sh
$ git clone git@github.com:shraddhabarke/probe.git
$ cd probe
$ git checkout f43ed831e0c8ac59ab68863cf6e5aaaa70ebfc3c  # last commit available at 2023-03-01
$ git apply ../probe_fix.patch  # fix build problem
$ cd ..
```

* `duet`: a baseline solver
```sh
$ git clone git@github.com:wslee/duet.git
$ cd duet
$ git checkout 627199a80c2eaad7c7a1c287ec65bf3de664e493  # last commit available at 2023-03-01
$ cd ..
```

* `simba`: our solver
```sh
git clone git@github.com:yhyoon/simba.git
```

## Build
tested on :
* Ubuntu 20.04.5 LTS 64bit Server
* Ubuntu 22.04.5 LTS 64bit Server
* macOS Ventura 13.1 (Intel Core Mac)

### TL;DR

In one line command:
```sh
$ ./build_all.sh
```

### Detail

The `./build_all.sh` script runs the following commands. 

```sh
$ cd simba
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

SOLVER_LIST is a list of solver names which are one of {simba, duet, probe, simba, simba_fonly, simba_smt}.  
BENCH_LIST is a list of benchmark set names which are on of {hd, deobfusc, crypto, lobster}. 

Each result will be stored into directory `pldi2023-artifact/result`
in csv format.

You can aggregate all the result files into single csv file by:

```sh
$ ./artifact aggregation [-csv_out CSV_FILE_PATH]
```


### Running Simba for other SyGuS problems
You can run Simba to solve other synthesis problems as follows:
```sh
$ simba/simba.exe <options> [a SyGuS input file]
```
The tool is also available in a separate [GitHub repository](https://github.com/yhyoon/simba).

You may find the options available by:
```sh
$ simba/simba.exe -help
```

For example, to solve the problem described in `bench/bitvec/hd/hd-17-d5-prog.sl`,
```sh
$ simba/simba.exe bench/bitvec/hd/hd-17-d5-prog.sl
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
$ simba/simba.exe -log stdout bench/bitvec/hd/hd-17-d5-prog.sl
$ simba/simba.exe -log solving-hd-17-d5.log bench/bitvec/hd/hd-17-d5-prog.sl
````
