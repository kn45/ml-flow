#!/bin/bash

PROJ_DIR=`pwd -P`
cd $PROJ_DIR/Raw2Tsv
python raw2tsv.py
python split.py

