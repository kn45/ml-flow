#!/usr/bin/env python2.7
# -*- coding=utf-8 -*-

import cPickle
import csv
import logging
import numpy as np
import sys
import xgboost as xgb
from mlfutil import *

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]: %(message)s")

model_file = 'gbt_model.pkl'
mdl_bst = None
port_encoder = None

def data2feat(inst):
    feats = []
    pclass = inst[0]  # number
    name = inst[1]  # string
    sex = inst[2]  # cat
    age = inst[3]  # number
    sbisp = inst[4]  # number
    parch = inst[5]  # number
    ticket = inst[6]  # string
    fare = inst[7]  # number
    cabin = inst[8]  # string
    port = inst [9]  # cat

    feats += [pclass]
    feats += sex_encoder(sex)
    feats += [age]
    feats += [sbisp]
    feats += [parch]
    feats += [fare]
    feats += port_encoder.encode(port)
    return fill_missing_value(feats)

  
def pred():
    # with open('data_pred/data_pred.tsv') as f:
    id_data = None
    with open('data_pred/test.csv') as fp_csv:
        fi = csv.reader(fp_csv)
        fi.next()
        id_data = [x for x in fi]
    pred_data = [x[1:] for x in id_data]
    data_id = [x[0] for x in id_data]
    logging.info('prepare feature')
    pred_data_feat = np.array(map(data2feat, pred_data), dtype='float64')

    logging.info('start predicting')
    logging.info('best_iteration: ' + str(mdl_bst.best_iteration))
    pred_res = mdl_bst.predict(
        xgb.DMatrix(pred_data_feat, missing=-999.0),
        ntree_limit=mdl_bst.best_iteration)

    sbt_res = zip(data_id, [(1 if x>0.5 else 0) for x in pred_res])
    # output prediction result to stdout
    with open('data_pred/sbt.csv', 'w') as sbtf:
        writer = csv.writer(sbtf)
        writer.writerow(['PassengerId', 'Survived'])
        writer.writerows(sbt_res)


def init():
    logging.info('start init')
    global mdl_bst
    global port_encoder

    # init gbt
    mdl_bst = cPickle.load(open(model_file, 'rb'))
    mdl_bst.set_param('nthread', 1)

    # init encoder
    port_encoder = PortEncoder()
    port_encoder.init()

    logging.info('finish init')


if __name__ == '__main__':
    init()
    pred()
