
- Raw2Tsv: 

  Transform label to structured form, while features remain original style.

  Provide 2 modules, one for transforming training data to <lable, feautures>, the other for predicting data to <features>.

  Split training data to training and validation set using stratified sampling.

- PreProc:

  Proc categorical and text features to strutured form.

- Test:

  Repeat all the procedure done to the traning set (using pickled modules) and apply model to generate submission file (predicting).

