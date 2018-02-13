#! /usr/bin/env python
# -*-coding:utf-8-*-

"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
fracs = [15, 45, 10, 37]
explode = [0, 0.1, 0, 0]
# pie()
# First parameter is data,second is labels,hum,you know
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, autopct="%.0f%%", explode=explode, shadow=True)
plt.show()
