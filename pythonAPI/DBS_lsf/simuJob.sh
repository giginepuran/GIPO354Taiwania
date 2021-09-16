#!/bin/bash
#PBS -P MST107345
#PBS -l walltime=00:02:00
#PBS -l select=1:ncpus=40
#PBS 
#PBS -N opt_G{gen}_P{p}
#PBS -j oe
#PBS -M {email}
#PBS -m abe
#PBS -q ctest
# ^PBS setting
# job

cd /home/u6097335/pythonAPI
module load intel/2018_u1
export I_MPI_HYDRA_BRANCH_COUNT=-1
# simulation test
mpiexec.hydra /home/u6097335/tools/lumerical/v211/bin/fdtd-engine-impi-lcl -logall {filePath}
# {fP} = /home/u6097335/pythonAPI/optPath/Gen1/p0/inherit.fsp
