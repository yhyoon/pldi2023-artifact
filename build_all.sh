#!/usr/bin/env bash

set -Eeuo pipefail

echo "Build Simba"
cd simba
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
    export PATH="$PATH:$HOME/.local/share/coursier/bin"
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
