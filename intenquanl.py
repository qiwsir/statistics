#!/usr/bin/env python
# coding=utf-8

import numpy as np
import math

def base_average(arry):
    """
    This is a function of the average
    The formal parameter is a one dimensional list.
    The return value is the average
    ---
    r_sum = sum(arry)
    result = r_sum*1.0 / len(arry)   
    >>> a = list(randn(1000000))
    >>>  %timeit base_average(a)
    10 loops, best of 3: 59 ms per loop

    ---
    result = np.mean(arry)
    >>>a = list(randn(1000000))
    >>>%timeit base_average(a)
    10 loops, best of 3: 80 ms per loop
    
    """
    #result = np.mean(arry)
    r_sum = sum(arry)
    result = r_sum*1.0 / len(arry)   
    return result


def base_geom_mean(arry):
     """
     This is a function of geometric mean.
     The formal parameter is a one dimensional list.
     The return value is the geometric average of the list

     ---
     >>>a = list(abs(randn(1000000)))
     >>>%timeit   base_geom_mean(a)
     10 loops, best of 3: 94.3 ms per loop
     
     
     sum =1
     for i in arry:
         sum = sum*i
     result =pow(sum,1.0*1/len(arry))
     return result
     ---
     def operat (x , y):
              return x*y
     return pow(reduce(operat , arry),1.0*1/len(arry))
     
     %run geom_mean.py
     >>>%timeit base_geom_mean(a)
     1 loops, best of 3: 175 ms per loop

     """
     sum =1
     for i in arry:
         sum = sum*i
     result =pow(sum,1.0*1/len(arry))
     return result


def base_weig_ave(x,y):
     """
     This is a function of weighted average.
     The formal parameter is a two dimensional list.
     The return value is the weighted average of the list
     
     sum = 0
     for i in x:
         sum = i*y[1]+sum
     result =1.0*sum/len(y)
     return result
     """
     result = np.average(x,weights=y)
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
