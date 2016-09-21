#!/usr/bin/env python

import sys
import numpy as np
from titanic import *

def gender_encoding(gender):
    gender = str(gender)
    res = ''
    if gender == 'male':
        res = '0'
    if gender == 'female':
        res = '1'
    return np.array([res])

infile = sys.argv[1]
outfile = sys.argv[2]

data = None
with open(infile) as f:
    data = np.array([l.rstrip('\r\n').split('\t') for l in f.readlines()])


fo = open(outfile, 'w')
for line in data:
    gender = line[5]
    gender_vec = gender_encoding(gender)

    print >> fo, \
        '\t'.join(np.hstack([line[:4],
                             gender_vec,
                             line[6:]]))
