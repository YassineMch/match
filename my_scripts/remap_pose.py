#!/usr/bin/env python3

import rospy
from marvelmind_nav.msg import hedge_pos_ang
from geometry_msgs.msg import PoseStamped

seq_init = 0 


def callback_marvelmind_pos(msg_pos):
    
    pose_out = PoseStamped()
    
    
# define header 
    global seq_init
    pose_out.header.seq = seq_init
    seq_init += 1

    pose_out.header.stamp = rospy.Time.now()
    pose_out.header.frame_id = 'map'


# position
    pose_out.pose.position.x = msg_pos.x_m
    pose_out.pose.position.y = msg_pos.y_m
    pose_out.pose.position.z = msg_pos.z_m

#Quaterion 
    pose_out.pose.orientation.x = 0
    pose_out.pose.orientation.y = 0
    pose_out.pose.orientation.z = 0
    pose_out.pose.orientation.w = 0
    
    pub.publish(pose_out)

if __name__ =='__main__':
    rospy.init_node('remap_pose')
    sub = rospy.Subscriber("/hedge1/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos)
    pub = rospy.Publisher("/position_marvelmind", PoseStamped, queue_size=10)
    rospy.spin()