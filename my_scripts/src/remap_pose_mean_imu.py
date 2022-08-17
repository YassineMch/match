#!/usr/bin/env python3

# mit diesem Skript werden Daten aus dem Marvelmind hedge_pos_ang und hedge_imu_fusion Topics in einem PoseWithCovarianceStamped msg gespeichert werden 

import rospy
from marvelmind_nav.msg import  hedge_imu_fusion
from sensor_msgs.msg import Imu

seq_init = 0 
imu_out = Imu()

def callback_marvelmind_imu(msg_pos_imu):   

# define header 
    imu_out.header.seq = seq_init 
    seq_init += 1
    imu_out.header.stamp = rospy.Time.now()
    imu_out.header.frame_id = 'map'

#imu_orientation
    imu_out.orientation.x = msg_pos_imu.qx
    imu_out.orientation.y = msg_pos_imu.qy
    imu_out.orientation.z = msg_pos_imu.qz
    imu_out.orientation.w = msg_pos_imu.qw
    imu_out.orientation_covariance = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#imu_angular velocity
    imu_out.angular_velocity.x = msg_pos_imu.vx
    imu_out.angular_velocity.y = msg_pos_imu.vy
    imu_out.angular_velocity.z = msg_pos_imu.vz
    imu_out.angular_velocity_covariance = [0, 0, 0, 0, 0, 0, 0, 0, 0]

  #imu_angular velocity
    imu_out.linear_acceleration.x = msg_pos_imu.ax
    imu_out.linear_acceleration.y = msg_pos_imu.ay
    imu_out.linear_acceleration.z = msg_pos_imu.az
    imu_out.linear_acceleration_covariance = [0, 0, 0, 0, 0, 0, 0, 0, 0]  

    pub.publish(imu_out)

if __name__ =='__main__':
    rospy.init_node('remap_pose_mean_covariance')

    rate = rospy.Rate(10)
    sub = rospy.Subscriber("/hedge1/hedge_imu_fusion", hedge_imu_fusion , callback_marvelmind_imu)
    pub = rospy.Publisher("/imu_marvelmind_with_covariance", Imu, queue_size=10)

    rospy.spin()