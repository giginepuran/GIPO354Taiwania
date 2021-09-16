import sys, os, shutil, time, lumapi

fdtd = lumapi.FDTD(hide=True)

# Build fundamental structure
fdtd.eval(open("./DBS_lsf/setBase.lsf", 'r').read())

# Set initial dot distribution & clone the pattern with fsp
shutil.copy("./DBS_lsf/DBS20by20_ini.txt", "./optPath/initial.txt")
shutil.copy("./DBS_lsf/DBS20by20_ini.txt", "./optPath/Gen1/p0/inherit.txt")
with open("./DBS_lsf/DBS20by20_ini.txt", 'r') as ini:
    pattern = ini.read().replace('\n', '')
    etchScript = open("./DBS_lsf/setHole.lsf", 'r').read()
    for i in range(Nx*Ny):
        if pattern[i] == '1':
            dot_y = 60 + (19-i//20) * 120
            dot_x = 60 + i % 20 * 120        
            add_dot = etchScript.replace("{Number}", f"{i}")
            add_dot = add_dot.replace("dot_x", f"{dot_x}")
            add_dot = add_dot.replace("dot_y", f"{dot_y}")
        fdtd.eval(add_dot)

# Set Simulation region & run
fdtd.eval(open("./DBS_lsf/setSimu.lsf", 'r').read())
fdtd.save("./optPath/initial.fsp")

print("initial fsp is settled.")
