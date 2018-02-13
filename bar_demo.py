#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""

import numpy as np
import matplotlib.pyplot as plt

N = 5
y = [20, 10, 30, 25, 15]
index = np.arange(N)


def vertical_bar():
    # vertical
    # bar()
    # Left means x
    # Height means y or height
    # Color....
    # Width....
    plt.bar(left=index, height=y, color='r', width=0.5)
    plt.show()


def horizontal_bar1():
    # horizontal
    plt.bar(left=0, bottom=index, width=y, color='red', height=0.5, orientation='horizontal')
    plt.show()


def horizontal_bar2():
    # horizontal2
    plt.barh(left=0, bottom=index, width=y)
    plt.show()

def muti_bar():
    plt.bar(left=index, height=y, width=0.3)
    plt.bar(left=index+0.3, height=y, width=0.3)
    plt.show()


if __name__ == "__main__":
    # vertical_bar()
    # horizontal_bar1()
    muti_bar()
    # horizontal_bar2()