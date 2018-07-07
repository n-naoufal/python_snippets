#!/usr/bin/env python

'''
    File name: gradient_descent.py
    Description: Performs gradient descent to learn theta
    Author: Naoufal Nifa
    Date created: 05/01/2018
    Python Version: 2.7
'''
from numpy import dot
def gradient_descent(X, y, theta, alpha, num_iter):
    n = y.size  
    for i in range(num_iter):
        y_bis = dot(X, theta)
        theta = theta - ( alpha * (1.0/n) * dot(X.T, y_bis-y) )
    return theta