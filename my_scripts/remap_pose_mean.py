#!/usr/bin/env python3

import rospy
from marvelmind_nav.msg import hedge_pos_ang
from geometry_msgs.msg import PoseStamped

seq_init = 0 
pose_out = PoseStamped()

def callback_marvelmind_pos_1(msg_pos_1):   
    global  x_1, y_1, z_1

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

# position
    pose_out.pose.position.x = (x_1 + x_2)/2
    pose_out.pose.position.y = (y_1 + y_2)/2
    pose_out.pose.position.z = (z_1 + z_2)/2

#Quaterion 
    pose_out.pose.orientation.x = 0
    pose_out.pose.orientation.y = 0
    pose_out.pose.orientation.z = 0
    pose_out.pose.orientation.w = 0
    
    pub.publish(pose_out)

if __name__ =='__main__':
    rospy.init_node('remap_pose')
    
    sub_1=rospy.Subscriber("/hedge1/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_1)
    sub_2=rospy.Subscriber("/hedge2/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_2)
    pub=rospy.Publisher("/position_marvelmind", PoseStamped, queue_size=10)

    rospy.spin()