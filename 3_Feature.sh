#!/bin/bash

# Build feature using various ways from tsv file
# tsv -> feature

data_trnvld=data_train/data_trnvld.tsv
data_train=data_train/data_train.tsv
data_valid=data_train/data_valid.tsv
data_test=data_test/data_test.tsv

feat_trnvld=data_train/trnvld_feature.tsv
feat_train=data_train/train_feature.tsv
feat_valid=data_train/valid_feature.tsv
feat_test=data_test/test_feature.tsv

python 3_Feature.py $data_train $feat_train 2> log.feature
python 3_Feature.py $data_valid $feat_valid 2>> log.feature

# For cross-validation
#python 3_Feature.py $data_trnvld $feat_trnvld 2> log.feature

python 3_Feature.py $data_test $feat_test 2>> log.feature
