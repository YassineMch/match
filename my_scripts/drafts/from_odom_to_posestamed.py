#! /usr/bin/env python3
import rospy

from geometry_msgs.msg import  PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

seq_init = 0 
pose_ekf = PoseWithCovarianceStamped()

#subscriber pose
def callback_ekf_nt(msg_pos):   
    global  seq_init
    pose_ekf.header=msg_pos.header
    pose_ekf.pose=msg_pos.pose
    pub.publish(pose_ekf)

if __name__ =='__main__':
    rospy.init_node('from_odom_to_posestamed')

    rate = rospy.Rate(10)
    sub = rospy.Subscriber("/odometry/filtered", Odometry, callback_ekf_nt)
    pub = rospy.Publisher("/pose_EKF_transformed", PoseWithCovarianceStamped, queue_size=10)

    rospy.spin()