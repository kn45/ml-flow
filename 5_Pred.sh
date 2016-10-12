#!/bin/bash

python 5_Pred.py | sort -t$'\t' -k1,1gr > result_pred.reg

