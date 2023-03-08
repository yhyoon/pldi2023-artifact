#!/bin/bash

echo "Build AbsSynth"
cd abs_synth
./first_build.sh
cd ..

echo "Build Duet"
cd duet
./build
make
cd ..

echo "Build Probe"
cd probe
sbt assembly
cd ..
