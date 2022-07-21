#! /usr/bin/env python3
import rospy

from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped

prev_time = 0

def callback_send_poseestimate(msg_in):
    
    #timer to limit publishing rate
    global prev_time
    interval = 4 #seconds
    currentTime = rospy.get_time()
    
    #type definition
    msg_out = PoseWithCovarianceStamped()

    #transfer header and pose from original message
    msg_out.header = msg_in.header
    msg_out.pose.pose = msg_in.pose

    #create covariance matrix, empty for now
    msg_out.pose.covariance = [0.25,0,0,0,0,0,0,0.25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.06853892326654787]
    
    if (currentTime-prev_time > interval):
        #publish converted message
        pub.publish(msg_out)
        prev_time = rospy.get_time()


if __name__=='__main__':
    rospy.init_node("changepose")
    sub = rospy.Subscriber("/position_marvelmind", PoseStamped, callback_send_poseestimate)
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)
    rospy.spin()
    