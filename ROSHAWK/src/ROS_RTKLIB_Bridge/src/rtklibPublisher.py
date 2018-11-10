#!/usr/bin/env python

import rospy
import roslib
import numpy as np
from std_msgs.msg import String
import socket
from sensor_msgs.msg import Imu, NavSatFix, NavSatStatus
from ROSsocket1.msg import rtklib

#This class is designed to test the three different RTK Processing Modes in
#RTKRCV, convert them into ECEF coordinates, store the data into their rtklib 
#ROS message and publish the message over the ROS environment
class RtklibPublisher(object):
	
	#RtklibPublisher Node Constructor
	def __init__(self):
		
		#Initialize the ROS Node
		rospy.init_node('rtklib_publisher')
		
		#Initialize and store the ROS Topics
		self.static_pub = rospy.Publisher('static', rtklib, queue_size=2)
		self.rtkStatic_pub = rospy.Publisher('rtk_static', rtklib, queue_size=2)
		self.rtkDynamic_pub = rospy.Publisher('rtk_dynamic', rtklib, queue_size=2)
		
		#Call the callback function
		self.callback()
		
	def callback(self):
		
		#Publish data at 1 Hz
		rate = rospy.Rate(1)
		
		#Define the RTKRCV server ports corresponding to each of the processing
		#Modes
		ports = [5801,5802,5803]
		sockets = []
		
		pubs = [self.static_pub, self.rtkStatic_pub, self.rtkDynamic_pub]
		
		#For each server, instantiate a socket and connect it to the server's 
		#port
		for i in ports:
			
			sock = socket.socket()
			host = socket.gethostname()
			sock.connect((host, i))
			sockets.append(sock)
		
		#WGS84 Parameters
		e2 = 6.69437999014e-3
		a = 6378137.0
		
		#At a rate of 1 hz, create an rtklib message for each socket and publish
		#the data over 
		while not rospy.is_shutdown():
			
			#For each processing mode
			for i in range(len(sockets)):
				
				#Create and RTKLIB and a NavSatFix data structure
				rtk = rtklib()
				navsat = NavSatFix()
				
				#Set the data structure header time to the current system time
				navsat.header.stamp = rospy.Time.now()
				rtk.header.stamp = rospy.Time.now()	
				
				#Get the position message from the RTKRCV server
				msgStr = sockets[i].recv(1024)
			
				#Split the message
				msg = msgStr.split()
				
				#Save the latitude, longitude and ellipsoid height
				navsat.latitude = float(msg[2])
				navsat.longitude = float(msg[3])
				navsat.altitude = float(msg[4])
				
				#Save the position covariance
				navsat.position_covariance = [float(msg[7]),float(msg[10]),float(msg[12]),float(msg[10]),float(msg[8]),float(msg[11]),float(msg[12]),float(msg[11]),float(msg[9])]
				navsat.position_covariance_type = NavSatFix.COVARIANCE_TYPE_KNOWN
				
				#Compute the radius of curvature in the 
				N = 1.0*a/np.sqrt(1-e2*(np.sin(float(msg[2])*np.pi/180.0)**2))
				
				#Compute and store the ECEF position
				rtk.x =  (N+float(msg[4]))*np.cos(float(msg[2])*np.pi/180.0)*np.cos(float(msg[3])*np.pi/180.0)
				rtk.y = (N+float(msg[4]))*np.cos(float(msg[2])*np.pi/180.0)*np.sin(float(msg[3])*np.pi/180.0)
				rtk.z = (N*(1-e2)+float(msg[4]))*np.sin(float(msg[2])*np.pi/180.0)
				rtk.delay = float(msg[13])
				rtk.ftest = float(msg[14])
				
				#Store the NavSatFix data
				rtk.state = navsat
				
				pubs[i].publish(rtk)
				
			rate.sleep()

#Main Function
if __name__ == '__main__':
	
	node = RtklibPublisher()
	rospy.spin()
