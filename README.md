# Table of contents

- Introduction
- Requirements
- Sources
- Installation
- Configuration
- Troubleshooting
- FAQ
- Maintainers

## Introduction

Robots are commonly assumed to have higher function than is typically true. This project aims to underline 
the significant limitations of robots and highlight the process by which robots interpret and understand data.
By analyzing data presented by a laser placed on a turtlebot, the general public will see the difficulties 
that come from data analysis in a diverse environment. These demonstrations will teach participants about the 
issue that comes from a robot's perception of its setting and how that can lead to problematic sensor data 
and poor decision-making.

- Link to the project page:

  [Rhodes College Webpage](https://cs.rhodes.edu/~reasoningbot).
  
  [GitHub Repositary](https://github.com/diego-glm/groundReasoning).
  
  [Video Demostration](https://youtu.be/6WE1XAsuSCI).
  
## Requirements

This module requires the following setup:

For Host machine:
- [ROS setup](https://wiki.ros.org/ROS/Installation)
- [Ground Reasoning Packages](https://github.com/diego-glm/groundReasoning/tree/main/packages)

For Turtlebot:
- [Turtlebot setup](http://wiki.ros.org/turtlebot/Tutorials/indigo/Turtlebot%20Installation)

## Sources

These were the sources that were used within the Ground Reasoning files: (Not required to have if you have the Ground Reasoning packages)

[turtlebot](https://github.com/turtlebot/turtlebot.git): The turtlebot stack provides all the 
basic drivers for running and using a TurtleBot with ROS.

[kobuki](https://github.com/yujinrobot/kobuki.git):(kobuki/kobuki_description) this specific folder for
the complete kobuki layout in rviz. Help fix certain warnings if working with a kobuki.

[Turtlebot interactions](https://github.com/turtlebot/turtlebot_interactions.git): Contains the Slam Map
pre-setup

## Installation

Follow the ROS setup on your Host computer and Turtlebot setup on the os of the robot (see Requirement section.)

Import Ground Reasoning "packages" into your workspace (make sure you build these packages with catkin_make). 

## Configuration

1. Establish a network configuration between the turtlebot and Host machine
   (see http://wiki.ros.org/turtlebot/Tutorials/indigo/Network%20Configuration)
2. On the turtlebot, run:

   $ roslaunch turtlebot_bringup minimal.launch --screen
   
3. On the turtlebot, run:

   $ roslaunch turtlebot_navigation gmapping_demo.launch
  
4. On the turtlebot, run and put always on top:

   $ roslaunch turtlebot_teleop keyboard_teleop.launch --screen
   
5. On the Host computer, run:

   $ roslaunch comp370_project start_interface.launch levelNUM:=true
   
   Exchange the "NUM" for any number 1-6 to run the desire activity.

## Configuration

The command start_interface.launch  has an argument level1-6 that has true for the desire activity to run.
The set ups is as follows:

      (1) Display the laserscan data raw and semi-formated to the terminal.
      
      (2) Display the laserscan data with a filter formated to the terminal.
      
      (3) Display the laserscan data with a filter to a live bar plot graph.
      
      (4) Display a live slam map interface with rviz.
      
      (5) Display a live camera feed with a depth filter with rviz.
      
      (6) Display a live camera feed with no filters (just RGB) with rviz.

# Troubleshooting

Wait for minimal.launch to setup before running gmapping_demo.launch. Usually, turtlebot will bep once it done.

Before running start_interface.launch, wait for gmapping.lauch to fully run. Wait for the message "ODM Recieved!"

### FAQ

Q:

A: 

## Maintainers

Current maintainers:
- Brayan Castro  - http://github.com/BrayanCastro
- Diego Gabriel Lopez Murillo - http://github.com/dieglo-glm
- Jackson Hendrix - http://github.com/JCHendrix33
