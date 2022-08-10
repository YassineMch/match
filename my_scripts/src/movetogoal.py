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
        vel_lin = 0.30
        vel_ang = math.pi/2


        while not rospy.is_shutdown():

            # create a Twist message, robot moves forward direction Hiwi Raum
            twist = Twist()
            twist.linear.x = vel_lin
            for i in range(1850):         
                self.pub.publish(twist)
                r.sleep()
            # create a twist message, robot turns 
            twist = Twist()
            twist.angular.z = vel_ang     # 45 deg/s * 2sec = 90 degrees (had to test it cause it didnt work with 200)
            for i in range(255):         
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, robot moves forward direction Match Tower
            twist = Twist()
            twist.linear.x = vel_lin
            for i in range(1020):         
                self.pub.publish(twist)
                r.sleep()
            # create a twist message, robot turns 
            twist = Twist()
            twist.angular.z = vel_ang     
            for i in range(255):         
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, robot moves forward direction desck
            twist = Twist()
            twist.linear.x = vel_lin
            for i in range(547):         
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
            # create a twist message, robot turns 
            twist.angular.z = vel_ang     
            for i in range(255):         
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, robot moves forward direction Werkstatt_1
            twist = Twist()
            twist.linear.x = vel_lin
            for i in range(352):         
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
            # create a twist message, robot turns 
            twist.angular.z = vel_ang    
            for i in range(255):         
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, robot moves forward direction Gate of the Hall
            twist = Twist()
            twist.linear.x = vel_lin
            for i in range(1345):         
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
            # create a twist message, robot turns 
            twist.angular.z = vel_ang     
            for i in range(255):         
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, robot moves forward direction Werkstatt_2
            twist = Twist()
            twist.linear.x = vel_lin
            for i in range(600):         
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
                # create a twist message, robot turns
            twist.angular.z = vel_ang     
            for i in range(255):         
                self.pub.publish(twist)
                r.sleep()
                break
        print('robot has achieved one round with a linear velocity v_x_lin = ', vel_lin , 'and an angular velocity v_x_ang=', vel_ang)

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.pub.publish(twist)

if __name__=="__main__":
    rospy.init_node('movetogoal')
    path()