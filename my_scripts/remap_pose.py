#!/usr/bin/env python

import rospy
from marvelmind_nav.msg import hedge_pos_ang
from geometry_msgs.msg import PoseStamped

seq_init = 0;
pose_out = PoseStamped()

def marvelmind_pos_callback(msg_pos):
    global seq_init
    
# define header 
pose_out.header.stamp = rospy.Time.now()
pose_out.header.frame_id = 'odom'

pose_out.header.seq = seq_init
seq_init += 1
 
# position
pose_out.pose.position.x = msg_pos.x_m
pose_out.pose.position.y = msg_pos.y_m
pose_out.pose.position.y = msg_pos.z_m

#Quaterion 
pose_out.pose.orientation.x = 0
pose_out.pose.orientation.y = 0
pose_out.pose.orientation.z = 0
pose_out.pose.orientation.w = 0

if __name__ == '__main__':
    
    rospy.init_node('position_marvelmind')
    
    pose_out_publisher = rospy.Publisher("/pose_out", PoseStamped, queue_size=5)
    pose_in_Suscriber = rospy.Subscriber("/hedge_pos_ang", msg_pos, marvelmind_pos_callback )
    
    rospy.spin()