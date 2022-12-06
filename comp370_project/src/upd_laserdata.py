#!/usr/bin/env python3

"""upd_laserdata Imformation
    Puts the information from the laserdata topic to the laserdata text file.
"""

# Every python controller needs these lines
import roslib; roslib.load_manifest('comp370_project')
import rospy
import sys # For args from launch file
import math
import numpy as np
from sensor_msgs.msg import LaserScan # The laser scan message
import time

# Convert an array into a small array containing it EVERY 32TH TERM.
def read_data1(arr, div):                # div = 20 ; len(arr)= 640
    parts = int(len(arr)/div)             # len(arr)/div = parts = 32
    avg_array = []
    for i in range(parts-1, len(arr), parts):   #From 0, 31, 63, ..., 511, 544, 575 = i
        if not math.isnan (arr[i]):             # Check if current value is not a nan
            avg_array.append(round(arr[i], 4))
        else:                                   # If the values were nan, then append max distance
            avg_array.append(0.7) 
    return avg_array

# Convert an array into a small array containing it AVERAGES
def read_data2(arr, div): # div = 20 ; len(arr)= 640
    parts = int(len(arr)/div) # len(arr)/div = parts = 32
    avg_array = []
    for i in range(0, len(arr), parts): # From 0, 32, 64, ..., 512, 545, 608= i
        total = 0.0
        sum = 0
        all_nan = True
        for j in range(0, parts): # Add the values from arr[i:parts+i]
            if not math.isnan (arr[j+i]): # Check if current value is not a nan
                all_nan = False
                sum += 1
                total += arr[j+i]
        if all_nan:
            avg_array.append(0.0) # If all the values were nan, then add 1
        else:
            avg_array.append(round(total/sum, 4)) # Average of all the values within the section
    return avg_array


# Update the laserscan data to the text file
def update_data(data):
    txt = "/home/rhodes/groundReasonTeam_ws/src/comp370_project/laserscan_data.txt"
    # Formate the data
    data = str(data).replace(' ', '')
    data = data[1:len(data)-1]
    # Write data to text file
    pullData = open(txt,"w")
    pullData.write(data)
    pullData.close()


def callback(scan):
    #data = read_data1(scan.ranges, 20) # Convert an array into a small array containing it EVERY 32TH TERM.
    data = read_data2(scan.ranges, 20) # Convert an array into an array of length 20 of EVERY 32th TERM
    update_data(data)
    

def transf_laserdata():
    rospy.init_node('transf_laserscan', anonymous=True)
    # rospy.loginfo('Reading Laserscan data Initialized')
    time.sleep(0.1)
    rospy.Subscriber('/scan', LaserScan, callback) # callback is subsribed to the LaserScan data.

if __name__ == '__main__':
    # Argument within Launch
    #args = rospy.myargv(argv=sys.argv)
    #para1 = args[1]
    #lazerdata_printpara1)

    transf_laserdata()