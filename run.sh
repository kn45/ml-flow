#!/bin/bash

H_DIR=`pwd -P`

bash 1_GetTsv.sh
bash 2_Split.sh
bash 3_Feature.sh
bash 4_Train.sh
bash 5_Pred.sh

