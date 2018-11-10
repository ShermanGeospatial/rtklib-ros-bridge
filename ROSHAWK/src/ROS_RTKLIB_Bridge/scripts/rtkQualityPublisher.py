#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
import socket
from sensor_msgs.msg import Imu, NavSatFix, NavSatStatus
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point, Pose, PoseStamped
from ROSsocket1.msg import rtklib

class RtkQualityPublisher(class):
	
	def __init__(self,x,y,z,name):
		
		rospy.init_node('rtklib_publisher')
		
		self.rtkStatic_pub = rospy.Publisher('rtk_static_quality', NavSatFix)
		self.outfile = open(name + '_' + str(rospy.Time.now()), 'w')
		
		rospy.Subscriber('rtk_static', rtklib, self.compute_quality)
		
	def compute_quality(self,data):
		
		
		
if __name__ == '__main__':
	
	#Nodes initialized with coordinates computed using the NRCAN PPP server
	nodeGRAC0 = RtkAnalysisPublisher(4581708.191,556132.845,4389341.398)
	
	rospy.spin()
