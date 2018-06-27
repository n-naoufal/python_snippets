#!/usr/bin/env python

'''
    File name: pearson_r.py
    Description: Compute Pearson correlation coefficient between two arrays
    Author: Naoufal Nifa
    Date created: 05/12/2017
    Python Version: 2.7
'''
from numpy import corrcoef

def pearson_r(x, y):
    # Compute correlation matrix: corr_mat
    corr_mat = corrcoef(x,y)

    # Return entry [0,1]
    return corr_mat[0,1]