import os
import shutil
import sys
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
base_dir = config.get('DEFAULT','basedir')

if os.path.isfile(os.path.join(base_dir, "WTMF", "ormf")):
    os.remove(os.path.join(base_dir, "WTMF", "ormf"))

if os.path.isdir(os.path.join(base_dir, "WTMF", "armadillo-9.800.4")):
    shutil.rmtree(os.path.join(base_dir, "WTMF", "armadillo-9.800.4"))

for each in os.listdir(os.path.join(base_dir, "output")):
    #  print(each)
    if os.path.isdir(os.path.join(base_dir, "output", each)):
        print("Removing " + os.path.join(base_dir, "output", each))
        shutil.rmtree(os.path.join(base_dir, "output", each))
