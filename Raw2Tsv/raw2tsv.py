#!/usr/bin/env python

import sys
sys.path.append('../')
try:
    from titanic import *
except:
    raise

data_in = '../DATA_TITANIC/train.csv'
data_out = 'data_all'


def raw2tsv(line):
    fields = line.rstrip('\r\n').split(',')
    label = fields[1:2]
    features = fields[0:1] + fields[2:]
    return '\t'.join(label + features)


def raw2tsv_test(line):
    fields = line.rstrip('\r\n').split(',')
    features = fields[:]
    yield '\t'.join(features)

with open(data_in) as fi, open(data_out, 'w') as fo:
    fi.next()  # skip col name
    for line in fi:
        print >> fo, raw2tsv(line)

# ====================================================
# Picle functions for re-use
# Pickle this function for testing module use

with open('m_raw2tsv_test', 'wb') as f:
    cPickle.dump(raw2tsv_test, f, -1)
