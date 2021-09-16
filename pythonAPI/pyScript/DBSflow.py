import sys, os, shutil, time
from past.builtins import execfile

# opt flow
gen = 1
while gen <= maxGen:
    for p in range(N_dots):
        # 1 binary search 1 directory
        dotPath = f"{optPath}/Gen{gen}/p{p}"
        jobPath = f"{optPath}/Gen{gen}/p{p}/job.sh"
        os.chdir(dotPath)
        # get inherit FOM
        while True:
            try:
                fdtd = lumapi.FDTD("inherit.fsp", hide=True)
                fdtd.eval(getData) # You can edit this lsf file to set your own FOM
                inherit_T = fdtd.getv("T")
                fdtd.close()
            except:
                print(f"eval getData failed at {dotPath}/inherit.fsp")
            finally:
                break
        
        # build binary search txt & fsp (new pattern)
        dots = open(f"{dotPath}/inherit.txt", 'r').read()
        dots = dots.replace("\n", "")
        if dots[p] == '1':
            dots = dots[:p]+"0"+dots[p+1:]
            while True:
                try:
                    fdtd = lumapi.FDTD("inherit.fsp", hide=True)
                    fdtd.eval(del_dot.replace("{Number}", f"{p}"))
                    fdtd.save(f"{dotPath}/binarySearch.fsp")
                    fdtd.close()
                except:
                    print(f"eval del_dot failed at {dotPath}/inherit.fsp")
                finally:
                    break
        else:
            dots = dots[:p]+"1"+dots[p+1:]
            dot_y = 60 + (19 - i // 20) * 120
            dot_x = 60 + i % 20 * 120
            while True:
                try:
                    fdtd = lumapi.FDTD("inherit.fsp", hide=True)
                    fdtd.eval(add_dot.replace("{Number}", f"{i}").replace("dot_x", f"{dot_x}").replace("dot_y", f"{dot_y}"))
                    fdtd.save(f"{dotPath}/binarySearch.fsp")
                    fdtd.close()
                except:
                    print(f"eval add_dot failed at {dotPath}/inherit.fsp")
                finally:
                    break
        # save new pattern naming by binarySearch.fsp & binarySearch.txt
        
        with open(f"{dotPath}/binarySearch.txt", "w") as binarySearch:
            for i in range(N_dots):
                binarySearch.write(dots[i])
                if i%20 == 19 and i//20 != 19:
                    binarySearch.write('\n')
        # FDTD binarySearch.fsp
        fspPath = f"{dotPath}/binarySearch.fsp"
        execfile(f"{workPath}/pyScript/simuFDTD.py")
        # get FOM of new pattern
        while True:
            try:
                fdtd = lumapi.FDTD(f"{dotPath}/binarySearch.fsp", hide=True)
                fdtd.eval(getData) # You can edit this lsf file to set your own FOM
                binarySearch_T = fdtd.getv("T")
                fdtd.close()
            except:
                print(f"eval getData failed at {dotPath}/binarySearch.fsp")
            finally:
                break
        # Compare FOM
        nextDotPath = f"{optPath}/Gen{gen if p+1 != N_dots else gen+1}/p{0 if p+1 == N_dots else p+1}"
        if binarySearch_T > inherit_T:
            shutil.copy(f"{dotPath}/binarySearch.txt", f"{nextDotPath}/inherit.txt")
            shutil.copy(f"{dotPath}/binarySearch.fsp", f"{nextDotPath}/inherit.fsp")
        else:
            shutil.copy(f"{dotPath}/inherit.txt", f"{nextDotPath}/inherit.txt")
            shutil.copy(f"{dotPath}/inherit.fsp", f"{nextDotPath}/inherit.fsp")
    gen = gen+1

