#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped

t_n = 0 


def callback_marvelmind_pos(msg_pos):
    global t_n
    t_n1 = rospy.Time.now
    updateTime = 5
    pose_out = PoseWithCovarianceStamped()
    
    
# define header 

    pose_out.header = msg_pos.header
    pose_out.pose.pose = msg_pos.pose


# covariance
    pose_out.covariance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    
    pub.publish(pose_out)
    
    if (t_n1-t_n > updateTime):
        pub.publish(pose_out)
        t_n = rospy.get_time()
        
if __name__ =='__main__':
    rospy.init_node('changepose')
    sub = rospy.Subscriber("/position_marvelmind", PoseStamped, callback_marvelmind_pos)
    pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=10)
    rospy.spin