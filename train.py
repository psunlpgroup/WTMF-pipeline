import shutil
import os
import sys

corpus_directory = "weiwei"
output_directory = "weiwei"

if len(sys.argv) == 2:
  corpus_directory = sys.argv[1]
  output_directory = sys.argv[1]
  
corpus_directory = os.path.join("models",corpus_directory)
output_directory = os.path.join("output", output_directory)
corpus_file = None
for f in os.listdir(corpus_directory):
  if f[-4:] == ".txt":
    print(f)
    if corpus_file is None:
      corpus_file = os.path.join(corpus_directory, f)
    else:
      print("Multiple *.txt files found in the corpus directory. Expected only one!")
      sys.exit()

print("Using the "+ corpus_file + " as the input corpus")      
ind_file = None    
train_script = os.path.join("preprocess","bin","train.pl")    
os.system("perl " + train_script + " " +corpus_directory + " " + "corpus_file")
if os.path.isdir(output_directory):
  shutil.rmtree(output_directory)
os.mkdir(output_directory)
for f in os.listdir(corpus_directory):
  if f[-4:] != ".txt":
    if f[-4:] == ".ind":
      ind_file = os.path.join("WTMF",f)
      shutil.copy(os.path.join(corpus_directory,f), ind_file)
      
    shutil.move(os.path.join(corpus_directory,f),os.path.join(output_directory,f))
if os.path.isfile(os.path.join("WTMF","P.txt")):
  os.remove(os.path.join("WTMF","P.txt"))

make_mat = os.path.join('WTMF','script','initmat.py')
os.system("python "+ make_mat)

if not os.path.isdir(os.path.join("WTMF","armadillo-9.800.4")):
  if not os.path.isfile(os.path.join("WTMF","armadillo-9.800.4.tar.xz")):
    print("Missing Armadillo folder and tar file")
    sys.exit()
  else:
    os.system("tar -xvf WTMF/armadillo-9.800.4.tar.xz --directory WTMF/")
    print("Armadillo extracted from tar")
#    sys.exit()
    

if not os.path.isfile(os.path.join("WTMF","ormf")):
  os.system("cd WTMF && make")
os.system("cd WTMF && ./ormf")
os.system("python " + os.path.join("WTMF", "script", "txttomat.py") + " "+os.path.join("WTMF","output.txt"))
shutil.move(os.path.join("WTMF","output.txt.mat"),os.path.join(output_directory,"model.mat"))
os.remove(os.path.join("WTMF","P.txt"))
os.remove(os.path.join("WTMF","output.txt"))
os.remove(ind_file)
print("model.mat stored in the output directory")

