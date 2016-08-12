
- Raw2Tsv: 

  - Transform label to structured form, while features remain original style.

    Handle missing value.

    Abnormal detection.

  - Dump transformation:

    From training data to <lable, feautures>.

    From predicting data to <features>.

- Split

  Split training data to training and validation set using stratified sampling.

- PreProc:

  - Encode categorical feature.
  - Proc text features to strutured form.

- Training:

  Resampling for unbanlanced data.?

- Test:

  Repeat all the procedure done to the traning set (using pickled modules) and apply model to generate submission file (predicting).

