# Description

This repository is used to support the following work:

### A temporally resolved DNA framework state machine in living cells
Yan Zhao, Shuting Cao, Yue Wang, Fan Li, Linjie Guo, Fei Wang, Jie Chao, Xiaolei Zuo, Ying Zhu, Lihua Wang, Jiang Li* and Chunhai Fan*

It contains example oxDNA files and Gromacs files for simulating DNA framework state machine exported from a DNA design tool and running a basic equilibrium MD simulation.

# System requirements and Dependencies

The shell scripts in this repository need to be run in a Linux environment, and please ensure the following dependencies are installed：
- [caDNAno](https://github.com/douglaslab/cadnano2)
- [oxDNA](https://github.com/lorenzo-rovigatti/oxDNA)
- [Gromacs](https://github.com/gromacs/gromacs)
- Python 3.8 or above.

# Installation

 Please use CUDA support to compile oxDNA and Gromacs to the path `/opt`.
 
 All the files need to download and the shell scripts can be run directly in the Linux environment.

# Instructions.

This folder contains examples of DNA-framework-state-machine for performing coarse-grained equilibrium simulations and all-atom molecular dynamics equilibrium simulations. 

To run a simulation, please change the path to the directory containing the initial state and type:

`./oxDNA_DNAmachine.sh`
or
`./GMX_DNAmachine.sh`

All expected results can be reproduced. Simulations can be performed over days or weeks on a single Linux computer.
