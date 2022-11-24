#! /usr/bin/env python3

# Diesen Script berechnet die Variance der einzelnen variabeln für die Covarianzmatrix 
# daten werden aus dem Stationary Zustand ausgewertet und der Noise des System damit ermittelt

import rospy
import math
import time
import statistics
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
from tf import transformations
import numpy as np

seq_init = 0 
x = []
y = []
z = []
roll = []
pitch =[]
yaw = []
w = []
quat= []
euler= []
yaw_deg =[]
pose_out_var= PoseWithCovarianceStamped()

def callback_marvelmind_pos(msg):   
    global x, y, z, roll, pitch, yaw, w, quat, euler, variance_x, variance_y, variance_z, variance_yaw, mean_x, mean_y, mean_z, mean_roll, mean_yaw, mean_pitch, mean_w, seq_init,radz

    #poition
    x.append(msg.position.x)
    y.append(msg.position.y)
    z.append(msg.position.z)
    
    #orientation quaternion
    roll.append(msg.orientation.x)
    pitch.append(msg.orientation.y)
    yaw.append(msg.orientation.z)
    w.append(msg.orientation.w)
    
    mean_x = np.mean(x)+ 1.224
    mean_y = np.mean(y)+ 0.3037
    mean_z = np.mean(z)
    
    mean_roll = np.mean(roll)
    mean_pitch = np.mean(pitch)
    mean_yaw = np.mean(yaw)
    mean_w = np.mean(w)
    
    quat = [mean_roll, mean_pitch, mean_yaw,mean_w]
    euler = transformations.euler_from_quaternion (quat)
    radz = euler[2]
    
    pose_out_var.header.seq = seq_init
    seq_init += 1
    
    pose_out_var.header.stamp = rospy.Time.now()
    pose_out_var.header.frame_id = 'map'
    
    pose_out_var.pose.pose.position.x = mean_x
    pose_out_var.pose.pose.position.y = mean_y
    pose_out_var.pose.pose.position.z = mean_z
    
    pose_out_var.pose.pose.orientation.x = mean_roll
    pose_out_var.pose.pose.orientation.y = mean_pitch
    pose_out_var.pose.pose.orientation.z = mean_yaw 
    pose_out_var.pose.pose.orientation.w = mean_w
    
    # covariance matrix with variance data from stationary state of the Beacons 

    
if __name__ =='__main__':
    rospy.init_node('define_variance')
    sub=rospy.Subscriber("/middle_point", Pose, callback_marvelmind_pos)
    pub=rospy.Publisher("/pose_mean", PoseWithCovarianceStamped, queue_size=10)
    time.sleep(5)
    
    rospy.set_param("/amcl/initial_pose_x",float(pose_out_var.pose.pose.position.x))
    rospy.set_param("/amcl/initial_pose_y",float(pose_out_var.pose.pose.position.y))
    #rospy.set_param("/initial_pose_a",euler[2])
    
    pub.publish(pose_out_var)
