#!/usr/bin/env python3

"""Displays the laserscan topic as a bar graph.

An improvement from dataFilterTH.py. 
Prints out the laserscan topic in a formative 
style manner that revolves around averages.

Attributes:
    None
"""

import load_laserscan
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import time

"""Displays the bar plot

Sets up and displays the bar plot. Update the bar plot 
accoding to the laserscan_datatxt.

Works inconjunction with load_laserscan.py

Args:
    txt (str): the string containing the address for the laserscan data file

"""
def print_graph(txt):
    plt.ion()
    palette = list(reversed(sns.color_palette("seismic", 2).as_hex()))

    # Figure Dimentions
    fig = plt.figure(figsize=(15,10)) #figsize=(8,9)
    plt.style.use("seaborn")
    plt.title("Ground Reasoning Project:", color=("blue"))
    plt.xlabel("LaserScan Data (Degrees)")
    plt.ylabel("Distance (m)")

    # Creating the label
    ranges = []
    lst_default = []
    for i in range(-30, 31, 3):
        if i != 0:
          ranges.append(str(i))
          lst_default.append(0.0)

    while True:
        # Read from txt the data
        lst= lst_default
        load_laserscan.transf_laserdata()
        pullData = open(txt,"r")
        data = pullData.read().split(',')
        if len(data) == 20:
            lst = list(map(float, data))
        pullData.close()

        # Assigns the values to corresponding bar
        rect = plt.bar(ranges, lst, color=palette)

        # Draw updated values
        fig.canvas.draw()

        # Run GUI event
        fig.canvas.flush_events()

        # Removes all bar
        rect.remove()
        time.sleep(0.1)
        

if __name__ == '__main__':
    print_graph("/home/rhodes/groundReasonTeam_ws/src/comp370_project/laserscan_data.txt")