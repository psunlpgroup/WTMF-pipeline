# WTMF-pipeline
## Documentation:

This is the package for running WTMF pipeline. It contains the Python code for a distributional similarity model -- Orthogonal matrix factorization (OrMF), and a perl pipeline that preprocesses the data and uses the OrMF model to extract the latent vectors of short texts.

The OrMF model is an unsupervised dimension reduction algorithm, use the exactly the same information that LSA and LDA exploit, which is word-document co-occurrence, and outperforms LSA and LDA by a large margin (on the sentence similarity data sets).  
It will train a model on a corpus.  For each short text in the test data, it will find a latent K-dimension vector.  Usually a larger K leads to a better performance.  In this package,  the default value of K is K=100.

Please cite these papers if you use this code. 

[1] Weiwei Guo and Mona Diab. 2012. [Modeling Sentences in the Latent Space](https://aclanthology.org/P12-1091/). In Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 864–872, Jeju Island, Korea. Association for Computational Linguistics.

[2] Weiwei Guo, Wei Liu, and Mona Diab. 2014. [Fast Tweet Retrieval with Compact Binary Codes](https://aclanthology.org/C14-1047/). In Proceedings of COLING 2014, the 25th International Conference on Computational Linguistics: Technical Papers, pages 486–496, Dublin, Ireland. Dublin City University and Association for Computational Linguistics.


## How to run on ICS-ACI 
Follow the two steps below if you are running the project on ICS-ACI (The Institute for CyberScience Advanced CyberInfrastructure), Penn State's high-performance research cloud:
1. Upload the project to @submit.aci.ics.psu.edu
2. Load the proper GCC with:
```
module load gcc
``` 
3. Run the following for testing: 
```
python3 test.py
```  
Or run the following for training: 
```
python3 train.py
```  


## How to run locally
1. Make sure your GCC version is after 5.3
2. Make sure the armadillo file (armadillo-9.800.4.tar.xz) gets unzipped

## Additional notes
1. Change the basedir variable in the config.ini to your local project path
2. Change the base_dir variable in the WTMF/ormf.cpp to your local project path
3. Check the line count in the train.txt file is the same as what the program computes
4. Check to see if the word count in the train.txt is the same as the input in the WTMF/script/intimate.py file
5. The results are in a model.mat format file
