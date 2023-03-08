#!/bin/bash

if [ "$(uname)" = "Darwin" ]; then
  echo 'DO: brew install gmp opam openjdk@8 python3 pip3'
  brew install gmp opam openjdk@8 python3 pip3
  echo 'DO: brew install coursier/formulas/coursier && cs setup'
  brew install coursier/formulas/coursier && cs setup

  echo 'DO: brew tap cvc4/cvc4'
  brew tap cvc4/cvc4
  echo 'DO: brew install cvc4/cvc4/cvc4'
  brew install cvc4/cvc4/cvc4
else
  echo 'DO: sudo apt install libgmp-dev opam openjdk-8-jdk python3 python3-pip'
  sudo apt install libgmp-dev opam openjdk-8-jdk python3 python3-pip
  echo 'DO: curl -fL https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup'
  curl -fL https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup

  echo 'DO: cd probe'
  cd probe
  echo 'DO: wget https://github.com/CVC4/CVC4/releases/download/1.8/cvc4-1.8-x86_64-linux-opt'
  wget https://github.com/CVC4/CVC4/releases/download/1.8/cvc4-1.8-x86_64-linux-opt
  echo 'DO: chmod +x cvc4-1.8-x86_64-linux-opt'
  chmod +x cvc4-1.8-x86_64-linux-opt
  echo 'DO: ln -s cvc4-1.8-x86_64-linux-opt cvc4'
  ln -s cvc4-1.8-x86_64-linux-opt cvc4
  echo 'DO: cd ..'
  cd ..
fi

pip3 install pandas matplotlib
