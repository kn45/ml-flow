# -*- coding=utf-8 -*-
import cPickle
import numpy as np
import os
import sys

"""Common tools for this project.
Utils are defined in this module for sharing.
"""

PROJ_DIR = os.path.split(os.path.realpath(__file__))[0]
RAW_DIR = PROJ_DIR + '/DataTitanic'


def draw_progress(iteration, total, pref='Progress:', suff='',
                  decimals=1, barlen=50):
    """Call in a loop to create terminal progress bar
    """
    formatStr = "{0:." + str(decimals) + "f}"
    pcts = formatStr.format(100 * (iteration / float(total)))
    filledlen = int(round(barlen * iteration / float(total)))
    bar = '█' * filledlen + '-' * (barlen - filledlen)
    out_str = '\r%s |%s| %s%s %s' % (pref, bar, pcts, '%', suff)
    out_str = '\x1b[0;34;40m' + out_str + '\x1b[0m'
    sys.stdout.write(out_str),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


class cat2idx(object):
    """Transform category to global uniq index
    """
    def __init__(self):
        self.cats = {}

    @staticmethod
    def build_dict(ifnames, columns, ofname):
        """ifnames are ',' separated
        fields are ',' separated, from 0. means from ... to
        """
        icats = {}
        cat_idx = 0
        ifnames = ifnames.split(',')
        cols = columns.split(',')
        col_st = int(cols[0])
        col_ed = int(cols[1]) if len(cols) > 1 else -1
        for ifname in ifnames:
            with open(ifname) as f:
                data = map(lambda l: l.strip('\n').split('\t'), f.readlines())
                for fields in data:
                    for idx in xrange(col_st, len(fields) if col_ed < 0 else
                                      col_ed+1):
                        if fields[idx] not in icats and fields[idx] != '':
                            icats[fields[idx]] = cat_idx
                            cat_idx += 1
        with open(ofname, 'w') as fo:
            for key in icats:
                print >> fo, '\t'.join(map(str, [key, icats[key]]))

    def load_dict(self, dfname):
        self.cats = {}
        with open(dfname) as f:
            data = map(lambda l: l.strip('\n').split('\t'), f.readlines())
            for fields in data:
                self.cats[fields[0]] = int(fields[1])

    def cat2idx(self, cat, dic='extern'):
        if cat == '':
            return -1
        if dic == 'extern':
            return self.cats[cat] if cat in self.cats else -1
        if dic == 'auto':
            if cat in self.cats:
                return self.cats[cat]
            else:
                idx = len(self.cats)
                self.cats[cat] = idx
                return idx


if __name__ == '__main__':
    print "PROJ_DIR:\t" + PROJ_DIR
    print "RAW_DIR:\t" + RAW_DIR
    from time import sleep
    for i in range(50):
        sleep(0.05)
        draw_progress(i, 49, pref='Progress:')
