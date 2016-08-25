#!/usr/bin/env python

import sys
from titanic import *

data_in = sys.argv[1]
data_out = sys.argv[2]


def raw2tsv(line):
    fields = line.rstrip('\r\n').split(',')
    label = fields[1:2]
    features = fields[0:1] + fields[2:]
    return '\t'.join(label + features)


with open(data_in) as fi, open(data_out, 'w') as fo:
    fi.next()  # skip col name
    for line in fi:
        print >> fo, raw2tsv(line)

# ====================================================
# Picle functions for re-use
# Pickle this function for testing module use

# def raw2tsv_test(line):
#     fields = line.rstrip('\r\n').split(',')
#     features = fields[:]
#     yield '\t'.join(features)


# with open('m_raw2tsv_test', 'wb') as f:
#     cPickle.dump(raw2tsv_test, f, -1)
