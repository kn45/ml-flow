
- GetTsv: 

  Transform label to structured form, while features remain original style.

  - Global pre-processing:

    handle missing value

    abnormal detection

    drop bad data by certain filter

  - Dump data to tab separated <lable, feautures>.

- Split

  Split data to training, validation and testing set.

  - Random sampling for regression task.
  - Stratified sampling for classification task.
  - For cross-validation, use the combination of training and validation set.


-   Feature:

    Prepare feature of each data instance.

    - Encode categorical feature.
    - Proc text features to strutured form.

-   Training&Testing:

    - Resampling for unbanlanced data.
    - Use validation set or cross-validation to tuning model parameters.
    - Evaluating metrics on testing set is the benchmark to compare models.

-   Predicting:

      Repeat all the procedure done to the traning set (using possible pickled modules) and apply model to generate submission file (predicting).

