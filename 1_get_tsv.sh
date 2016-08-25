#!/bin/bash

data_raw=DataTitanic/train.csv
data_all=data_all/data_all.tsv
python 1_get_tsv.py $data_raw $data_all
