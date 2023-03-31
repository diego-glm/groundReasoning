#!/usr/bin/env python3

"""
Prints the LaserScan Data as a bargraph using matplotlib and seaborn
"""

import load_laserscan
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import time

"""
Displays an updated bar plot via laserscan data

Works with load_laserscan.py

Args:
    txt (str): the string containing the address for the laserscan data file
"""
def print_graph(txt):
    plt.ion() #interactive mode on
    palette = list(reversed(sns.color_palette("seismic", 2).as_hex())) #color palette selection

    # Figure Details and Labels
    fig = plt.figure(figsize=(15,10)) #width and height in inches
    plt.style.use("seaborn")
    plt.title("Ground Reasoning Project:", color=("blue"))
    plt.xlabel("LaserScan Data (Degrees)")
    plt.ylabel("Distance (m)")

    # Initialize arrays for printing
    ranges = []
    lst_default = []
    for i in range(-30, 31, 3): # I dont understand what this for loop is doing or why it has such specific parameters
        if i != 0:
          ranges.append(str(i))
          lst_default.append(0.0) # I dont understand why we are appending 0.0 here

    while True:
        # Read data from given txt file
        lst= lst_default
        load_laserscan.transf_laserdata()
        pullData = open(txt) # open the given txt file (laserscan_data.txt)
        data = pullData.read().split(',') # separates data via commas
        if len(data) == 20: # Dont know why this is set to 20
            lst = list(map(float, data)) 
        pullData.close()

        # Assigns the values to corresponding bar
        rect = plt.bar(ranges, lst, color=palette)

        # Draw updated values
        fig.canvas.draw()

        # Run GUI event
        fig.canvas.flush_events()

        # Removes all bars
        rect.remove()
        time.sleep(0.1)
        

if __name__ == '__main__':
    print_graph("/home/rhodes/groundReasonTeam_ws/src/comp370_project/laserscan_data.txt")