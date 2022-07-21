#!/usr/bin/env python3

import rospy
import tf
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped

def callback_position(msg_pos):
    
    bc = tf.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "base_link"
    t.transform.translation = msg_pos.pose.pose.position
    t.transform.rotation = msg_pos.pose.pose.orientation
    bc.sendTransform(t)
    
    
    
    if __name__ =='__main__':
        rospy.init_node('maptransformation')
        rospy.Subscriber("/position_marvelmind", PoseStamped, callback_position)
        rospy.spin()