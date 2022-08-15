#! /usr/bin/env python3
# anhand von diesem Skript werden Data aus einer .bag Datei extracted werden und in einem csv Datei gespeichert werden 
#import rospy
import rosbag
import statistics
import numpy as np
from array import array
from nav_msgs.msg import Odometry  

x = []
y = []
z = []
#x_punkt = []
#y_punkt = []
#z_punkt = []
# yaw = []

bag = rosbag.Bag ('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.6_ms/2022-08-11-17-32-04.bag')

# open the .bag file

for topic, msg, t in bag.read_messages(topics=['/odom']):

    x.append(msg.pose.pose.position.x)
    y.append(msg.pose.pose.position.y)
    z.append(msg.pose.pose.position.z)
    #x_punkt.append(msg.twist.twist.linear.x)
    #y_punkt.append(msg.twist.twist.linear.y)
    #z_punkt.append(msg.twist.twist.linear.z)
    #yaw.append(msg.pose.pose.orientation.z)

bag.close()

x = np.array ([x])
y = np.array ([y])
z = np.array ([z])
#x_punkt = np.array ([x_punkt])
#y_punkt = np.array ([x_punkt])
#z_punkt = np.array ([x_punkt])
#yaw = np.array ([yaw])

#save data in an csv file in /recording/myresults
#change the name of the file if required


np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.6_ms/2022-08-11-17-32-04_x_odom.csv',x, delimiter=",", header="position in x direction for 0.6 m/s")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.6_ms/2022-08-11-17-32-04_y_odom.csv',y, delimiter=",", header="position in y direction for 0.6 m/s")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.6_ms/2022-08-11-17-32-04_z_odom.csv',z, delimiter=",", header="position in z direction for 0.6 m/s")

# in case to print an array

#print ('position variation in x direction:', x, 'position variation in y direction:', y, 'position variation in z direction:', z)

print ('geschwindigkeit variation in x direction:', x, 'geschwindigkeit variation in y direction:', y, 'geschwindigkeit variation in z direction:', z)

#in case to define the variance uncomment

#variance_x = statistics.variance(x)
#variance_y = statistics.variance(y)
#variance_z = statistics.variance(z)
#variance_yaw = statistics.variance (yaw)
#print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
    