#! /usr/bin/env python3

# Diesen Script berechnet die Variance der einzelnen variabeln für die Covarianzmatrix 
# daten werden aus dem Stationary Zustand ausgewertet und der Noise des System damit ermittelt
 
import rospy
import time
import statistics
from geometry_msgs.msg import PoseStamped
#import numpy as np

x = []
y = []
z = []
yaw = []
x_1 = 0
y_1= 0
yaw_1= 0
angle = 0

def callback_marvelmind_pos(msg):   
    global x, y, z, yaw, x_1, y_1, z_1, angle
    
    x_1 = msg.pose.position.x
    y_1 = msg.pose.position.y
    z_1 = msg.pose.position.z
    
    x.append(msg.pose.position.x)
    y.append(msg.pose.position.y)
    z.append(msg.pose.position.z)
    yaw.append(msg.pose.orientation.w)
    
    
    
if __name__ =='__main__':
    rospy.init_node('define_variance')
    sub=rospy.Subscriber("/position_marvelmind", PoseStamped, callback_marvelmind_pos)
    
    time.sleep(10)
    
    variance_x = statistics.variance(x)
    variance_y = statistics.variance(y)
    variance_z = statistics.variance(z)
    variance_yaw = statistics.variance (yaw)
    
    
    print('variance x =', variance_x, 'variance y =', variance_y,  'variance z =', variance_z, 'variance yaw =', variance_yaw)
   