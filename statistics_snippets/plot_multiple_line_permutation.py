#!/usr/bin/env python

'''
    File name: plot_multiple_line_permutation.py
    Description: plot multiple lines for permutation samples
    Author: Naoufal Nifa
    Date created: 10/12/2017
    Python Version: 2.7
'''

# related functions: permutation_sample, ecdf

import matplotlib.pyplot as plt

def plot_multiple_line_permutation(data1,data2)
    for _ in range(50):
    # Generate permutation samples
    perm_sample_1, perm_sample_2 = permutation_sample(data1,data2)


    # Compute ECDFs
    x_1, y_1 = ecdf(perm_sample_1)
    x_2, y_2 = ecdf(perm_sample_2)

    # Plot ECDFs of permutation sample
    _ = plt.plot(x_1, y_1, marker='.', linestyle='none',
                 color='red', alpha=0.02)
    _ = plt.plot(x_2, y_2, marker='.', linestyle='none',
                 color='blue', alpha=0.02)

	# Create and plot ECDFs from original data
	x_1, y_1 = ecdf(data1)
	x_2, y_2 = ecdf(data2)
	_ = plt.plot(x_1, y_1, marker='.', linestyle='none', color='red')
	_ = plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue')
	
	# Label axes, set margin, and show plot
	plt.margins(0.02)
	_ = plt.xlabel('XXX')
	_ = plt.ylabel('ECDF')
	plt.show()	