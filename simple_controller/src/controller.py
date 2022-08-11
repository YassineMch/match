#!/usr/bin/env python3


# We always import roslib, and load the manifest to handle dependencies
import rospy

# recall: robots generally take base movement commands on a topic 
#  called "cmd_vel" using a message type "geometry_msgs/Twist"
from geometry_msgs.msg import Twist
class square:
    """ This example is in the form of a class. """

    def __init__(self):
        """ This is the constructor of our class. """
        # register this function to be called on shutdown
        rospy.on_shutdown(self.cleanup)

        # publish to cmd_vel
        self.pub = rospy.Publisher('cmd_vel', Twist)
        # give our node/publisher a bit of time to connect
        rospy.sleep(1)

        # use a rate to make sure the bot keeps moving
        r = rospy.Rate(100)

        # go forever!
        while not rospy.is_shutdown():
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = 0.30
            for i in range(1850):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            # create a twist message, fill it in to turn
            twist = Twist()
            twist.angular.z = 1.57/2    # 45 deg/s * 2sec = 90 degrees
            for i in range(255):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = 0.30
            for i in range(1020):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            # create a twist message, fill it in to turn
            twist = Twist()
            twist.angular.z = 1.57/2    # 45 deg/s * 2sec = 90 degrees
            for i in range(255):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = 0.30
            for i in range(547):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
            # create a twist message, fill it in to turn
            twist.angular.z = 1.57/2    # 45 deg/s * 2sec = 90 degrees
            for i in range(255):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = 0.30
            for i in range(352):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
            # create a twist message, fill it in to turn
            twist.angular.z = -1.57/2    # 45 deg/s * 2sec = 90 degrees
            for i in range(255):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = 0.30
            for i in range(1345):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
            # create a twist message, fill it in to turn
            twist.angular.z = 1.57/2    # 45 deg/s * 2sec = 90 degrees
            for i in range(255):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = 0.30
            for i in range(600):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
            twist = Twist()
                # create a twist message, fill it in to turn
            twist.angular.z = 1.57/2    # 45 deg/s * 2sec = 90 degrees
            for i in range(255):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.pub.publish(twist)

if __name__=="__main__":
    rospy.init_node('square')
    square()