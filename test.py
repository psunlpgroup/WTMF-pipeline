import shutil
import os
import sys
import configparser

model_directory = "weiwei"
testset = "sts12"

config = configparser.ConfigParser()
config.read('config.ini')
base_dir = config.get('DEFAULT','basedir')

model_directory = os.path.join(base_dir,"output", model_directory)
test_dir = os.path.join(base_dir,"test", "test", testset)
shutil.copy(os.path.join(model_directory,"model.mat"), os.path.join(base_dir,"test","model.mat"))

os.system("perl " + os.path.join(base_dir,"test","test.pl") + " " + os.path.join(test_dir, "text"))
os.system("python " + os.path.join(base_dir,"test","test_ormf_io.py") + " " + model_directory + " " + test_dir)

os.system("perl "+ os.path.join(base_dir,"test", "bin", "Postprocess", "get_sim.pl") + " " + os.path.join(test_dir, "text.ls") + " " + os.path.join(model_directory, testset) + ".sim")

os.system("python " + os.path.join(base_dir,"test", "correl.py") + " "+ os.path.join(test_dir, "gs") + " " + os.path.join(model_directory, testset) + ".sim")

os.remove(os.path.join(base_dir,"test","model.mat"))
