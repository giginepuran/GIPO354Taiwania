import sys, os, shutil, time, lumapi

pattern = open("./DBS_lsf/DBS20by20_ini.txt", 'r').read().replace('\n', '')
# Build fundamental structure


# Set initial dot distribution & clone the pattern with fsp
shutil.copy(f"{workPath}/DBS_lsf/DBS20by20_ini.txt", "./optPath/initial.txt")
shutil.copy(f"{workPath}/DBS_lsf/DBS20by20_ini.txt", "./optPath/Gen1/p0/inherit.txt")
while True:
    try:
        fdtd = lumapi.FDTD(hide=True)
        fdtd.eval(open(f"{workPath}/DBS_lsf/setBase.lsf", 'r').read())
        for i in range(Nx*Ny):
            if pattern[i] == '1':
                dot_y = 60 + (19-i//20) * 120
                dot_x = 60 + i % 20 * 120
                fdtd.eval(add_dot.replace("{Number}", f"{i}").replace("dot_x", f"{dot_x}").replace("dot_y", f"{dot_y}"))
        # Set Simulation region & run
        fdtd.eval(open(f"{workPath}/DBS_lsf/setSimu.lsf", 'r').read())
        fdtd.save(f"{workPath}/optPath/initial.fsp")
    except:
        print(f"eval build ini fsp failed")
    finally:
        break

print("initial fsp is settled.")
