#!/usr/bin/env python

'''
    File name: ecdf.py
    Description: Compute ECDF for a one-dimensional array of measurements
    Author: Naoufal Nifa
    Date created: 06/12/2017
    Python Version: 2.7
'''

import numpy as np

def ecdf(data):

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y