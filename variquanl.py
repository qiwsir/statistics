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
           return round(result,2)

def standard_deviation(arr):
         result = np.std(arr)
         return round(result,2)

def variance(arr):
         result = np.var(arr)
         return round(result,2) 

def variation_coefficient(arr):
         result = 1.0*np.std(arr)/np.mean(arr)
         return '%.2f%%'%(result*100)

def interquartile_range(arr):
         arr.sort()
         result = (arr[len(arr)*3/4]-arr[len(arr)/4])/2.0
         return round(result,2)

def percentile_range(arr):
         arr.sort()
         result = arr[len(arr)*9/10]-arr[len(arr)/10]
         return result
