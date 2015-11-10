#!/usr/bin/env python
# coding=utf-8

#import numpy as np
import math

def base_average(arry):
    """
    This is a function of the average
    The formal parameter is a one dimensional list.
    The return value is the average
    """
    #result = np.mean(arry)
    r_sum = sum(arry)
    result = r_sum*1.0 / len(arry)
    return result


def base_sqrt(arry):
     """
     This is square root fuction
     
     """
     res_sqrt = math.sqrt(arry)
     return res_sqrt

def base_geom_mean(arry):
     """
     This is a function of geometric mean.
     The formal parameter is a one dimensional list.
     The return value is the geometric average of the list
     """
     sum =1
     for i in arry:
         sum = sum*i
     result =pow(sum,1.0*1/len(arry))
     return result

def base_weig_ave(arry):
     """
     This is a function of weighted average.
     The formal parameter is a two dimensional list.
     The return value is the weighted average of the list
     """
     sum = 0
     for i in arry:
         sum = i[0]*i[1]+sum
     result =1.0*sum/len(arry)
     return result

def base_harmo_ave(arry):
     """
     This is a function of harmonic mean.
     The formal parameter is a one dimensional list.
     The return value is the harmonic mean of the list.
     """
     sum = 0
     for i in arry:
         sum = 1.0*1/i+sum
     result = 1.0/(1.0*1/len(arry)*sum)
     return result

def base_median(l):
    """
    This is a function of median.
    The formal parameter is a one dimensional list.
    The return value is the median of the list
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
         
