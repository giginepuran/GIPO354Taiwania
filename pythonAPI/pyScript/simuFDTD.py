import sys, os, shutil, time

# read & edit job script for qsub
job = job_template.replace("{filePath}", f"{fspPath}")
job = job.replace("{gen}", f"{gen}")
job = job.replace("{p}", f"{p}")
if p%10 == 0:
    job = job.replace("{email}", "r09941007@g.ntu.edu.tw")
with open(f"{jobPath}", "w") as job_sh: # overwrite
    job_sh.write(job)
# qsub & get queue number
job_queue = os.popen("qsub job.sh").read().replace(".srvcl","").replace("\n","")
#print(f"job_queue = {job_queue}")
# check whether siumlation is done by qstat
while True:
    time.sleep(5) # sleep 5 sec
    job_stat = os.popen(f"qstat -H {job_queue}").read()
    #print(f"job_stat = {job_stat}")
    if " F " in job_stat:
        break
print("Simulation is complete.")
