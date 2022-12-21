#! /usr/bin/env python3

# Diesen Script berechnet die Variance der einzelnen variabeln für die Covarianzmatrix 
# daten werden aus dem Stationary Zustand ausgewertet und der Noise des System damit ermittelt


import rospy
from marvelmind_nav.msg import  hedge_imu_raw
import numpy as np
import time
import statistics

variance_yaw=[]
yaw_accel =[]

def callback_marvelmind_imu(msg):   
    global yaw_accel, mean_yaw_accel
    # angular accel
    yaw_accel.append(msg.gyro_z / 1000)
    # covariance matrix with variance data from stationary state of the Beacons 
    mean_yaw_accel = np.mean (yaw_accel)
    
if __name__ =='__main__':
    rospy.init_node('define_variance_imu')
    sub=rospy.Subscriber("/hedge2/hedge_imu_raw", hedge_imu_raw, callback_marvelmind_imu)
    time.sleep(5)
    
    variance_yaw= statistics.variance(yaw_accel)
    print (variance_yaw)
