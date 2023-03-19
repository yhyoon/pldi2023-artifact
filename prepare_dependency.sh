#!/bin/bash

if [ ! -d "./probe" ]; then
  echo "first cloning probe"
  git clone git@github.com:shraddhabarke/probe.git
  cd probe
  git checkout f43ed831e0c8ac59ab68863cf6e5aaaa70ebfc3c  # last commit available at 2023-03-01
  git apply ../probe_fix.patch  # fix build problem
  cd ..
fi

if [ ! -d "./duet" ]; then
  echo "first cloning duet"
  git clone git@github.com:wslee/duet.git
  cd duet
  git checkout 627199a80c2eaad7c7a1c287ec65bf3de664e493  # last commit available at 2023-03-01
  cd ..
fi

if [ ! -d "./abs_synth" ]; then
  echo "first cloning abs_synth"
  git clone git@github.com:yhyoon/abs_synth.git
fi

if [ "$(uname)" = "Darwin" ]; then
  echo 'DO: brew install gmp opam openjdk@8 python3'
  brew install gmp opam openjdk@8 python3
  echo 'DO: brew install coursier/formulas/coursier && cs setup'
  brew install coursier/formulas/coursier && cs setup

  echo 'DO: brew tap cvc4/cvc4'
  brew tap cvc4/cvc4
  echo 'DO: brew install cvc4/cvc4/cvc4'
  brew install cvc4/cvc4/cvc4
else
  echo 'DO: sudo apt install libgmp-dev opam openjdk-8-jdk python3 python3-pip'
  sudo apt install libgmp-dev opam openjdk-8-jdk python3 python3-pip
  echo 'DO: curl -fL https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux-static.gz | gzip -d > cs && chmod +x cs && ./cs setup'
  curl -fL https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux-static.gz | gzip -d > cs && chmod +x cs && ./cs setup

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
