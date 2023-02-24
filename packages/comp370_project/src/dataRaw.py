#!/usr/bin/env python3

"""
Prints unfiltered Data
"""

# Every python controller needs these lines
from shelve import Shelf
import roslib; roslib.load_manifest('comp370_project')
import rospy
import sys # For args from launch file
import os 
import math
import numpy as np
from sensor_msgs.msg import LaserScan # The laser scan message

""" Print laserscan data

Print the laserScan data in a semi-formated way.

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
    print(scan.ranges)

"""Interprets the laserscan data

Set up the rate, clears the terminal, and prints the laserscan data

Args:
    scan (laserscan): single scan from a planar laser range-finder

"""
def callback(scan):
    rate = rospy.Rate(1)
    os.system('clear')
    formated_print(scan)
    rate.sleep()

"""Inicializes the ROS environment

Creates a node within ROS and subsribes to the \scan topic

"""
def lazerdata_print():
    rospy.init_node('lazerdataRAW_V1_print', anonymous=True)
    rospy.loginfo('Data Visualization Initialized')
    rospy.Subscriber('/scan', LaserScan, callback)

    rospy.spin() # simply keeps python from exiting until this node is stopped

if __name__ == '__main__':
    # Argument within Launch
    #args = rospy.myargv(argv=sys.argv)
    #para1 = args[1]
    #lazerdata_printpara1)

    lazerdata_print()