import os
import configparser
import pickle
import json

cfg_file = "joe_app.conf"
cfg = ""




def read_config():
    cfg_file = "joe_app.conf"
    with open(cfg_file, "r") as f:
        cfg = f.read()
        #cfg = str(cfg)
    return cfg


def write_complete_config(data):
    with open('joe_app.conf', 'w') as outfile:
        json.dump(data, outfile)
    return data
cfg = read_config()
