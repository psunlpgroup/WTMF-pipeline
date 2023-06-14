import shutil
import os
import sys
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
base_directory = config.get('DEFAULT','basedir')

corpus_directory = os.path.join(base_directory, "models", "weiwei")

output_directory = os.path.join(base_directory, "output", "weiwei")


corpus_file = None
for f in os.listdir(corpus_directory):
    if f[-4:] == ".txt":
        if corpus_file is None:
            corpus_file = os.path.join(corpus_directory, f)

        else:
            print("Multiple *.txt files found in the corpus directory. Expected only one!")
            sys.exit()

print("Using the " + corpus_file + " as the input corpus")
ind_file = None
train_script = os.path.join(base_directory, "preprocess", "bin", "train.pl")
os.system("perl " + train_script + " " + corpus_directory + " " + corpus_file)
if os.path.isdir(output_directory):
    shutil.rmtree(output_directory)

os.makedirs(output_directory)
for f in os.listdir(corpus_directory):
    print(f)

    if f[-4:] != ".txt":
        if f[-4:] == ".ind":
            ind_file = os.path.join(base_directory, "WTMF", f)
            shutil.copy(os.path.join(corpus_directory, f), ind_file)

        shutil.move(os.path.join(corpus_directory, f), os.path.join(output_directory, f))
if os.path.isfile(os.path.join(base_directory, "WTMF", "P.txt")):
    os.remove(os.path.join(base_directory, "WTMF", "P.txt"))

make_mat = os.path.join(base_directory, "WTMF", 'script', 'initmat.py')

os.system("python3 " + make_mat)

if not os.path.isdir(os.path.join(base_directory, "WTMF", "armadillo-9.800.4")):
    if not os.path.isfile(os.path.join(base_directory, "WTMF", "armadillo-9.800.4.tar.xz")):
        print("Missing Armadillo folder and tar file")
        sys.exit()
    else:
        os.system("tar -xvf " + os.path.join(base_directory, "WTMF",
                                             "armadillo-9.800.4.tar.xz") + " --directory " + os.path.join(base_directory,
                                                                                                          "WTMF"))
        print("Armadillo extracted from tar")
#    sys.exit()


# if not os.path.isfile(os.path.join("/storage/home/mfs6614/WTMF/WTMF-pipeline/WTMF", "ormf")):
os.system("cd " + os.path.join(base_directory, "WTMF") + " && make")
# print("%%%%%")
os.system("cd " + os.path.join(base_directory, "WTMF") + " && ./ormf")
# print("$$$$$")
os.system(
    "python3 " + os.path.join(base_directory, "WTMF", "script", "txttomat.py") + " " + os.path.join(base_directory, "WTMF",
                                                                                                 "output.txt"))
# print("#####")
shutil.move(os.path.join(base_directory, "WTMF", "output.txt.mat"), os.path.join(output_directory, "model.mat"))
os.remove(os.path.join(base_directory, "WTMF", "P.txt"))
os.remove(os.path.join(base_directory, "WTMF", "output.txt"))
os.remove(ind_file)
print("model.mat stored in the output directory")
