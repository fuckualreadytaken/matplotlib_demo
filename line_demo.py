#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt


def method1():
    x = np.linspace(-10, 10,5)
    y = np.sin(x)
    # plot()
    # First parameter is x coordinate
    # Second is y coordinate
    plt.plot(x, y)
    plt.show()


def method2():
    # About date line chart
    # plot()
    # First parameter is x coordinate(date)
    # Second is y coordinate
    # Third is style
    plt.plot_date(x, y, linestyle='-')


if __name__ == "__main__":
    method1()
