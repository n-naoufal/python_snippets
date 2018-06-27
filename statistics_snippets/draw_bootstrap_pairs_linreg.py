#!/usr/bin/env python

'''
    File name: draw_bootstrap_pairs_linreg.py
    Description: perform pairs bootstrap on a set of x,y data.
    Author: Naoufal Nifa
    Date created: 06/12/2017
    Python Version: 2.7
'''

import numpy as np


def draw_bootstrap_pairs_linreg(x, y, size=1):

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds,size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)

    return bs_slope_reps, bs_intercept_reps