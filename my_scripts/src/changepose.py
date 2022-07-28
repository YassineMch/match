#! /usr/bin/env python3
# Dieses Script dient dazu, zu der Initial Pose (tf map to odom anhand vom AMCL) upzudaten anhang der Pose-Daten von den mobielen Beacons 

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
t_n = 0

# Callback greift auf die Position der Mobienen beacons aus dem Node Remap_pose_mean/_new.py
def callback_position(msg_in):
    global t_n
    update_rate = 4
    rospy.get_time()
    
    #transfer Data to PoseWithCovariancestamped
    initpose_msg = PoseWithCovarianceStamped()
    initpose_msg.header = msg_in.header
    initpose_msg.pose.pose = msg_in.pose

    #covariance matrix mit der Variance von den Punkten bestimmt
    initpose_msg.pose.covariance = [0.007376561813186813, 0, 0, 0, 0, 0, 0, 0.007376561813186813, 0, 0, 0, 0, 0, 0, 0.007376561813186813, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.865003690775747e-06]
    
    if (rospy.get_time()-t_n > update_rate):
        pub.publish(initpose_msg)
        t_n = rospy.get_time()

if __name__=='__main__':
    
    rospy.init_node("changepose")
    sub = rospy.Subscriber("/position_marvelmind", PoseStamped, callback_position)
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)
    
    rospy.spin()
    