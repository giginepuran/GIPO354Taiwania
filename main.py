import os, sys
from past.builtins import execfile

# step 0: prework
# Current directory
workPath = os.path.dirname(__file__)
sys.path.append(workPath)

# preRead some script template, using in opt process
del_dot = open(f"{workPath}/DBS_lsf/delHole.lsf", 'r').read()
add_dot = open(f"{workPath}/DBS_lsf/setHole.lsf", 'r').read()
getData = open(f"{workPath}/DBS_lsf/getData.lsf", 'r').read()
job_template = open(f"{workPath}/DBS_lsf/simuJob.sh", 'r').read()

# step 1: create opt env
execfile(f"{workPath}/pyScript/buildOptPath.py")

# step 2: create first fsp
execfile(f"{workPath}/pyScript/buildInitialPattern.py")

# step 3: FDTD the first fsp & clone it to next individual
os.chdir(optPath)
fspPath = f'{workPath}/optPath/initial.fsp'
jobPath = f"{optPath}/job.sh"
gen = "initial"
p = 0
execfile(f"{workPath}/pyScript/simuFDTD.py")
# inherit initial pattern to next Gen_p0
shutil.copy(f"{optPath}/initial.fsp", f"{optPath}/Gen1/p0/inherit.fsp")

# step 4: run DBS
execfile(f"{workPath}/pyScript/DBSflow.py")
