#! /usr/bin/env python3

#import rospy
import rosbag
import statistics
#from geometry_msgs.msg import PoseStamped

x = []
y = []
z = []
yaw = []

bag = rosbag.Bag ('/home/ros/catkin_ws_yassin/src/match/my_scripts/recording/30_sec_stationairy.bag')


for topic, msg, t in bag.read_messages(topics=['/position_marvelmind']):

    x.append(msg.pose.position.x)
    y.append(msg.pose.position.y)
    z.append(msg.pose.position.z)   
    yaw.append(msg.pose.orientation.z)

bag.close()

# in case to print an array

print ('position variation in x direction:', x, 'position variation in y direction:', y, 'position variation in z direction:', z, 'orientation variation in yaw direction:', yaw)

#variance_x = statistics.variance(x)
#variance_y = statistics.variance(y)
#variance_z = statistics.variance(z)
#variance_yaw = statistics.variance (yaw)
#print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
    