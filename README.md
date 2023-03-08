# Artifacts for "Inductive Program Synthesis via Iterative Forward-Backward Abstract Interpretation"

## Virtual Machine Image

We provide a VirtualBox VM image to address the difficulty of setting up the execution environment for the artifact.
The image includes all the necessary components to immediately run the artifact.
You can skip the [Dependencies](#dependencies) and [Build](#build) part
and just jump to the [Running](#running) part.
However, due to limitations of the virtual machine,
it may not achieve the performance number reported in the paper.

* OS: Ubuntu 22.04.5 LTS 64bit Server
* Username: abssynth
* Password: synthesis2023

The artifact is in directory `~/pldi2023-artifact`.

## Dependencies
This artifact requires following tools and libraries to build and run.

* `libgmp-dev`(https://gmplib.org/): for z3 solver (`abs_synth`, `duet`)
```sh
$ sudo apt install libgmp-dev # for linux
$ brew install gmp # for mac
```
* `opam`(https://opam.ocaml.org/): for ocaml compiler (`abs_synth`, `duet`)
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

* `python3`, `pip`, `pandas` `matplotlib`: for running evaluation scripts (all)
```sh
$ sudo apt install python3  # for linux
$ sudo apt install python3-pip
$
$ brew install python3  # for mac
$ brew install pip3
$
$ pip3 install pandas matplotlib  # common
```

Or, in one line command:
```sh
$ ./prepare_dependency.sh
```
Be aware that all packages and libraries will be installed directly into your environment, and may affect your existing system, therefore proceed with caution.


## Build
tested on :
* Ubuntu 20.04.5 LTS 64bit Server
* macOS Ventura 13.1 (Intel Core Mac)

```sh
$ cd abs_synth
$ ./ready_to_build.sh
$ ./build.sh
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

Or, in one line command:
```sh
$ ./build_all.sh
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
