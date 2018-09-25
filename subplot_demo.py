#! /usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 100)
fig1 = plt.figure(figsize=(10, 5))
# 121 means: 1 row, 2 col, first zone
sub1 = fig1.add_subplot(121)
sub1.plot(x, x)
sub1.set_title("121")
sub2 = fig1.add_subplot(122)
sub2.plot(x, -x)
sub2.set_title("122")

plt.show()
