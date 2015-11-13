# /usr/bin/env python
# coding:utf-8

import basestat 


a = [1, 3, 5, 6]
b= range(1000000)
c = 10000
arry = [1, 2, 3, 4, 5, 6, 9]
d = [[1,2],[3,4],[5,6]]
e = [1,2,3,4,5,6]
li = [21,44,2,45,33,4,3,67]
f = [11, 37, 2, 37, 2, 45, 99, 37]
print basestat.base_average(a)
print basestat.base_average(b)
print basestat.base_sqrt(c)
print basestat.base_geom_mean(arry)
print basestat.base_weig_ave(d)
print basestat.base_harmo_ave(e)
print basestat.base_median(li)
print basestat.base_mode(f)   
