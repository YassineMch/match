#! /usr/bin/env python3

# Diesen Script berechnet die Variance der einzelnen variabeln für die Covarianzmatrix 
# daten werden aus dem Stationary Zustand ausgewertet und der Noise des System damit ermittelt

import rospy
import time
import statistics
from geometry_msgs.msg import PoseWithCovarianceStamped
#import numpy as np

x = []
y = []
z = []
yaw = []


def callback_marvelmind_pos(msg):   
    global x, y, z, yaw
    
    
    x.append(msg.pose.pose.position.x)
    y.append(msg.pose.pose.position.y)
    z.append(msg.pose.pose.position.z)
    yaw.append(msg.pose.pose.orientation.w)
    
    
    
if __name__ =='__main__':
    rospy.init_node('define_variance')
    sub=rospy.Subscriber("/position_marvelmind_with_covariance", PoseWithCovarianceStamped, callback_marvelmind_pos)
    
    time.sleep(10)
    
    variance_x = statistics.variance(x)
    variance_y = statistics.variance(y)
    variance_z = statistics.variance(z)
    variance_yaw = statistics.variance (yaw)
    
    #print ('x =', x)
    print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
