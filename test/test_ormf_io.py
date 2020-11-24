"""
test_ormf pipeline for converting a list of token indices into a list of sentence vectors
Input: *.ind from test.pl, *.mat from training ormf  
Output: *.ls 
"""
from test_ormf import getVectorization
import sys
import os 

model_path = "output/weiwei/model.mat"  # e.g. models/train100/model.mat
text_ind_path = "test/test/sts12/text.ind"  # e.g. /Users/Serena/wtmf/test/sts12/text.ind

if len(sys.argv) == 3:
  model_path = os.path.join(sys.argv[1], "model.mat")
  text_ind_path = os.path.join(sys.argv[2],"text.ind")

out_ls_path= text_ind_path[:text_ind_path.rfind(".")]+".ls"
vecs = getVectorization(text_ind_path, model_path)

with open(out_ls_path,'w') as f:
	for n,vec in enumerate(vecs):
		f.write(str(vec).replace("[","").replace("]","")+'\n')

