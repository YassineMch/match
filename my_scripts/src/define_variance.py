#! /usr/bin/env python3

# Diesen Script berechnet die Variance der einzelnen variabeln für die Covarianzmatrix 
# daten werden aus dem Stationary Zustand ausgewertet und der Noise des System damit ermittelt

import rospy
import math
import time
import statistics
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
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
    global x, y, z, roll, pitch, yaw, w, quat, euler

    #poition
    x.append(msg.position.x)
    y.append(msg.position.y)
    z.append(msg.position.z)
    
    #orientation quaternion
    roll.append(msg.orientation.x)
    pitch.append(msg.orientation.y)
    yaw.append(msg.orientation.z)
    w.append(msg.orientation.w)
    
    
if __name__ =='__main__':
    rospy.init_node('define_variance')
    sub=rospy.Subscriber("/middle_point", Pose, callback_marvelmind_pos)
    pub=rospy.Publisher("/pose_mean", PoseWithCovarianceStamped, queue_size=10)
    time.sleep(20)
    
    variance_x = statistics.variance(x)
    variance_y = statistics.variance(y)
    variance_z = statistics.variance(z)
    variance_yaw = statistics.variance (yaw)
    
    mean_x = np.mean(x)+ 1.224
    mean_y = np.mean(y)+ 0.3037
    mean_z = np.mean(z)
    
    
    mean_roll = np.mean(roll)
    mean_pitch = np.mean(pitch)
    mean_yaw = np.mean(yaw)
    mean_w = np.mean(w)
    
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
    pose_out_var.pose.covariance = [variance_x, 0, 0, 0, 0, 0,
                                    0,variance_y, 0, 0, 0, 0,
                                    0, 0, variance_z, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 
                                    0, 0, 0, 0, 0, 0, 
                                    0, 0, 0, 0, 0, variance_yaw ]
    
    pub.publish(pose_out_var)
