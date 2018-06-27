#!/usr/bin/env python

'''
    File name: distribution_plot.py
    Description: Testing if data is fit to a theoretical distribution
    Author: Naoufal Nifa
    Date created: 12/11/2017
    Python Version: 2.7
'''

import matplotlib.pyplot as plt
import scipy
import scipy.stats

dist_names = ['gamma', 'beta', 'rayleigh', 'norm', 'pareto']
def drawDistribution(y,dist_names):
    size = np.size(y)
    x = scipy.arange(size)
    h = plt.hist(y, bins=range(48), color='w')

    for dist_name in dist_names:
        dist = getattr(scipy.stats, dist_name)
        param = dist.fit(y)
        pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1]) * size
        plt.plot(pdf_fitted, label=dist_name)
        plt.xlim(0,47)
    plt.legend(loc='upper right')
    plt.show()


# There are 82 implemented distribution functions in SciPy 0.12.0. You can test how some
#  of them fit to your data using their fit() method. For more distributions, use a much bigger 
# set of colors:

# dist_names = [ 'alpha', 'anglit', 'arcsine', 'beta', 'betaprime', 'bradford', 
# 'burr', 'cauchy', 'chi', 'chi2', 'cosine', 'dgamma', 'dweibull', 'erlang', 'expon', 
# 'exponweib', 'exponpow', 'f', 'fatiguelife', 'fisk', 'foldcauchy', 'foldnorm', 'frechet_r', 
# 'frechet_l', 'genlogistic', 'genpareto', 'genexpon', 'genextreme', 'gausshyper', 'gamma', 
# 'gengamma', 'genhalflogistic', 'gilbrat', 'gompertz', 'gumbel_r', 'gumbel_l', 'halfcauchy', 
# 'halflogistic', 'halfnorm', 'hypsecant', 'invgamma', 'invgauss', 'invweibull', 'johnsonsb', 
# 'johnsonsu', 'ksone', 'kstwobign', 'laplace', 'logistic', 'loggamma', 'loglaplace', 'lognorm', 
# 'lomax', 'maxwell', 'mielke', 'nakagami', 'ncx2', 'ncf', 'nct', 'norm', 'pareto', 'pearson3', 
# 'powerlaw', 'powerlognorm', 'powernorm', 'rdist', 'reciprocal', 'rayleigh', 'rice', 'recipinvgauss', 
# 'semicircular', 't', 'triang', 'truncexpon', 'truncnorm', 'tukeylambda', 'uniform', 'vonmises', 
# 'wald', 'weibull_min', 'weibull_max', 'wrapcauchy'] 