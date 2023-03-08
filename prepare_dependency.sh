#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
  brew install gmp opam openjdk@8 python3 pip3
  brew install coursier/formulas/coursier && cs setup
else
  sudo apt install libgmp-dev opam open-jdk-8-jdk python3 python3-pip
  curl -fL https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup
fi

pip3 install pandas matplotlib
