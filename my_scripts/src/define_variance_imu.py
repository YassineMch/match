#! /usr/bin/env python3

# Diesen Script berechnet die Variance der einzelnen variabeln für die Covarianzmatrix 
# daten werden aus dem Stationary Zustand ausgewertet und der Noise des System damit ermittelt


import rospy
from marvelmind_nav.msg import  hedge_imu_raw
import numpy as np
import time
import statistics

variance_yaw=[]


def callback_marvelmind_imu(msg):   
    global variance_yaw, mean_yaw_var

    #poition
    variance_yaw.append(msg.gyro_z / 1000)
    # covariance matrix with variance data from stationary state of the Beacons 
    mean_yaw_var = np.mean (variance_yaw)
    
if __name__ =='__main__':
    rospy.init_node('define_variance_imu')
    sub=rospy.Subscriber("/hedge2/hedge_imu_raw", hedge_imu_raw, callback_marvelmind_imu)
    time.sleep(5)
    
    variance__yaw= statistics.variance(variance_yaw)
    print (variance__yaw)
