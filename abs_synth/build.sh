#!/bin/bash

dune build
dune install --prefix=_install
cp _install/bin/abs_synth abs_synth.exe
