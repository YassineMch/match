#! /usr/bin/env python3
# anhand von diesem Skript werden Data aus einer .bag Datei extracted werden und in einem csv Datei gespeichert werden 
#import rospy

import rosbag
import numpy as np
from nav_msgs.msg import Odometry  
import matplotlib.pyplot as plt

x_odom = []
y_odom = []
z_odom = []
x_fil = []
y_fil = []
z_fil = []
x_marv = []
y_marv = []
z_marv = []
x_2 = []
y_2 = []
z_2 = []
x_1 = []
y_1 = []
z_1 = []
bag = rosbag.Bag ('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahmen_test_marvelmind/stationary_state/aufnahme_stationary_nlos/2022-08-05-13-36-54.bag')

# open the .bag file
for topic, msg, t in bag.read_messages(topics=['/odom']):
    x_odom.append(msg.pose.pose.position.x)
    y_odom.append(msg.pose.pose.position.y)
    z_odom.append(msg.pose.pose.position.z)
for topic, msg, t in bag.read_messages(topics=['/odometry/filtered']):
    x_fil.append(msg.pose.pose.position.x)
    y_fil.append(msg.pose.pose.position.y)
    z_fil.append(msg.pose.pose.position.z)
for topic, msg, t in bag.read_messages(topics=['/position_marvelmind_with_covariance']):
    x_marv.append(msg.pose.pose.position.x)
    y_marv.append(msg.pose.pose.position.y)
    z_marv.append(msg.pose.pose.position.z)   
for topic, msg, t in bag.read_messages(topics=['/hedge2/hedge_pos_ang']):
    x_2.append(msg.x_m)
    y_2.append(msg.y_m)
    z_2.append(msg.z_m)   
for topic, msg, t in bag.read_messages(topics=['/hedge1/hedge_pos_ang']):
    x_1.append(msg.x_m)
    y_1.append(msg.y_m)
    z_1.append(msg.z_m)   
bag.close()



#save data in an csv file in /recording/myresults
    #change the name of the file if required

    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_x_odom.csv',x_odom, delimiter=",", header="position in x direction for 0.4 m/s")
    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_y_odom.csv',y_odom, delimiter=",", header="position in y direction for 0.4 m/s")
    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_z_odom.csv',z_odom, delimiter=",", header="position in z direction for 0.4 m/s")

    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_x_odom_filtered.csv',x_fil, delimiter=",", header="position in x direction for 0.4 m/s")
    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_y_odom_filtered.csv',y_fil, delimiter=",", header="position in y direction for 0.4 m/s")
    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_z_odom_filtered.csv',z_fil, delimiter=",", header="position in z direction for 0.4 m/s")

    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_x_marvelmind.csv',x_marv, delimiter=",", header="position in x direction for 0.4 m/s")
    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_y_marvelmind.csv',y_marv, delimiter=",", header="position in y direction for 0.4 m/s")
    #np.savetxt('/home/ros/catkin_ws_yassin/src/match/my_scripts/aufnahmen/aufnahme_nonomni_path_0.4_ms_filtered/2022-09-19-14-30-20_z_marvelmind.csv',z_marv, delimiter=",", header="position in z direction for 0.4 m/s")

# plot the data

#plot1=plt.plot(x_odom,y_odom,'-b',label='Odometry')
#plot2=plt.plot(x_fil,y_fil,'-k',label='Data fusion')
#plot3=plt.plot(x_marv,y_marv,'-r',label='Marvelmind')
#plot4=plt.plot(x_1,y_1,'ro',alpha=0.2,label='Beacon Position')
plot5=plt.plot(x_2,y_2,'bo',alpha=0.2,label='Beacon Position')

plt.legend(loc="upper right")
plt.grid(True)
plt.show()

    