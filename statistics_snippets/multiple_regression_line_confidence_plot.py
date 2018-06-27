#!/usr/bin/env python

'''
    File name: multiple_regression_line_confidence_plot.py
    Description: perform pairs bootstrap on a set of x,y data and plot confidence lines
    Author: Naoufal Nifa
    Date created: 06/12/2017
    Python Version: 2.7
'''

# related function: draw_bootstrap_pairs_linreg.py

import numpy as np
import matplotlib.pyplot as plt

def multiple_regression_line_confidence_plot(dataX,dataY,bs_slope_reps,bs_intercept_reps)

	# Generate array of x-values for bootstrap lines: x
	x = np.array([0,100])
	
	# Plot the bootstrap lines
	for i in range(100):
	    _ = plt.plot(x, bs_slope_reps[i]*x + bs_intercept_reps[i],
	                 linewidth=0.5, alpha=0.2, color='red')
	
	# Plot the data
	_ = plt.plot(dataX,dataY,marker='.',linestyle='none')
	
	# Label axes, set the margins, and show the plot
	_ = plt.xlabel('dataX')
	_ = plt.ylabel('dataY')
	plt.margins(0.02)
	plt.show()