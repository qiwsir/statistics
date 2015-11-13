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
    """
    return stats.mstats.gmean(arry)

def base_geom_mean2(arry):
    import operator
    if 0 in arry:
        arry.remove(0)
    return (reduce(operator.mul, arry)) ** (1.0 / len(arry))

def base_weig_ave(arry,y):
    """
    This is a function of weighted average.
    The formal parameter is a two dimensional list.
    The return value is the weighted average of the list
    """
    result = np.average(arry, weights=y)
    return result
    


def base_harmo_ave(arry):
    """
    This is a function of harmonic mean.
    The formal parameter is a one dimensional list.
    The return value is the harmonic mean of the list.
    """
    result = stats.hmean(arry)
    return round(result,2)

def base_median(arry):
    """
    This is a function of median.
    The formal parameter is a one dimensional list.
    The return value is the median of the list
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
