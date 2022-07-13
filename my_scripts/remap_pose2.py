#! /usr/bin/env python3
import rospy
from marvelmind_nav.msg import hedge_pos_ang
from geometry_msgs.msg import PoseStamped

seq_counter = 0


def callback_convert_pose(msg_in):
    
    #type definition
    msg_out = PoseStamped()

    #header
    global seq_counter #sequential counter
    msg_out.header.seq = seq_counter
    seq_counter += 1
    
    msg_out.header.stamp = rospy.get_rostime() #in ros time format (#seconds & #nanoseconds)
    msg_out.header.frame_id = "odom" 
        
    #point position
    msg_out.pose.position.x = msg_in.x_m
    msg_out.pose.position.y = msg_in.y_m
    msg_out.pose.position.z = msg_in.z_m
        
    #quaternion orientation
    #here we would need to convert from angle to quaternions, temporarily all set to 0
    msg_out.pose.orientation.x = 0
    msg_out.pose.orientation.y = 0
    msg_out.pose.orientation.z = 0
    msg_out.pose.orientation.w = 0

    #publish converted message
    pub.publish(msg_out)

if __name__=='__main__':
    rospy.init_node("convert_hedgepos_posestamped")
    sub = rospy.Subscriber("hedge1/hedge_pos_ang", hedge_pos_ang, callback_convert_pose)
    pub = rospy.Publisher("/marvelmind_pos", PoseStamped, queue_size=10)
    rospy.spin()
    
    