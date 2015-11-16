#!/usr/bin/env python
# coding=utf-8

import numpy as np
from scipy import stats

def base_binom_num(x,n0):
    """
    This is a function of the binomial distribution.
    The return value is the probabilty which you want to reach.
    """
    res = stats.binom.pmf(range(n0+1), n0, 1/2.0) 
    a = 0   
    for i in range(n0+1):
        if i <= x:
            a = a +res[i]
    return a
                 
def base_binom_pro(pro,n0):
    """
    This is a function of the binomial distribution.
    The return value is the number which you want to reach.
    """
    res = stats.binom.pmf(range(n0+1), n0, 1/2.0)
    a = 0
    for i in range(n0+1):
        a = a + res[i]
        if a>=pro:   
            return i
        
def base_norm_num(num,m0,std0):
    """
    This is a function of normal distribution.
    The return value is the probabilty which you want to reach.

    """
    
    X = stats.norm(loc=m0, scale=std0)
    result = X.cdf(num)
    return result

def base_norm_pro(pro,m0,std0):
    """
    This is a function of normal distribution.
    The return value is the number which you want to reach.

    """    
    X = stats.norm(loc=m0, scale=std0)   
    t = np.arange((m0-30), (m0+30), 0.01) 
    t = (t[:-1] + t[1:])/2
    
    for i  in t:
        if X.cdf(i)>=pro:
            return  int(i)
            break
