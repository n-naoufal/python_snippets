#!/usr/bin/env python

'''
    File name: sgd.py
    Description: stochastic gradient descent
    Author: Naoufal Nifa
    Date created: 05/01/2018
    Python Version: 2.7
'''

def sgd(func, theta0, alpha, num_iter):

    start_iter = 0
    theta= theta0
    for iter in xrange(start_iter + 1, num_iter + 1):
        _, grad = func(theta)
        theta = theta - (alpha * grad) 
    return theta