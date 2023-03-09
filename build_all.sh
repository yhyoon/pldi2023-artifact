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
if ! command -v sbt &> /dev/null
then
    # update env variable for coursier
    export PATH="$PATH:/home/yoony/.local/share/coursier/bin"
fi

# re-check
if ! command -v sbt &> /dev/null
then
    echo "check if sbt is correctly installed. restart the shell maybe helpful."
    cd ..
    exit
fi

sbt assembly
cd ..
