#!/usr/bin/env python3

# mit diesem Skript werden Daten aus dem Marvelmind hedge_pos_ang und hedge_imu_fusion Topics in einem PoseWithCovarianceStamped msg gespeichert werden 

import rospy
import math 
from marvelmind_nav.msg import hedge_pos_ang, hedge_imu_fusion
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
    pose_out.header.frame_id = 'map'

# mean position from Beacons pose data
    pose_out.pose.position.x = (x_1 + x_2)/2
    pose_out.pose.position.y = (y_1 + y_2)/2
    pose_out.pose.position.z = (z_1 + z_2)/2

# Quaterion from imu_fused data
def callback_marvelmind_pos_3(msg_pos_imu):   

    pose_out.pose.orientation.x = msg_pos_imu.qx
    pose_out.pose.orientation.y = msg_pos_imu.qy
    pose_out.pose.orientation.z = msg_pos_imu.qz
    pose_out.pose.orientation.w = msg_pos_imu.qw

# covariance matrix with variance data from stationary state of the Beacons 
    pose_out.pose.covariance = [0.007376561813186813, 0, 0, 0, 0, 0,
                                0, 0.007376561813186813, 0, 0, 0, 0,
                                0, 0, 0.007376561813186813, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                0, 0, 0, 0, 0, 1.865003690775747e-06]

    pub.publish(pose_out)

if __name__ =='__main__':
    rospy.init_node('remap_pose_mean_covariance')

    rate = rospy.Rate(10)
    sub_1 = rospy.Subscriber("/hedge1/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_1)
    sub_2 = rospy.Subscriber("/hedge2/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_2)
    sub_3 = rospy.Subscriber("/hedge1/hedge_imu_fusion", hedge_imu_fusion , callback_marvelmind_pos_3)
    pub=rospy.Publisher("/position_marvelmind_with_covariance", PoseWithCovarianceStamped, queue_size=10)

    rospy.spin()