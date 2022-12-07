#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
class path:

    def __init__(self):
        
        # register this function to be called on shutdown
        rospy.on_shutdown(self.cleanup)

        # publish to cmd_vel
        self.pub = rospy.Publisher('cmd_vel', Twist)

        # give the node/publisher time to connect
        rospy.sleep(1)
        r = rospy.Rate(100)
        vel_lin = 0.4 #0.4 #0.6 #0.7 #0.8
        vel_ang = 1.57
        vel_ang_2 = 1.57*2
        t_rot = 250
        t_rot_2 = 2500
        while not rospy.is_shutdown():

            # create a Twist message, robot moves forward direction Hiwi Raum
            twist = Twist()
            twist.linear.x = vel_lin
            for i in range(700):   # 1390 #927  #796 #697   #time adjustment: current vel/new vel*current range
                self.pub.publish(twist)
                r.sleep()
                
            twist = Twist()
            twist.angular.z = vel_ang     # 45 deg/s * 2sec = 90 degrees (had to test it cause it didnt work with 200)
            for i in range(t_rot):         
                self.pub.publish(twist)
                r.sleep()

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.pub.publish(twist)

if __name__=="__main__":
    rospy.init_node('movetogoal')
    path()