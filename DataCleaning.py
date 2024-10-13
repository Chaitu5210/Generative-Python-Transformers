import os
dir="Data"
for dirpath,dirnames,filenames in os.walk(dir):
    for f in filenames:
        full_path=os.path.join(dirpath,f)
        if full_path.endswith(".py"):
            print("FOUND THE FILE",full_path)
        else:
            if dir in full_path:
                try:
                    print("Removing")
                    os.remove(full_path)
                except:
                    pass
import os
dir="Data"
for dirpath,dirnames,filenames in os.walk(dir):
    for f in filenames:
        full_path=os.path.join(dirpath,f)
        if full_path.endswith(".py"):
            print("FOUND THE FILE",full_path)
        else:
            if dir in full_path:
                try:
                    print("Removing")
                    os.remove(full_path)
                except:
                    pass
for dirpath, dirnames, filenames in os.walk(dir, topdown=False):
    for d in dirnames:
        full_path = os.path.join(dirpath, d)
        try:
            os.rmdir(full_path)
            print("Removed empty directory:", full_path)
        except OSError as e:
            # Directory not empty
            print("Directory not empty or error:", full_path, "Error:", e)
