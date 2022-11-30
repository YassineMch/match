#!/usr/bin/env python3

# mit diesem Skript werden Daten aus dem Marvelmind hedge_pos_ang und hedge_imu_fusion Topics in einem PoseWithCovarianceStamped msg gespeichert werden 

import rospy
from marvelmind_nav.msg import  hedge_imu_raw
from sensor_msgs.msg import Imu

seq_init = 0 
imu_out = Imu()

def callback_marvelmind_imu(msg_pos_imu):   
    global  seq_init
# define header 
    imu_out.header.seq = seq_init 
    seq_init += 1
    imu_out.header.stamp = rospy.Time.now()
    imu_out.header.frame_id = 'base_link'


#imu_angular velocity
    imu_out.angular_velocity.x = msg_pos_imu.gyro_x
    imu_out.angular_velocity.y = msg_pos_imu.gyro_y
    imu_out.angular_velocity.z = msg_pos_imu.gyro_z
    imu_out.angular_velocity_covariance = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#imu_angular velocity
    imu_out.linear_acceleration.x = msg_pos_imu.acc_x
    imu_out.linear_acceleration.y = msg_pos_imu.acc_y
    imu_out.linear_acceleration.z = msg_pos_imu.acc_z
    imu_out.linear_acceleration_covariance = [0, 0, 0, 0, 0, 0, 0, 0, 0]  

    pub.publish(imu_out)

if __name__ =='__main__':
    rospy.init_node('remap_pose_mean_imu')

    rate = rospy.Rate(10)
    sub = rospy.Subscriber("/hedge2/hedge_imu_raw", hedge_imu_raw , callback_marvelmind_imu)
    pub = rospy.Publisher("/imu_marvelmind_with_covariance", Imu, queue_size=10)

    rospy.spin()