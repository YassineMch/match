#! /usr/bin/env python3
import rospy

from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped

#prev_time = 0

def callback_position(msg_in):
    
    #timer to limit publishing rate
    #global prev_time
    #interval = 4 #seconds
    #currentTime = rospy.get_time()
    
  
    initpose_msg = PoseWithCovarianceStamped()
    initpose_msg.header = msg_in.header
    initpose_msg.pose.pose = msg_in.pose

    #covariance matrix
    initpose_msg.pose.covariance = [0.0004, 0, 0, 0, 0, 0, 0, 0.0004, 0, 0, 0, 0, 0, 0, 0.0004, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0004]
    
    #if (currentTime-prev_time > interval):
        #publish converted message
        #pub.publish(initpose_msg)
        #prev_time = rospy.get_time()


if __name__=='__main__':
    rospy.init_node("changepose")
    sub = rospy.Subscriber("/position_marvelmind", PoseStamped, callback_position)
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)

    rate = rospy.Rate(0.1)

while not rospy.is_shutdown():
    rate.sleep()
    