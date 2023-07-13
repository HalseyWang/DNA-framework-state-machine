#!/bin/bash

CODEDIR=/opt/gromacs
GMX_BIN=$CODEDIR/bin/gmx

echo "Simulating a New Work"

if [ -e $GMX_BIN ]
then
    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN pdb2gmx -f 6HB.pdb -n -o 6HB.gro -ignh -missing -ter -n

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN editconf -f 6HB.gro -o box.gro -c -bt cubic -d 1.0

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN editconf -f 6HB.gro -o box.gro -c -box 30 30 30

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN solvate -cp box.gro -cs spc216.gro -p topol.top -o water.gro

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN grompp -f minim.mdp -c water.gro -p topol.top -o ions.tpr -maxwarn 2

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN genion -s ions.tpr -o ions.gro -p topol.top -pname MG -conc 0.125 -neutral

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN genion -s em.tpr -o em-neutral.gro -p topol.top -neutral

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN grompp -f minim.mdp -c em-neutral.gro -p topol.top -o em.tpr -maxwarn 2

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN mdrun -v -deffnm em -nt 100

    # run the examples
    echo "1 step: Preparing materials"
    #$GMX_BIN gmx make_ndx -f em.gro -o index.ndx

    # run the examples
    echo "2 step: Preparing nvt simulation"
    $GMX_BIN grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o nvt.tpr -maxwarn 2

    # run the examples
    echo "2 step: Starting nvt simulation"
    $GMX_BIN mdrun -v -deffnm nvt -nb gpu
    
    # run the examples
    echo "3 step: Preparing npt simulation"
    $GMX_BIN grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -n index.ndx -o npt.tpr -maxwarn 2
    
    # run the examples
    echo "3 step: Starting npt simulation"
    $GMX_BIN mdrun -v -deffnm npt -nb gpu

    # run the examples
    echo "4 step: Preparing md simulation"
    $GMX_BIN grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md.tpr

    # run the examples
    echo "4 step: Starting md simulation"
    $GMX_BIN mdrun -v -deffnm md -nb gpu
else
    echo "Can't find $GMX_BIN, did you compile gmx?"
    exit
fi
