#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt


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


if __name__ == "__main__":
    # univariate()
    bivarite()