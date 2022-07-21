#! /usr/bin/env python3
import rospy

from geometry_msgs.msg import PoseWithCovarianceStamped

    
initpose_msg = PoseWithCovarianceStamped()


initpose_msg.pose.pose.position.x= 0
initpose_msg.pose.pose.position.y= 0
initpose_msg.pose.pose.position.z= 0
initpose_msg.pose.pose.orientation.w= 0
initpose_msg.pose.pose.orientation.z= 0
initpose_msg.pose.pose.orientation.y= 0
initpose_msg.pose.pose.orientation.x= 0
initpose_msg.pose.covariance = [0.0004, 0, 0, 0, 0, 0, 0, 0.0004, 
                                    0, 0, 0, 0, 0, 0, 0.0004, 0, 0, 0, 
                                    0, 0, 0, 0.0004, 0, 0, 0, 0, 0, 0, 
                                    0.0004, 0, 0, 0, 0, 0, 0, 0.0004]
    


if __name__=='__main__':
    rospy.init_node("changepose")
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)
    
    