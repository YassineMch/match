#! /usr/bin/env python3
# anhand von diesem Skript werden Data aus einer .bag Datei extracted werden und in einem csv Datei gespeichert werden 
#import rospy
import rosbag
import statistics
import numpy as np
from array import array
from marvelmind_nav.msg import hedge_pos_ang
#from geometry_msgs.msg import PoseStamped

x = []
y = []
z = []

bag = rosbag.Bag ('/home/ros/catkin_ws_yassin/src/match/aufnahmen/2022-08-05-13-48-37.bag')

# open the .bag file

for topic, msg, t in bag.read_messages(topics=['/hedge2/hedge_pos_ang']):

    x.append(msg.x_m)
    y.append(msg.y_m)
    z.append(msg.z_m)   
    

bag.close()

x = np.array ([x])
y = np.array ([y])
z = np.array ([z])

#save data in an csv file in /recording/myresults
#change the name of the file if required

np.savetxt('/home/ros/catkin_ws_yassin/src/match/aufnahmen/2022-08-05-13-48-37_x.csv',x, delimiter=",", header="position in x direction for 1.6 m/s")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/aufnahmen/2022-08-05-13-48-37_y.csv',y, delimiter=",", header="position in y direction for 1.6 m/s")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/aufnahmen/2022-08-05-13-48-37_z.csv',z, delimiter=",", header="position in z direction for 1.6 m/s")

# in case to print an array

print ('position  in x direction:', x, 'position in y direction:', y, 'position in z direction:', z)

#print (x)
#print (y)
#print (z)
#in case to define the variance uncomment

#variance_x = statistics.variance(x)
#variance_y = statistics.variance(y)
#variance_z = statistics.variance(z)
#variance_yaw = statistics.variance (yaw)
#print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
    