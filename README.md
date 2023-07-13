# DNA-Framework-State-Machine

This folder contains example oxDNA files and Gromacs files for simulating DNA framework state machine exported from a DNA design tool and running a basic equlibrium MD simulation.

# System requirements and Dependencies

The shell scripts in this repository need to be run in a linux environment, and please ensure the following dependencies are installed：
- [oxDNA](https://github.com/lorenzo-rovigatti/oxDNA)
- [Gromacs](https://github.com/gromacs/gromacs)
- Python 3.8 or above.

# Installation

 Please use CUDA support to compile oxDNA and Gromacs to path `/opt`
 
 All the files need to download and the shell scripts can be run directly in the linux environment.

# Instructions.

This folder contains examples of DNA-framework-state-machine for performing coarse-grained equilibrium simulations and all-atom molecular dynamics equilibrium simulations. 

To run a simulation, please change the path to the directory containing the initial state and type:

`$./oxDNA_DNAmachine.sh`
or
`$./GMX_DNAmachine.sh`

All expected results can be reproduced. Simulations can be performed over days or weeks on a single Linux computer.
