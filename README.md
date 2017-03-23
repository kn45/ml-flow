# MLFlow

A simple machine learning procedure for general supervised tasks. It can be used to setup a fast workspace for task like data competition. Commonly-used steps are stated and carefully arranged such as preprocessing, data split, abstracting features and predicting.

https://github.com/kn45/mlflow

## Procedure


- GetTsv:  
  Transform label to structured form, while features remain original style.  
  - Global pre-processing:
    handle missing value
    abnormal detection
    drop bad data by certain filter
  - Dump data to tab separated <lable, feautures>.

- Split:  
  Split data to training, validation and testing set.  
  - Random sampling for regression task.
  - Stratified sampling for classification task.
  - For cross-validation, use the combination of training and validation set.


- Feature:  
  Prepare feature of each data instance.  
  - Encode categorical feature.
  - Proc text features to strutured form.
  - Nomalizatoin for some algorithms.

- Training & Testing:  
  - Resampling for unbanlanced data.
  - Use validation set or cross-validation to tuning model parameters.
  - Evaluating metrics on testing set is the benchmark to compare models.

- Predicting:  
  Repeat all the procedure done to the traning set (using possible pickled modules) and apply model to generate submission file (predicting).

## Tips

- Features are dependent with the model and they two act as *solution*(pair of feature and model) so we need to create workspace for each *solution*. *Solution* takes unfeatured data as input and provide end2end prediction.
- Training, testing set should be generated at the very beginning before feature engineering and remain the same for each possible solutions so that solutions would be comparable and evaluated by the same rule. That's why the training and testing directory are public and independent with solutions. 
- Predicting set of course is same for all solutions but its features and results are different solution by solution.
- Is it necessary to separate featuring process and predicting process for predicting?

## Utils

- put common utils used in the project to utils directory for instance mlfutil.py.
