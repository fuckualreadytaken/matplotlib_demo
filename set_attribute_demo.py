#! /usr/bin/env python
# -*-coding:utf-8-*-
"""
Author: ProofZ
Date: Do not tell you,huh
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
# This plot() return a line2D object
line, = plt.plot(x, x*x)
# Set antialiase
line.set_antialiased(False)
# This plot() return a line2D object list
lines = plt.plot(x, np.sin(x), x, np.cos(x))
# Use by setp()o set some properties
plt.setp(lines, color="r", linewidth=2.0)
# Print the line's width
print(line.get_linewidth())
# Print the first line's color
print(plt.getp(lines[0], "color"))
# Print all the properties of lines[1]
print(plt.getp(lines[1]))
# gcf() to get figure object
f = plt.gcf()
# Figure object has a property named axes, it is a list of AxesSubplot object.
# We can also use plt.gca() get the property.
plt.getp(f, "axes")
plt.gca()
# Get all the object of the figure
alllines = plt.getp(plt.gca(), "lines")
plt.show()