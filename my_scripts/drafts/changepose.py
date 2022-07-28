#! /usr/bin/env python3
# Dieses Script dient dazu, zu der Initial Pose (tf map to odom anhand vom AMCL) upzudaten anhang der Pose-Daten von den mobielen Beacons 

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped


initpose_msg = PoseWithCovarianceStamped()

def callback_position(msg_in):
    #transfer Data to PoseWithCovariancestamped
    
    initpose_msg.header = msg_in.header
    initpose_msg.pose.pose = msg_in.pose

    #covariance matrix mit der Variance von den Punkten bestimmt
    initpose_msg.pose.covariance = [0.007376561813186813, 0, 0, 0, 0, 0, 0, 0.007376561813186813, 0, 0, 0, 0, 0, 0, 0.007376561813186813, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.865003690775747e-06]
    


if __name__=='__main__':
    rospy.init_node("changepose")

    rate = rospy.Rate(10)
    sub = rospy.Subscriber("/position_marvelmind", PoseStamped, callback_position)
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)

    while not rospy.is_shutdown():
            connections = pub.get_num_connections()
            rospy.loginfo('Connections: %d', connections)
            if connections > 0 and initpose_msg.pose.pose.position.x != 0:
                pub.publish(initpose_msg)
                rospy.loginfo('Published')
                break
rate.sleep ()

    