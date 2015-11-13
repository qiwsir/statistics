#!/usr/bin/env python
# coding=utf-8

import numpy as np

def base_average_deviation(arry):
				"""
				Compute the average deviation
				The formal parameter is a one dimensional list.
				"""				
				arry.sort()
				if len(arry)%2==1:
								res = abs(np.array(arry)-arry[len(arry)/2])
				else:
				    res = abs(np.array(arry)-(arry[len(arry)/2]+arry[len(arry)/2-1])/2.0)
				         
				result = 1.0*res.sum()/len(arry)
				return round(result,2)

def base_standard_deviation(arry):
				"""
				Compute the standard deviation
				The formal parameter is a one dimensional list.
				"""
				result = np.std(arry)
				return round(result,2)

def base_variance(arry):
				"""
				Compute the varince
				The formal parameter is a one dimensional list.
				"""
				result = np.var(arry)
				return round(result,2) 

def base_variation_coefficient(arry):
				"""
				Compute the coefficient of variation
				The formal parameter is a one dimensional list.
				"""
				result = 1.0*np.std(arry)/np.mean(arry)
				return '%.2f%%'%(result*100)

def base_interquartile_range(arry):
				"""
				Compute the interquartile range
				The formal parameter is a one dimensional list.
				"""
				arry.sort()
				result = (np.percentile(arry, 75)-np.percentile(arry, 25))/2.0
				return round(result,2)

def base_percentile_range(arry):
				"""
				Compute the percentile range
				The formal parameter is a one dimensional list.
				"""
				result = np.percentile(arry, 90)-np.percentile(arry, 10)
				return result
