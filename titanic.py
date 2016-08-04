import cPickle
from sklearn.cross_validation import StratifiedKFold
import numpy as np
import os


PROJ_DIR = os.path.split(os.path.realpath(__file__))[0]
RAW_DIR = PROJ_DIR + '/DataTitanic'

if __name__ == '__main__':
    print "PROJ_DIR:\t" + PROJ_DIR
    print "RAW_DIR:\t" + RAW_DIR
