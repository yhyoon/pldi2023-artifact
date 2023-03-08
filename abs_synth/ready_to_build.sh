#!/bin/bash

if [ ! -d "$HOME/.opam" ]
then
    opam init --auto-setup --disable-sandboxing --yes --compiler=$OCAML_VERSION && opam clean
fi

if [ ! -d "$HOME/.opam/abs_synth" ]
then
    opam switch create abs_synth 4.12.0
fi

opam switch abs_synth
opam install --yes dune merlin ocaml-lsp-server dune-build-info batteries ocamlgraph core_kernel yojson containers-data containers z3

# NOTE: if z3 install failed, install z3.4.8.5 instead of latest
# opam install --yes z3.4.8.5