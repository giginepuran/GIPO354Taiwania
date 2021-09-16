import sys, os

# Check lumerical install directory
apiPath = "/home/u6097335/tools/lumerical/v211/api/python/"
sys.path.append(apiPath)
print("API setting complete.")

# optimization environment initializing
# 1 genration 1 directory,
# there are N particles(directory) in one generation
maxGen = 10
Nx = 20
Ny = 20
N_dots = Nx*Ny
optPath = f"{workPath}/optPath"
if(not os.path.isdir(optPath)):
    os.mkdir(optPath)
for i in range(maxGen+1):
    # create generation directory
    genDir = f"{optPath}/Gen{i+1}"
    if(not os.path.isdir(genDir)):
        os.mkdir(genDir)
    for j in range(N_dots):
        # create particle directory
        if (not os.path.isdir(f"{genDir}/p{j}")):
            os.mkdir(f"{genDir}/p{j}")
print("Optimization Path setting complete.")
