import shutil
import os
import sys

model_directory = "weiwei"
testset = "sts12"

if len(sys.argv) == 2:
  model_directory = sys.argv[1]

if len(sys.argv) == 3:
  model_directory = sys.argv[1]
  testset = sys.argv[2]

model_directory = os.path.join("output", model_directory)
test_dir = os.path.join("test", "test", testset)
shutil.copy(os.path.join(model_directory,"model.mat"), os.path.join("test","model.mat"))

os.system("perl " + os.path.join("test","test.pl") + " " + os.path.join(test_dir, "text"))
os.system("python " + os.path.join("test","test_ormf_io.py") + " " + model_directory + " " + test_dir)

os.system("perl "+ os.path.join("test", "bin", "Postprocess", "get_sim.pl") + " " + os.path.join(test_dir, "text.ls") + " " + os.path.join(model_directory, testset) + ".sim")

os.system("python " + os.path.join("test", "correl.py") + " "+ os.path.join(test_dir, "gs") + " " + os.path.join(model_directory, testset) + ".sim")

os.remove(os.path.join("test","model.mat"))
