import json
import os.path
import shutil

TMPDIR = "/opt/joe_holding"

def delete(file, path):

    file = json.loads(file)
    path = json.loads(path)
    
    # delete for-real the temp stuff from previous time
    prev = os.listdir(TMPDIR)
    print(prev)
    #if prev != "":
      #ß  shutil.rmtree(TMPDIR)

    # phony delete from Downloads
    origpath = os.path.join(path, file)
    destpath = os.path.join(TMPDIR, file)
    shutil.move(origpath, destpath)

    return("Complete.")