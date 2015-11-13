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
#####
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
    res = np.array(arry)
    Sum=(1.0/res).sum()
    result = 1/(1.0/len(arry)*Sum)
    return result

def base_median(l):
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
    """
    flag = True
    for i in range(len(l)-1, 0, -1):
        if flag:             
            flag = False
            for j in range(i):
                if l[j] > l[j + 1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    flag = True
        else:
            break
    if len(l)%2==1:
        result =l[len(l)/2+1]
    else:
        result = 1.0*(l[len(l)/2+1]+l[len(l)/2])/2
    return result
    ---
    
    a = list(randn(10000))
    >>>%timeit base_median(a)
    1000 loops, best of 3: 946 µs per loop

    
    """
    result = np.median(l)
    return result

def base_mode(arry):
    """
    This is a function of mode.
    The formal parameter is a one dimensional list.
    The return value are the mode and the frequency
    """
    list_num = []
    dict_num ={}
    for item in arry:
         if dict_num.has_key(item):  
             dict_num[item] += 1
         else:
             dict_num.setdefault(item,1)   
             pass
    
    top_value = 0
    for valus in dict_num.itervalues():
        if valus> top_value:
             top_value = valus
             pass
    the_pop_num = 0
    the_pop_num_count = 0
    for keys,values in dict_num.iteritems():
         if values == top_value:
             the_pop_num = keys
             the_pop_num_count = values
             return the_pop_num, the_pop_num_count         
