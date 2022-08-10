#! /usr/bin/env python3
# anhand von diesem Skript werden Data aus einer .bag Datei extracted werden und in einem csv Datei gespeichert werden 
#import rospy
import rosbag
import statistics
import numpy as np
from array import array
#from geometry_msgs.msg import PoseStamped

#x = []
#y = []
#z = []
x_punkt = []
y_punkt = []
z_punkt = []
# yaw = []

bag = rosbag.Bag ('/home/rosmatch/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_0.2_ms/2022-08-05-13-13-14.  bag')

# open the .bag file

for topic, msg, t in bag.read_messages(topics=['/odom']):

    #x.append(msg.pose.pose.position.x)
    #y.append(msg.pose.pose.position.y)
    #z.append(msg.pose.pose.position.z)
    x_punkt.append(msg.twist.twist.linear.x)
    y_punkt.append(msg.twist.twist.linear.y)
    z_punkt.append(msg.twist.twist.linear.z)
    #yaw.append(msg.pose.pose.orientation.z)

bag.close()

#x = np.array ([x])
#y = np.array ([y])
#z = np.array ([z])
x_punkt = np.array ([x_punkt])
y_punkt = np.array ([x_punkt])
z_punkt = np.array ([x_punkt])
#yaw = np.array ([yaw])

#save data in an csv file in /recording/myresults
#change the name of the file if required


np.savetxt('/home/rosmatch/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_0.2_ms/2022-08-05-13-13-14_x_punkt_odom.csv',x_punkt, delimiter=",", header="geschwindigkeit in x direction for approx 0.2 m/s odom")
np.savetxt('/home/rosmatch/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_0.2_ms/2022-08-05-13-13-14_y_punkt_odom.csv',y_punkt, delimiter=",", header="geschwindigkeit in y direction for approx 0.2 m/s odom")
np.savetxt('/home/rosmatch/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_0.2_ms/2022-08-05-13-13-14_z_punkt_odom.csv',z_punkt, delimiter=",", header="geschwindigkeit in z direction for approx 0.2 m/s odom")
#np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/myresults/yaw_30_sec_stationary.csv',yaw, delimiter=",", header="orientation variation in yaw direction")

# in case to print an array

#print ('position variation in x direction:', x, 'position variation in y direction:', y, 'position variation in z direction:', z)

print ('geschwindigkeit variation in x direction:', x_punkt, 'geschwindigkeit variation in y direction:', y_punkt, 'geschwindigkeit variation in z direction:', z_punkt)

#in case to define the variance uncomment

#variance_x = statistics.variance(x)
#variance_y = statistics.variance(y)
#variance_z = statistics.variance(z)
#variance_yaw = statistics.variance (yaw)
#print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
    