#!/usr/bin/env python3

import math
import rospy
from marvelmind_nav.msg import hedge_imu_fusion
from tf import transformations

quater = []
euler = []
euler_tr = []

def callback_marvelmind_pos(msg_pos):   
    global  quater, euler,euler_tr 

    quater = [msg_pos.qx, msg_pos.qy, msg_pos.qz, msg_pos.qw]
    euler = transformations.euler_from_quaternion (quater)
    degx=((euler[0]/(math.pi))*180)
    degy=((euler[1]/(math.pi))*180)
    degz=((euler[2]/(math.pi))*180)
    print('degx',degx, 'degy', degy,'degz' ,degz)

if __name__ =='__main__':
    rospy.init_node('quaternion_to_euler')
    
    sub = rospy.Subscriber("/hedge1/hedge_imu_fusion", hedge_imu_fusion , callback_marvelmind_pos)

    rospy.spin()

print (euler)