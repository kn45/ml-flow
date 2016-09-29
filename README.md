
- GetTsv: 

  Transform label to structured form, while features remain original style.

  - Global pre-processing:

    handle missing value

    abnormal detection

    drop bad data by certain filter

  - Dump data to tab separated <lable, feautures>.

- Split

  Split data to training, validation and testing set

  - Random sampling for regression task.
  - Stratified sampling for classification task.
  - For cross validation, use the combination of training and validation set.


-   PreProc:

    - Encode categorical feature.
    - Proc text features to strutured form.

-   Training:

    - Resampling for unbanlanced data.
    - Split data into real-training set & validation set.

-   Test:

    Repeat all the procedure done to the traning set (using pickled modules) and apply model to generate submission file (predicting).

