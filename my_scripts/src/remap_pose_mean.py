#!/usr/bin/env python3

import rospy
import math 
from marvelmind_nav.msg import hedge_pos_ang
from geometry_msgs.msg import PoseStamped
from tf import transformations


seq_init = 0 
pose_out = PoseStamped()

x_1 = 0
y_1 = 0
z_1 = 0
x_2 = 0
y_0 = 0
z_2 = 0
angle = 0

def callback_marvelmind_pos_1(msg_pos_1):   
    global  x_1, y_1, z_1, angle

    x_1 = msg_pos_1.x_m
    y_1 = msg_pos_1.y_m
    z_1 = msg_pos_1.z_m
    #angle = (msg_pos_1.angle*math.pi)/180

def callback_marvelmind_pos_2(msg_pos_2):   
    global seq_init, x_2, y_2, z_2
    
    x_2 = msg_pos_2.x_m
    y_2 = msg_pos_2.y_m
    z_2 = msg_pos_2.z_m
    angle = (msg_pos_2.angle*math.pi)/180
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

    [x_quaternion,y_quaternion,z_quaternion,w_quaternion] = transformations.quaternion_from_euler (0, 0, angle)

    pose_out.pose.orientation.x = x_quaternion
    pose_out.pose.orientation.y = y_quaternion
    pose_out.pose.orientation.z = z_quaternion
    pose_out.pose.orientation.w = w_quaternion
    
    pub.publish(pose_out)

if __name__ =='__main__':
    rospy.init_node('remap_pose')
    
    sub_1=rospy.Subscriber("/hedge1/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_1)
    sub_2=rospy.Subscriber("/hedge2/hedge_pos_ang", hedge_pos_ang, callback_marvelmind_pos_2)
    pub=rospy.Publisher("/position_marvelmind", PoseStamped, queue_size=10)

    rospy.spin()