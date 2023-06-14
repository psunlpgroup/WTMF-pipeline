import sys
import numpy
import os
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(str(Path.cwd())+'/config.ini')
base_dir = config.get('DEFAULT','basedir')

mat = numpy.random.normal(size=(100,82249))
numpy.savetxt(os.path.join(base_dir,"WTMF","P.txt"), mat, delimiter=',')
print("Randomized vectors created in P.txt")
