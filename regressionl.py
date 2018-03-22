#! /usr/bin/env python
# -*-coding:utf-8-*-

"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20)
y = []
flag = True
for i in x:
    if flag:
        y.append(i + np.random.rand() * 5)
        flag = False
    else:
        y.append(i - np.random.rand() * 5)
        flag = True

plt.scatter(x, y)
plt.plot(x, x, color='r')
plt.show()
