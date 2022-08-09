#! /usr/bin/env python3
# anhand von diesem Skript werden Data aus einer .bag Datei extracted werden und in einem csv Datei gespeichert werden 
#import rospy
import rosbag
import statistics
import numpy as np
from array import array
#from geometry_msgs.msg import PoseStamped

x = []
y = []
z = []
# yaw = []

bag = rosbag.Bag ('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_stationary_nlos/2022-08-05-13-36-54.bag')

# open the .bag file

for topic, msg, t in bag.read_messages(topics=['/odom']):

    x.append(msg.pose.pose.position.x)
    y.append(msg.pose.pose.position.y)
    z.append(msg.pose.pose.position.z)   
    #yaw.append(msg.pose.pose.orientation.z)

bag.close()

x = np.array ([x])
y = np.array ([y])
z = np.array ([z])
#yaw = np.array ([yaw])

#save data in an csv file in /recording/myresults
#change the name of the file if required


np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_stationary_nlos/2022-08-05-13-36-54_x_odom.csv',x, delimiter=",", header="position in x direction for 1.6 m/s odom")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_stationary_nlos/2022-08-05-13-36-54_y_odom.csv',y, delimiter=",", header="position in y direction for 1.6 m/s odom")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_stationary_nlos/2022-08-05-13-36-54_z_odom.csv',z, delimiter=",", header="position in z direction for 1.6 m/s odom")
#np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/myresults/yaw_30_sec_stationary.csv',yaw, delimiter=",", header="orientation variation in yaw direction")

# in case to print an array

#print ('position variation in x direction:', x, 'position variation in y direction:', y, 'position variation in z direction:', z)

#print (x)

#in case to define the variance uncomment

#variance_x = statistics.variance(x)
#variance_y = statistics.variance(y)
#variance_z = statistics.variance(z)
#variance_yaw = statistics.variance (yaw)
#print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
    