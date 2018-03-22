#! /usr/bin/env python
# -*-coding:utf-8-*-

"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 30)


def random_():
    n = 5
    a = []
    while n > 0:
        a.append(int(np.random.rand() * 30))
        n -= 1

    return a


a1 = random_()
a2 = random_()
print(a1)
print(a2)