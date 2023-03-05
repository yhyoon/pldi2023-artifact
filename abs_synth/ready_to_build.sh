if [ ! -d "$HOME/.opam" ]
then
    opam init
else
    echo "opam already initialized"
fi

if [[ ! -d "$HOME/.opam/abs_synth" ]]
then
    opam switch create abs_synth 4.12.0
else
    echo "switch 'abs_synth' already exists"
fi

opam switch abs_synth
opam install --yes dune merlin ocaml-lsp-server dune-build-info batteries ocamlgraph core_kernel yojson containers-data containers z3

# if z3 install failed, install z3.4.8.5 instead of latest
# opam install --yes z3.4.8.5