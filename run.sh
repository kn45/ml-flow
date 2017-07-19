#!/bin/bash

H_DIR=`pwd -P`

bash 1_GetTsv.sh
bash 2_Split.sh
cd model_example
bash 3_Feature.sh
bash 4_Train.sh
bash 5_Pred.sh
