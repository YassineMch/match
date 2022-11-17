#! /usr/bin/env python3

# Diesen Script berechnet die Variance der einzelnen variabeln für die Covarianzmatrix 
# daten werden aus dem Stationary Zustand ausgewertet und der Noise des System damit ermittelt

import rospy
import math
import time
import statistics
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf import transformations
import numpy as np

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

def callback_marvelmind_pos(msg):   
    global x, y, z, roll, pitch, yaw, w, quat, euler

    #poition
    x.append(msg.pose.pose.position.x)
    y.append(msg.pose.pose.position.y)
    z.append(msg.pose.pose.position.z)
    
    #orientation quaternion
    roll.append(msg.pose.pose.orientation.x)
    pitch.append(msg.pose.pose.orientation.y)
    yaw.append(msg.pose.pose.orientation.z)
    w.append(msg.pose.pose.orientation.w)
    
    
if __name__ =='__main__':
    rospy.init_node('define_variance')
    sub=rospy.Subscriber("/position_marvelmind_with_covariance", PoseWithCovarianceStamped, callback_marvelmind_pos)
    
    time.sleep(10)
    
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
    
    quater = [mean_roll, mean_pitch, mean_yaw, mean_w]
    euler = transformations.euler_from_quaternion (quater)
    
    radx = euler[0]
    rady = euler[1]
    radz = euler[2]
    
    degx = ((euler[0]/(math.pi))*180)
    degy = ((euler[1]/(math.pi))*180)
    degz = ((euler[2]/(math.pi))*180)
    
    print (degx, degy, degz)
    print ('x =', mean_x,'y =', mean_y, 'z =', mean_z, 'yaw =', radz )
    print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
