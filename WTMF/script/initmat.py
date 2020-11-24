import numpy
import os

mat = numpy.random.normal(size=(100,81847))
numpy.savetxt(os.path.join("WTMF","P.txt"), mat, delimiter=',')
print("Randomized vectors created in P.txt")