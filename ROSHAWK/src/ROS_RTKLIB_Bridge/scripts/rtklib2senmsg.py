#!/usr/bin/env python

import rospy
import roslib

from sensor_msgs.msg import Imu, NavSatFix, NavSatStatus
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point, Pose

class rtkpos:
	
	def __init__(self):
		
		rospy.init_node('rtkNav', anonymous=True)
		
		self.pos_pub = rospy.Publisher("/rtklib/nav_sat_fix/position", NavSatFix)
		
		rospy.Subscriber("/rtklib/latitude", String, self.latitude)
		rospy.Subscriber("/rtklib/longitude", String, self.longitude)
		rospy.Subscriber("/rtklib/height", String, self.height)

		rospy.loginfo(self.latitude)
		
		rospy.spin()
