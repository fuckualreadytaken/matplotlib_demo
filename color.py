#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh

八种内建颜色：
    b:blue
    r:red
    g: green
    c:cyan
    m:magenta
    y:yellow
    k:black
    w:white
其他颜色表示方法：
    灰色阴影
    html 十六进制
    RGB元组
"""
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(1, 5)
plt.plot(y, color='g')  # 八种内建颜色
plt.plot(y + 1, color='0.5')  # 灰度
plt.plot(y + 2, color='#FF00FF')  # html十六进制
plt.plot(y + 3, color=(0.1, 0.2, 0.3))  # rgb
plt.show()
