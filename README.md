# WTMF-pipeline
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
