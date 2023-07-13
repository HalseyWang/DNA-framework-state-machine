#!/bin/bash

CODEDIR=/opt/oxDNA/build
OXDNA_BIN=$CODEDIR/bin/oxDNA

echo "Simulating a New Job at 300 K"

if [ -e $OXDNA_BIN ]
then
    # prepare the inputMD_seq_dep file
    #sed "s;seq_dep_file = ../../oxDNA1_sequence_dependent_parameters.txt;seq_dep_file = $CODEDIR\/oxDNA1_sequence_dependent_parameters.txt;" input_seq_dep > input.tmp
    #mv -f input.tmp input_seq_dep

    # run the examples
    echo "Starting MC simulation"
    $OXDNA_BIN relax_MC
    
    echo "Starting MD relax simulation"
    $OXDNA_BIN relax_MD

    echo "Starting MD simulation"
    $OXDNA_BIN run
else
    echo "Can't find $OXDNA_BIN, did you compile oxDNA?"
    exit
fi
