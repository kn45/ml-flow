#!/usr/bin/env python2.7

import cPickle
import logging
import numpy as np
import sys
import xgboost as xgb
from mlfutil import *
from operator import itemgetter

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]: %(message)s")

model_file = 'gbt_model.pkl'


def train():
    logging.info('loading training data')
    trainf = open('data_train/train_feature.tsv')
    data_train = np.array(
        map(fill_missing_value,
            [l.rstrip().split('\t') for l in trainf.readlines()]),
        dtype='float64')

    trainf.close()
    data_train_dmat = xgb.DMatrix(data_train[:, 1:], data_train[:, 0], -999.0)
    del data_train
    validf = open('data_train/valid_feature.tsv')
    data_valid = np.array(
        map(fill_missing_value,
            [l.rstrip().split('\t') for l in validf.readlines()]),
        dtype='float64')
    data_valid_dmat = xgb.DMatrix(data_valid[:, 1:], data_valid[:, 0], -999.0)
    del data_valid

    logging.info('start training')
    bst_params = {
        'nthread': 4,
        'silent': 1,
        'eta': 0.1,
        'eval_metric': ['auc', 'error'],
        'max_depth': 6,
        'subsample': 1.0,
        'colsample_bytree': 1.0,
        'objective': 'binary:logistic',
        'lambda': 1.0
        }
    train_params = {
        'params': bst_params,
        'dtrain': data_train_dmat,
        'num_boost_round': 2000,  # max round
        'evals': [(data_train_dmat, 'train'), (data_valid_dmat, 'valid_0')],
        'maximize': False,
        #'early_stopping_rounds': 300,
        'verbose_eval': True
        }
    mdl_bst = xgb.train(**train_params)

    logging.info('Saving model')
    # not use save_model mothod because it cannot dump best_iteration etc.
    cPickle.dump(mdl_bst, open(model_file, 'wb'))

    feat_imp = mdl_bst.get_score(importance_type='gain').items()
    print sorted(feat_imp, key=itemgetter(1), reverse=True)[0:10]


def test():
    testf = open('data_train/valid_feature.tsv')
    data_test = np.array(
        map(fill_missing_value,
            [l.rstrip().split('\t') for l in testf.readlines()]),
        dtype='float64')
    x_test = data_test[:, 1:]
    y_test = data_test[:, 0]

    # init gbt
    mdl_bst = cPickle.load(open(model_file, 'rb'))
    mdl_bst.set_param('nthread', 1)
    mdl_bst.set_param('eval_metric', 'auc')
    mdl_bst.set_param('eval_metric', 'error')  # add new metric

    test_res = mdl_bst.eval_set([(xgb.DMatrix(x_test, y_test), 'test_0')])
    print test_res


if __name__ == '__main__':
    train()
    test()
