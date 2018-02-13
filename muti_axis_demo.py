#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import matplotlib.pyplot as plt

# for idx, color in enumerate("rgbyck"):
#     # subplot() use to create sub axis pic
#     plt.subplot(320+idx+1, axisbg=color)
# subplot() first parameter is row ,second is col, third is num
plt.subplot(221)  # 第一行的左图
plt.subplot(222)  # 第一行的右图
plt.subplot(212)  # 第二整行
plt.show()

