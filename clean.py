import os
import shutil
import sys

if os.path.isfile(os.path.join("WTMF","ormf")):
  os.remove(os.path.join("WTMF","ormf"))
  
if os.path.isdir(os.path.join("WTMF","armadillo-9.800.4")):
  shutil.rmtree(os.path.join("WTMF","armadillo-9.800.4"))

for each in os.listdir("output"):
#  print(each)
  if os.path.isdir(os.path.join("output",each)):
    print("Removing "+os.path.join("output",each))
    shutil.rmtree(os.path.join("output",each))