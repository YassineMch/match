#!/usr/bin/env python3 

import rospy 
from geometry_msgs.msg import Twist

x_linear= 0.0
y_linear = 0.0
z_linear = 0.0
x_angular = 0.0
y_angular = 0.0
z_angular = 0.0
now = 0.0

vel = 0.4

rospy.init_node("path_l_shape")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

command = Twist()

rate = rospy.Rate(100)
duration = 4
now = rospy.get_rostime().to_sec()
start_time = now
real_time = rospy.get_rostime().to_sec()
while not rospy.is_shutdown():
    
    if (real_time-start_time <= duration):
        real_time = rospy.get_rostime().to_sec()
        
        command.linear.x = vel
        command.linear.y = 0.0
        command.linear.z = 0.0
        command.angular.x = 0.0
        command.angular.y = 0.0
        command.angular.z = 0.0
        pub.publish(command)
        rate.sleep()
