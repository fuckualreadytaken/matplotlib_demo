#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""

import numpy as np
import matplotlib.pyplot as plt


def box():
    # np.random.seed(100)
    data = np.random.normal(size=1000, loc=0, scale=1)
    plt.boxplot(data, sym='o', whis=1)
    plt.show()


def muti_box():
    data = np.random.normal(size=(1000, 4), loc=0, scale=1)
    labels = 'A', 'B', 'C', 'D'
    plt.boxplot(data, labels=labels)
    plt.show()


if __name__ == "__main__":
    # box()
    muti_box()