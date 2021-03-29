from pathlib import Path

#path = Path("newdirectory")           # A FILE OR DIRECTORY
#print(path.exists())                            # -- .exists (returns a boolean - to see if the file / directory exists)

#print(path.mkdir())     # this would create the new directory(not existing) and would return NONE

#print(path.rmdir())  # This also removes the directory and returns NONE

path = Path()           # ---- current directory()
for file in path.glob("*"):
    print(file)