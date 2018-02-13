#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x ** 2)

# create plot object and set the pic size
plt.figure(figsize=(8, 4))
"""
plot:
    linewidth to set line width
    label(name of curve) = '$sin(x)$' + plt.legend() to show something
    
    b = blue
    -- = dotted line
    b-- = blue dotted line
"""
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=10)
plt.plot(x, z, "b--", label="$cos(x^2)$")
# set x axis name
plt.xlabel("Time(s)")
# set y axis name
plt.ylabel("Volt")
# set pic title
plt.title("PyPlot First Example")
# set the range of y axis
plt.ylim(-1.2, 1.2)
# show plot label, such as "$sin(x)$"
plt.legend()
# show means show, you know? asshole?
plt.show()
