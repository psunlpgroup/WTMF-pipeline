# WTMF-pipeline
## Documentation:

This is the package for running PyrEval (which includes a new variant PyrEval+CR). The current package is written in Python 3.6 and is an update of the original PyrEval version [Link](https://github.com/serenayj/PyrEval/) which used PyrEval 2.7. This version comes with many optimizations and other changes to facilitate experiments and parameter tuning.  In particular, many of the recent and ongoing changes facilitate use of PyrEval for real-time assessment of student writing. (Has been used with Python versions up to 3.9 on MAC OS, does not work as well on Windows.)

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
2. Make sure the armadillo file gets unzipped

## Additional notes
1. Change the basedir variable in the config.ini to your local project path
2. Change the base_dir variable in the WTMF/ormf.cpp to your local project path
3. Check the line count in the train.txt file is the same as what the program computes
4. Check to see if the word count in the train.txt is the same as the input in the WTMF/script/intimate.py file
5. The results are in a model.mat format file
