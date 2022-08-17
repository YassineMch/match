#! /usr/bin/env python3
# anhand von diesem Skript werden Data aus einer .bag Datei extracted werden und in einem csv Datei gespeichert werden 
#import rospy
import rosbag
import statistics
import numpy as np
from array import array
from geometry_msgs.msg import PoseWithCovarianceStamped
#from geometry_msgs.msg import PoseStamped

x = []
y = []
z = []

bag = rosbag.Bag ('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.8_ms/2022-08-11-17-21-43.bag')

# open the .bag file

for topic, msg, t in bag.read_messages(topics=['/position_marvelmind_with_covariance']):

    x.append(msg.pose.pose.position.x)
    y.append(msg.pose.pose.position.y)
    z.append(msg.pose.pose.position.z)   
    

bag.close()

x = np.array ([x])
y = np.array ([y])
z = np.array ([z])

#save data in an csv file in /recording/myresults
#change the name of the file if required

np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.8_ms/2022-08-11-17-21-43_x.csv',x, delimiter=",", header="position in x direction for 0.6 m/s")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.8_ms/2022-08-11-17-21-43_y.csv',y, delimiter=",", header="position in y direction for 0.6 m/s")
np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.8_ms/2022-08-11-17-21-43_z.csv',z, delimiter=",", header="position in z direction for 0.6 m/s")

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
    