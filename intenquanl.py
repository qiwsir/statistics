#!/usr/bin/env python
# coding=utf-8

import numpy as np
from scipy import stats

def base_average(arry):
    """
    This is a function of the average
    The formal parameter is a one dimensional list.
    The return value is the average
    """
    if len(arry):
        r_sum = sum(arry)
        result = r_sum*1.0 / len(arry)   
    else:
        result = 0
    return result


def base_geom_mean(arry):
    """
    This is a function of geometric mean.
    The formal parameter is a one dimensional list.
    The return value is the geometric average of the list
    ---
    def base_geom_mean2(arry):
    import operator
    if 0 in arry:
        arry.remove(0)
    return (reduce(operator.mul, arry)) ** (1.0 / len(arry))
    ---
    """
    return stats.mstats.gmean(arry)

#####
def base_weig_ave(arry,y):
    """
    This is a function of weighted average.
    The formal parameter is a two dimensional list.
    The return value is the weighted average of the list
    
    def base_weig_ave2(value, weight):
				numerator = sum(value[i] * weight[i] for i in range(len(value)))
				divisor =  sum(weight[i] for i in range(len(value)))
				return (1.0*numerator / divisor) if divisor != 0 else None 
				---
				>>>%timeit base_weig_ave(a,b)
    >>>1000 loops, best of 3: 1.56 ms per loop
    >>>%timeit base_weig_ave2(a,b)
    >>>100 loops, best of 3: 4 ms per loop
				---   
    """
    result = np.average(arry, weights=y)
    return result
    


def base_harmo_ave(arry):
    """
    This is a function of harmonic mean.
    The formal parameter is a one dimensional list.
    The return value is the harmonic mean of the list.
    """
    """
    res = np.array(arry)
    Sum=(1.0/res).sum()
    result = 1/(1.0/len(arry)*Sum)
    return result
    """
    result = stats.hmean(arry)
    return round(result,2)

def base_median(arry):
    """
    This is a function of median.
    The formal parameter is a one dimensional list.
    The return value is the median of the list
    ---
    >>>a = list(randn(10000))
    >>>%timeit base_median(a)
    1000 loops, best of 3: 1.33 ms per loop

    ---
    >>>a = list(randn(10000))
    >>>%timeit np.median(a)
    1000 loops, best of 3: 852 µs per loop
    """
    result = np.median(arry)
    return result

def base_mode(arry):
    """
    This is a function of mode.
    The formal parameter is a one dimensional list.
    The return value are the mode and the frequency
    """   
    result= stats.mode(arry)
    return result
