
- GetTsv: 

  Transform label to structured form, while features remain original style.

  - Global pre-processing:

    handle missing value

    abnormal detection

  - Dump data to tab separated <lable, feautures>.

- FilSplit

  Split data to training & validation set

  - Filter data by certain rules.


  - Split data to training & validation set using stratified sampling.

- PreProc:

  - Encode categorical feature.
  - Proc text features to strutured form.

- Training:

  Resampling for unbanlanced data.?

- Test:

  Repeat all the procedure done to the traning set (using pickled modules) and apply model to generate submission file (predicting).

