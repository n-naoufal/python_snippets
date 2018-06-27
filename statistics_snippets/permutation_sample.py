#!/usr/bin/env python

'''
    File name: permutation_sample.py
    Description: Generate a permutation sample from two data sets
    objective: permutation sampling is a great way to simulate the hypothesis 
    		that two variables have identical probability distributions. 
    Author: Naoufal Nifa
    Date created: 08/12/2017
    Python Version: 2.7
'''

import numpy as np

def permutation_sample(data1, data2):

    # Concatenate the data sets: data
    data = np.concatenate((data1,data2))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]

    return perm_sample_1, perm_sample_2