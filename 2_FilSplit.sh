#!/bin/bash

data_raw=DataTitanic/train.csv
data_all=data_all/data_all.tsv
data_train=data_train/data_train.tsv
data_valid=data_valid/data_valid.tsv

python 2_FilSplit.py $data_all $data_train $data_valid
