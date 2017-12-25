from radioclash.sources.config_app import cfg
import os.path
import os
import shutil


def move(data):
    #data = json.loads(data)
    title = data['title']
    type = data['type']

    print(app_cfg['dummycopy'])

    if app_cfg["dummycopy"] == 'true':
        dummycopy = True
        dummydir = "/home/bundito/Backup"
    print(dummycopy)


    print("MMM")
    print(app_cfg)
    print("MMM")


    if type == "tv":

        if app_cfg["dummycopy"] == 'true':
            dummycopy = True
            dummydir = "/home/bundito/Backup"
            print(dummycopy)

        if dummycopy:
            destbasepath = dummydir
        else:
            destbasepath = cfg['mediadirs']['TV']


        destpath = os.path.join(destbasepath, data['title'])
        if not os.path.exists(destpath):
            os.makedirs(destpath)

        for file in data['episodes']:
            origitem = os.path.join(data['path'], file)
            shutil.move(origitem, destpath)


        if data['filefolder'] == "folder":
            deaddir = data['path']
            os.rmdir(deaddir)

        if dummycopy:
            return ("Simulated copy.")
        else:
            return ("Live copy complete.")

    if type == "movie":

        if app_cfg["dummycopy"] == 'true':
            dummycopy = True
            dummydir = "/home/bundito/Backup"
            print(dummycopy)
            print(app_cfg['dummycopy'])

        if dummycopy:
            destbasepath = dummydir
        else:
            destbasepath = cfg['mediadirs']['Movies']

        destpath = os.path.join(destbasepath, data['title'])
        origitem = os.path.join(data['path'], data['title'])
        #shutil.move(origitem, destpath)

        if data["filefolder"] == "folder":
            deaddir = data['path']
         #   os.rmdir(deaddir)

        if dummycopy:
            return("Simulated copy.")
        else:
            return("Live copy complete.")
