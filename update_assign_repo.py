"""Uses rsync to copy all files from a source directory to target directories,
excluding .git directory and ipynb checkpoints. Will add git commit and push
capabilities once Classroom Assistant deals with the authentication setup"""  


import os
import sys
import glob

if (len(sys.argv) == 3):
    sourceDir= sys.argv[1]
    targetDir = sys.argv[2]
else:
    print("Force student repositories to match the state of a source. Excludes .git and checkpoints")
    print("Usage: python update_assign_repo.py [abs path to source] [abs path to target]")
    sys.exit()

targetRepos = glob.glob(targetDir + '/*')

for target in targetRepos:
    os.chdir(sourceDir)
    print(sourceDir, target)
    cmd = """rsync -avz --exclude=.git --exclude="*.ipynb_checkpoints" . """
    cmd = cmd + target + '/'
    print(cmd)
    os.system(cmd)
    os.chdir(target)
    print("git add .")
    print("git commit")
    print("git push")

