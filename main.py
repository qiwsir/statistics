# /usr/bin/env python
# coding:utf-8

import numpy as np
import intenquanl 

import random
#b = np.random.randint(100, size=(1, 50))
b = [random.randint(1, 100) for i in range(500)]
w = np.arange(len(b))
#print intenquanl.base_weig_ave(b, w)
print intenquanl.base_mode(b)
