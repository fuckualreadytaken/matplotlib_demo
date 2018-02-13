#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt

X = 1000
x = np.random.rand(X)
y = np.random.rand(X)
# scatter()
# s ————>> size
# c ————>> color
# marker
# alpha
plt.scatter(x, y, s=20, c="r", marker='o', alpha="0.5")
plt.show()
