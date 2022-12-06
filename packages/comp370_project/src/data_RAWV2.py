#!/usr/bin/env python3

"""data_RAWV2 Imformation
    Same as data_RAWV1 but this prints out on the terminal the 8th term from the LaserScan float array.
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


# Convert an array into a small array containing it 16th term.
def average_arr(arr, div):                # div = 40 ; len(arr)= 640
    parts = int(len(arr)/div)             # len(arr)/div = parts = 16
    avg_array = []
    for i in range(parts-1, len(arr), parts):   # From 15, 31, 47...639 = i
        if not math.isnan (arr[i]):             # Check if current value is not a nan
            avg_array.append(round(arr[i], 2))
        else:                                   # If the values were nan, then append nan
            avg_array.append(math.nan) 
    return avg_array

# Print out an large array into smaller average array.
def laser_array_print(ranges):
    simlify_laserdata = average_arr(ranges, 40) 
    print(" LEFT (30 Degree)    (25 Degree)    (20 Degree)    (15 Degree)    (10 Degree)   (5 Degree)    (0 Degree)   (-5 Degree)   (-10 Degree)   (-15 Degree)   (-20 Degree)   (-25 Degree)   (-30 Degree) RIGHT")
    print(simlify_laserdata)


# Print the lazerScan data in a formated way.
def formated_print(scan):
    print("Minimun Angle:------------- ", '{0:.2f}'.format(scan.angle_min), "rad")
    print("Maximun Angle:------------- ", '{0:.2f}'.format(scan.angle_max), "rad")
    print("Angle increment:----------- ", '{0:.5f}'.format(scan.angle_increment), "rad")
    print("Angle calculation time:---- ", '{0:.2f}'.format(scan.scan_time), "s")
    print("Minimun Range:------------- ",  '{0:.2f}'.format(scan.range_min), " m")
    print("Maximun Range-------------- ", '{0:.2f}'.format(scan.range_max), " m")
    print("Length of Array:----------- ", len(scan.ranges))
    print("Array:")
    #print(scan.ranges)
    laser_array_print(scan.ranges)

def callback(scan):
    rate = rospy.Rate(1)
    os.system('clear') # Clear terminal at every update of the values
    formated_print(scan) 
    rate.sleep()

def lazerdata_print():
    rospy.init_node('lazerdataRAW_V2_print', anonymous=True)
    rospy.loginfo('Data Visualization Initialized')
    rospy.Subscriber('/scan', LaserScan, callback) # callback is subsribed to the LaserScan data.

    rospy.spin() # simply keeps python from exiting until this node is stopped

if __name__ == '__main__':
    # Argument within Launch
    #args = rospy.myargv(argv=sys.argv)
    #para1 = args[1]
    #lazerdata_printpara1)

    lazerdata_print()