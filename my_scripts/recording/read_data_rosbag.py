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
yaw = []

bag = rosbag.Bag ('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/30_sec_stationairy.bag')

# open the .bag file

for topic, msg, t in bag.read_messages(topics=['/position_marvelmind']):

    x.append(msg.pose.position.x)
    y.append(msg.pose.position.y)
    z.append(msg.pose.position.z)   
    yaw.append(msg.pose.orientation.z)

bag.close()

x = np.array ([x])
y = np.array ([y])
z = np.array ([z])
yaw = np.array ([yaw])

#save data in an csv file in /recording/myresults
#change the name of the file if required

np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/myresults/x_30_sec_stationary.csv',x, delimiter=",", header="position variation in x direction")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/myresults/y_30_sec_stationary.csv',y, delimiter=",", header="position variation in y direction")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/myresults/z_30_sec_stationary.csv',z, delimiter=",", header="position variation in z direction")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/myresults/yaw_30_sec_stationary.csv',yaw, delimiter=",", header="orientation variation in yaw direction")

# in case to print an array

print ('position variation in x direction:', x, 'position variation in y direction:', y, 'position variation in z direction:', z, 'orientation variation in yaw direction:', yaw)

#print (x)

#in case to define the variance uncomment

#variance_x = statistics.variance(x)
#variance_y = statistics.variance(y)
#variance_z = statistics.variance(z)
#variance_yaw = statistics.variance (yaw)
#print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
    