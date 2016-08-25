#!/usr/bin/env python

import sys
from sklearn.cross_validation import StratifiedKFold
from titanic import *


# data_file = 'data_all'
# train_file = 'data_train'
# valid_file = 'data_valid'
data_file = sys.argv[1]
train_file = sys.argv[2]
valid_file = sys.argv[3]

data = None
with open(data_file) as f:
    data = np.array([l.rstrip('\r\n').split('\t') for l in f.readlines()])

X = data[:, 1:]
y = data[:, 0]
valid_ratio = 0.15
skf = StratifiedKFold(y, round(1./valid_ratio))
train_idx, valid_idx = next(iter(skf))
data_train = data[train_idx]
data_valid = data[valid_idx]

with open(train_file, 'w') as fo_train:
    for line in data_train:
        print >> fo_train, '\t'.join(line)
with open(valid_file, 'w') as fo_valid:
    for line in data_valid:
        print >> fo_valid, '\t'.join(line)
