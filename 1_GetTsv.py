#!/usr/bin/env python

import csv
import sys
from titanic import *

data_in = sys.argv[1]
data_out = sys.argv[2]


def raw2tsv(fields):
    label = fields[1:2]
    features = fields[0:1] + fields[2:]
    return '\t'.join(label + features)

with open(data_in) as fi_csv, open(data_out, 'w') as fo:
    fi = csv.reader(fi_csv)
    fi.next()  # skip col name
    for fields in fi:
        print >> fo, raw2tsv(fields)
