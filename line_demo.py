#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


def method1():
    # Use figsize to set pic size.
    plt.figure(figsize=(20, 8), dpi=80)
    x = np.linspace(-10, 10, 5)
    y = np.sin(x)
    # Plot x asis
    # xticks(_x, _label)
    plt.xticks(x)
    # plot()
    # First parameter is x coordinate
    # Second is y coordinate
    plt.plot(x, y)
    plt.show()
    # Save,
    # plt.savefig("./f.png")


def temperature_change_with_time():
    # Windows and linux set font
    # font = {'family': 'NSimSun',
    #         'weight': 'bold',
    #         'size': 15}
    # plt.rc("font", **font)

    # my_font = font_manager.FontProperties(fname=r"E:\Program Files (x86)\font\msyh.ttc", size=12)
    plt.figure(figsize=(20, 10), dpi=80)
    x = range(120)
    y = [random.randint(28, 35) for i in range(120)]
    _xlabel = ["10点{0}分".format(i) for i in range(60)]
    _xlabel += ["11点{0}分".format(i) for i in range(60)]
    plt.xticks(list(x)[::3], _xlabel[::3], rotation=270, fontproperties="SimHei", size=15)
    # Description of figure
    plt.xlabel("时间", fontproperties="SimHei", size=15)
    plt.ylabel("温度", fontproperties="SimHei", size=15)
    plt.title("温度随时间的变化折线图", fontproperties="SimHei", size=15)
    plt.plot(x, y)
    plt.show()


def method2():
    # About date line chart
    # plot()
    # First parameter is x coordinate(date)
    # Second is y coordinate
    # Third is style
    plt.plot_date(x, y, linestyle='-')


def practice():
    my_font = font_manager.FontProperties(fname=r"E:\Program Files (x86)\font\msyh.ttc", size=12)
    x = range(11, 31)
    y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(x, y1, label="自己", color="orange", linestyle=":")
    plt.plot(x, y2, label="同桌", color="cyan", linestyle="--")
    # Scale set
    plt.xticks(x, ["{0}岁".format(i) for i in x], fontproperties="SimHei")
    plt.yticks(range(8), ["{0}个".format(i) for i in range(8)], fontproperties="SimHei")

    # Description set
    plt.xlabel("年龄", fontproperties="SimHei", fontsize=15)
    plt.ylabel("个数", fontproperties="SimHei", fontsize=15)
    plt.title("练习", fontproperties="SimHei", fontsize=15)

    # plot grid
    plt.grid(alpha=0.4)
    plt.legend(prop=my_font, loc="upper left")
    plt.show()


if __name__ == "__main__":
    practice()
