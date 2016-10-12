#!/usr/bin/env python2.7
# -*- coding=utf-8 -*-

import cPickle
import fasttext
import logging
import jieba
import numpy as np
import sys
import xgboost as xgb

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]: %(message)s")

w2v_file = '/data1/qspace/travischen/fasttext/fasttext_cbow.model.bin'
w2v_model = None
model_file = 'gbt_model.reg.pkl'
mdl_bst = None
stop_words = {}  # in unicode
puncs = {}  # in unicode


def title_encoding(title):
    smooth_factor = 3.
    title_u = str(title).decode('utf8')
    segs = jieba.cut(title_u)
    valid_segs = [x for x in segs if x not in stop_words and x not in
                  puncs]
    vec_sent = np.zeros(200)
    word_cnt = 0.  # cnt of word collected in w2v model
    for seg in valid_segs:
        try:
            vec_word = w2v_model[seg]
            vec_sent += vec_word
            word_cnt += 1
        except:
            pass
    if word_cnt > 0:
        vec_sent = vec_sent / (word_cnt + smooth_factor)
    return vec_sent


def pred():
    with open('data_pred/data_pred.tsv') as f:
        pred_data_raw = [l.rstrip('\n') for l in f.readlines()]
    logging.info('prepare feature')
    pred_data_mod = [l for l in pred_data_raw]
    pred_data_feat = np.array([title_encoding(l) for l in pred_data_mod])

    logging.info('start predicting')
    logging.info('best_iteration: ' + str(mdl_bst.best_iteration))
    pred_res = mdl_bst.predict(
        xgb.DMatrix(pred_data_feat),
        ntree_limit=mdl_bst.best_iteration)

    # output prediction result to stdout
    for title, feats, res in zip(pred_data_raw, pred_data_feat, pred_res):
        pred = res
        if sum(feats**2) == 0.:
            pred = 0.
        print '\t'.join([str(pred), title])


def init():
    logging.info('start init')
    global mdl_bst
    global w2v_model

    # init seg
    seg_dir = '/data1/qspace/travischen/segmentation/seg_jieba'
    jieba.load_userdict(seg_dir + '/newdict.dat')
    with open(seg_dir + '/punctuations.dat') as f:
        for line in f:
            puncs[line.rstrip('\r\n').decode('utf8')] = ''

    # init fasttext-w2v
    w2v_model = fasttext.load_model(w2v_file)

    # init gbt
    mdl_bst = cPickle.load(open(model_file, 'rb'))
    mdl_bst.set_param('nthread', 1)

    logging.info('finish init')


if __name__ == '__main__':
    init()
    pred()
