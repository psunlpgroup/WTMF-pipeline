from scipy.io import savemat
import numpy as n
import sys

infile = sys.argv[1]

p_in = []

with open(infile, 'r') as f:
    f.readline()
    for l in f:
        p_in.append(list(map(float, l.split())))
        # print(p_in)
        # sys.exit()

matout = {
        'P': n.array(p_in).T,
        'dim': 100,
        'lambda': 20,
        'w_m': 0.01,
        'alpha': 0.0001,
        'n_iters': 20
        }

savemat(infile+".mat", matout)
