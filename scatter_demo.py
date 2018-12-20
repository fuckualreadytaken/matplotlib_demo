#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

def simple_demo():
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


def practice():
    myfont = font_manager.FontProperties(fname=r"E:\Program Files (x86)\font\msyh.ttc", size=14)
    y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22,
           22, 22, 23]
    y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11,
            13, 12, 13, 6]
    plt.figure(figsize=(20, 8), dpi=80)
    x_3 = range(1, 32)
    x_10 = range(51, 82)
    plt.scatter(x_3, y_3, label="3月")
    plt.scatter(x_10, y_10, label="10月")

    # Scale set
    _x = list(x_3) + list(x_10)
    _xtick_labels = ["3月{0}日".format(i) for i in x_3]
    _xtick_labels += ["10月{0}日".format(i - 50) for i in x_10]
    plt.xticks(_x[::3], _xtick_labels[::3], fontproperties="SimHei", rotation=45)

    # Description set
    plt.xlabel("时间", fontproperties="SimHei")
    plt.ylabel("温度", fontproperties="SimHei")
    plt.title("温度随时间变化图", fontproperties="SimHei")
    plt.legend(prop=myfont, loc="upper left")
    plt.show()


if __name__ == '__main__':
    practice()
