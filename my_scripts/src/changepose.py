#! /usr/bin/env python3
import rospy

from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped

t_n = 0

def callback_position(msg_in):
    global t_n
    update_rate = 4 
    rospy.get_time()
    
    #transfer Data to PoseWithCovariancestamped
    initpose_msg = PoseWithCovarianceStamped()
    initpose_msg.header = msg_in.header
    initpose_msg.pose.pose = msg_in.pose

    #covariance matrix
    initpose_msg.pose.covariance = [0.0004, 0, 0, 0, 0, 0, 0, 0.0004, 0, 0, 0, 0, 0, 0, 0.0004, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0004]
    
    if (rospy.get_time()-t_n > update_rate):

        pub.publish(initpose_msg)
        t_n = rospy.get_time()


if __name__=='__main__':
    
    rospy.init_node("changepose")
    sub = rospy.Subscriber("/position_marvelmind", PoseStamped, callback_position)
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)
    
    rospy.spin()
    