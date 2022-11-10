#! /usr/bin/env python3
# Dieses Script dient dazu, zu der Initial Pose (tf map to odom anhand vom AMCL) upzudaten anhang der Pose-Daten von den mobielen Beacons 

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped



initpose_msg = PoseWithCovarianceStamped()

def callback_position(msg_in):
    #transfer Data to PoseWithCovariancestamped

    initpose_msg.header.seq = msg_in.header.seq
    initpose_msg.header.stamp = msg_in.header.stamp
    initpose_msg.header.frame_id = 'beacon_map'
    initpose_msg.pose = msg_in.pose

    


if __name__=='__main__':
    rospy.init_node("setup_initial_pose")

    rate = rospy.Rate(1)
    sub = rospy.Subscriber("/position_marvelmind_with_covariance", PoseWithCovarianceStamped, callback_position)
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)

    while not rospy.is_shutdown():
            connections = pub.get_num_connections()
            rospy.loginfo('Connections: %d', connections)
            if connections > 2 and initpose_msg.pose.pose.position.x != 0:
                pub.publish(initpose_msg)
                rospy.loginfo('Published')
                break
rate.sleep ()
