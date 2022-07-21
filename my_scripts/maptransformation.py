#!/usr/bin/env python3

import rospy
import tf
import position_marvelmind.msg

def callback_position(msg_pos, args):

    br = tf.TransformBroadcaster()
    br.sendTransform ((msg_pos.pose.orientation.x, msg_pos.pose.orientation.y, 0), (msg_pos.pose.orientation.x, msg_pos.pose.orientation.y. msg_pos.pose.orientation.z, msg_pos.pose.orientation.w), rospy.Time.now(), args[1], args[2] )
    
    
    
    if __name__ =='__main__':
        rospy.init_node('maptransformation')
    
    
    sub = rospy.Subscriber("/position_marvelmind", PoseStamped, callback_position)