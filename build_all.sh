#!/bin/bash

cd abs_synth
./ready_to_build.sh
./build.sh
cd ..

cd duet
./build
cd ..

cd probe
sbt assembly
cd ..
