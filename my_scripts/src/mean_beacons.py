#!/usr/bin/env python3

# mit diesem Skript werden Daten aus dem Marvelmind hedge_pos_ang und hedge_imu_fusion Topics in einem PoseWithCovarianceStamped msg gespeichert werden 

import rospy
from marvelmind_nav.msg import hedge_pos_ang
from geometry_msgs.msg import PoseWithCovarianceStamped

seq_init = 0 
pose_out = PoseWithCovarianceStamped()

x_1 = 0
y_1 = 0
z_1 = 0
x_2 = 0
y_0 = 0
z_2 = 0


def callback_marvelmind_pos_1(msg_pos_1):   
    global  x_1, y_1, z_1, angle

    x_1 = msg_pos_1.x_m
    y_1 = msg_pos_1.y_m
    z_1 = msg_pos_1.z_m
    

def callback_marvelmind_pos_2(msg_pos_2):   
    global seq_init, x_2, y_2, z_2
    
    x_2 = msg_pos_2.x_m
    y_2 = msg_pos_2.y_m
    z_2 = msg_pos_2.z_m
    
# define header 
    pose_out.header.seq = seq_init
    seq_init += 1
    
    pose_out.header.stamp = rospy.Time.now()
    pose_out.header.frame_id = 'beacon_map'

# mean position from Beacons pose data
    pose_out.pose.pose.position.x = (x_1 + x_2)/2
    pose_out.pose.pose.position.y = (y_1 + y_2)/2
    pose_out.pose.pose.position.z = 0      # mit Absicht auf null

# Quaterion from imu_fused data
    pose_out.pose.pose.orientation.x = 0 # mit Absicht auf null
    pose_out.pose.pose.orientation.y = 0 # mit Absicht auf null
    pose_out.pose.pose.orientation.z = 0
    pose_out.pose.pose.orientation.w = 0

# covariance matrix with variance data from stationary state of the Beacons 
    pose_out.pose.covariance = [0.04783418046042617, 0, 0, 0, 0, 0,
                                0, 0.04189385245433789, 0, 0, 0, 0,
                                0, 0, 0.0016022922374429218, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                0, 0, 0, 0, 0, 1.6018519786910204e-05]

    pub.publish(pose_out)

if __name__ =='__main__':
    rospy.init_node('mean_beacons')

    rate = rospy.Rate(10)
    sub_1 = rospy.Subscriber("/hedge1/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_1)
    sub_2 = rospy.Subscriber("/hedge2/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_2)
    pub=rospy.Publisher("/position_mean", PoseWithCovarianceStamped, queue_size=10)

    rospy.spin()