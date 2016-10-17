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


def draw_progress(iteration, total, pref='', suff='', decimals=1, barlen=50):
    """Call in a loop to create terminal progress bar
    """
    formatStr = "{0:." + str(decimals) + "f}"
    pcts = formatStr.format(100 * (iteration / float(total)))
    filledlen = int(round(barlen * iteration / float(total)))
    bar = '█' * filledlen + '-' * (barlen - filledlen)
    sys.stdout.write('\r%s |%s| %s%s %s' % (pref, bar, pcts, '%', suff)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


if __name__ == '__main__':
    print "PROJ_DIR:\t" + PROJ_DIR
    print "RAW_DIR:\t" + RAW_DIR
    from time import sleep
    for i in range(50):
        sleep(0.05)
        draw_progress(i, 49, pref='Progress:')
