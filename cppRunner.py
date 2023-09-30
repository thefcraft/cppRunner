import sys, os

def deleteFile(filename): 
    os.remove(filename)
    return not os.path.exists(filename)
def fileNameWithoutExt(path): return ".".join(os.path.basename(path).split(".")[:-1])

path = sys.argv[1]
if not os.path.exists(path): 
    path = os.path.join(os.getcwd(), path)
    if not os.path.exists(path): raise ValueError("Could not find path %s" % path)

exeName = fileNameWithoutExt(path)
command = f'c++ "{path}" -o {exeName}.exe'  # "~pathForMingw~\mingw\bin\c++.exe" but i already add this to my environment variable
runCommand = f'{exeName}.exe'

# Compile the C++ file
os.system(command)

os.system(runCommand)

deleteFile(f"{exeName}.exe")