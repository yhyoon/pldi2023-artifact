dune build
dune install --prefix=_install
ln -s _install/bin/abs_synth abs_synth.exe
cp _install/bin/abs_synth abs_synth.`git rev-parse --short HEAD`.exe
