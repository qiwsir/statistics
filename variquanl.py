#!/usr/bin/env python
# coding=utf-8

import numpy as np

def average_deviation(arr):
         
           arr.sort()
           if len(arr)%2==1:
               res = abs(np.array(arr)-arr[len(arr)/2])
           else:
               res = abs(np.array(arr)-(arr[len(arr)/2]+arr[len(arr)/2-1])/2.0)
                    
           result = 1.0*res.sum()/len(arr)
           return result

def standard_deviation(arr):
         result = np.std(arr)
         return result

def variance(arr):
         result = np.var(arr)
         return result

def variation_coefficient(arr):
         result = 1.0*np.std(arr)/np.mean(arr)
         return '%.2f%%'%(result*100)