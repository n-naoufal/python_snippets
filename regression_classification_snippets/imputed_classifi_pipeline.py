#!/usr/bin/env python

'''
    File name: imputed_classifi_pipeline.py
    Description: Design an imputed classification pipeline 
    Author: Naoufal Nifa
    Date created: 03/08/2017
    Python Version: 2.7
'''
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn import datasets

# Load sklearn digits dataset
digits = datasets.load_digits()
X = digits.data
y = digits.target
n_samples = X.shape[0]
n_features = X.shape[1]

# Add missing values in 25% of the lines
rng = np.random.RandomState(0)
missing_rate = 0.25
n_missing_samples = int(np.floor(n_samples * missing_rate))
missing_samples = np.hstack((np.zeros(n_samples - n_missing_samples,
                   dtype=np.bool), np.ones(n_missing_samples, dtype=np.bool)))
rng.shuffle(missing_samples)
missing_features = rng.randint(0, n_features, n_missing_samples)

# Estimate the score without the lines containing missing values
X = X[~missing_samples, :]
y = y[~missing_samples]


# Setup the Imputation transformer: imp
imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp),
        ('SVM', clf)]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train,y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))