#!/bin/bash

feat_train=data_train/train_feature.tsv
feat_train_red=data_train/train_feature_red.tsv

# Down-sampling of negative instance
## rate of neg-instance would be preserved
sample_rate=1.0
## backup non-sampled set
cp -f $feat_train $feat_train_red
cat $feat_train_red | awk -v rate=$sample_rate -F'	' 'BEGIN{srand()}{if($1==1||rand()<=rate) print $0}' > $feat_train

python 4_Train.py &> log.train
