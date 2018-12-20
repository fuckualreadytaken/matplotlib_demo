#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt
import random


def univariate():
    mu = 100
    sigma = 20
    x = mu + sigma * np.random.randn(2000000)
    plt.hist(x, bins=50, color='red', normed=True)
    plt.show()


def bivarite():
    x = np.random.randn(1000) + 2
    y = np.random.randn(1000) + 3
    plt.hist2d(x, y, bins=50)
    plt.show()


def practice():
    x = [random.randint(70, 150) for i in range(250)]
    plt.figure(figsize=(10, 8), dpi=80)
    # Calculate group number
    d = 5
    num_bins = (max(x) - min(x)) // 5
    plt.hist(x, num_bins, normed=True)
    plt.xticks(range(min(x), max(x) + d, d))
    plt.grid()
    plt.show()


if __name__ == "__main__":
    practice()
