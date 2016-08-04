#!/usr/bin/env python

import cPickle

def pred(in_iter):
    for line in enumerate(in_iter):
        res = raw2tbl(line)
        yield res

with open('../RAW2TBL_SP/func_raw2tbl') as f:
    raw2tbl = cPicle.load(f)

with open('../DATA_TITANIC/') as fi, open('pred.csv') as fo:
