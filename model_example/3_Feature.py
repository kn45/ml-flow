#!/usr/bin/env python

import sys
import numpy as np
from mlfutil import *

port_encoder = None


def init():
    global port_encoder
    port_encoder = PortEncoder()
    port_encoder.init()


def build_feat():
    infile = sys.argv[1]
    outfile = sys.argv[2]
    fo = open(outfile, 'w')
    data = None
    with open(infile) as f:
        data = np.array([l.rstrip('\r\n').split('\t') for l in f.readlines()])
    data_size = len(data)
    for nr, inst in enumerate(data):
        feats = []
        label = inst[0]
        uid = inst[1]
        pclass = inst[2]  # number
        name = inst[3]  # string
        sex = inst[4]  # cat
        age = inst[5]  # number
        sbisp = inst[6]  # number
        parch = inst[7]  # number
        ticket = inst[8]  # string
        fare = inst[9]  # number
        cabin = inst[10]  # string
        port = inst[11]  # cat

        feats += [pclass]
        feats += sex_encoder(sex)
        feats += [age]
        feats += [sbisp]
        feats += [parch]
        feats += [fare]
        feats += port_encoder.encode(port)

        print >> fo, '\t'.join(map(str, [label] + feats))
        draw_progress(nr, data_size-1)

if __name__ == '__main__':
    init()
    build_feat()
