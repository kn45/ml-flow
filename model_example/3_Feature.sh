#!/bin/bash

# Build feature using various ways from tsv file
# tsv -> feature

data_trnvld=../data_train/data_trnvld.tsv
data_train=../data_train/data_train.tsv
data_valid=../data_train/data_valid.tsv
data_test=../data_test/data_test.tsv

feat_trnvld=feat_train/trnvld_feature.tsv
feat_train=feat_train/train_feature.tsv
feat_valid=feat_train/valid_feature.tsv
feat_test=feat_test/test_feature.tsv

python 3_Feature.py $data_train $feat_train
python 3_Feature.py $data_valid $feat_valid

# For cross-validation
#python 3_Feature.py $data_trnvld $feat_trnvld

python 3_Feature.py $data_test $feat_test
