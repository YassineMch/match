#!/usr/bin/env python3
import rospy
import tf_conversions
import tf2_ros
from geometry_msgs.msg import PoseWithCovarianceStamped
import geometry_msgs.msg 

def callback_marvelmind(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'world'
    t.child_frame_id = 'map'
    t.transform.translation.x = 2
    t.transform.translation.z = 0.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0.5)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    rospy.Subscriber("/marvelmind_transformed", PoseWithCovarianceStamped, callback_marvelmind)
rospy.spin()