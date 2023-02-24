#!/usr/bin/env python3

'''
This feels unnecessary for our demonstration. Not only is this printing fewer values, lowering the resolution of our 
sensor, but it also averages the data points, which would just lead to false information. Wouldn't be opposed to removing
this file entirely and replacing it with something else.
'''

"""Print out the laserscan topic to the terminal as averages.

An improvement from dataFilterTH.py. 
Prints out the laserscan topic in a formative 
style manner that revolves around averages.

Attributes:
    None
"""

# Every python controller needs these lines
import roslib; roslib.load_manifest('comp370_project')
import rospy
import sys # For args from launch file
import os 
import math
import numpy as np
from sensor_msgs.msg import LaserScan # The laser scan message

"""Create an smaller array from a bigger array

Convert an array into a small array containing it averages 
of each section.

Args:
    arr (array): the array that want to be reduce
    div (int):   dictates how the arr will be divided
Returns:
    The smaller representation of the arr given.

"""
def average_arr(arr, div):                # div = 40 ; len(arr)= 640
    parts = int(len(arr)/div)             # len(arr)/div = parts = 16
    avg_array = []
    for i in range(0, len(arr)-1, parts): # From 0, 16, 32...224 = i
        total = 0.0
        all_nan = True
        for j in range(0, parts):         # Add the values from arr[i:parts+i]
            if not math.isnan (arr[j+i]): # Check if current value is not a nan
                all_nan = False
                total += arr[j+i]
        if all_nan:
            avg_array.append(math.nan)              # If all the values were nan, then append nan
        else:
            avg_array.append(round(total/parts, 2)) # Average of all the values within the section
    return avg_array

def laser_array_print(ranges):
    simlify_laserdata = average_arr(ranges, 40) 
    print(" LEFT (30 Degree)    (25 Degree)    (20 Degree)    (15 Degree)    (10 Degree)   (5 Degree)    (0 Degree)   (-5 Degree)   (-10 Degree)   (-15 Degree)   (-20 Degree)   (-25 Degree)   (-30 Degree) RIGHT")
    print(simlify_laserdata)


""" Print laserscan data

Print the laserScan data in a formated way.

Args:
    scan (laserscan): single scan from a planar laser range-finder

"""
def formated_print(scan):
    print("Minimun Angle:------------- ", '{0:.2f}'.format(scan.angle_min), "rad")
    print("Maximun Angle:------------- ", '{0:.2f}'.format(scan.angle_max), "rad")
    print("Angle increment:----------- ", '{0:.5f}'.format(scan.angle_increment), "rad")
    print("Angle calculation time:---- ", '{0:.2f}'.format(scan.scan_time), "s")
    print("Minimun Range:------------- ",  '{0:.2f}'.format(scan.range_min), " m")
    print("Maximun Range-------------- ", '{0:.2f}'.format(scan.range_max), " m")
    print("Length of Array:----------- ", len(scan.ranges))
    print("Array:")
    laser_array_print(scan.ranges)


"""Interprets the laserscan data

Set up the rate, clears the terminal, and prints the laserscan data

Args:
    scan (laserscan): single scan from a planar laser range-finder

"""
def callback(scan):
    rate = rospy.Rate(1)
    os.system('clear') # Clear terminal at every update of the values
    formated_print(scan) 
    rate.sleep()

"""Inicializes the ROS environment

Creates a node within ROS and subsribes to the \scan topic

"""
def lazerdata_print():
    rospy.init_node('lazerdataAVG_print', anonymous=True)
    rospy.loginfo('Data Visualization Initialized')
    rospy.Subscriber('/scan', LaserScan, callback) # callback is subsribed to the LaserScan data.
    rospy.spin() # simply keeps python from exiting until this node is stopped

if __name__ == '__main__':
    lazerdata_print()