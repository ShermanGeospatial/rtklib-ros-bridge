#!/usr/bin/env python

#Connects to an RTKRCV server stream which outputs an XYZ-ECEF RTK solution. 
#This solution message is parsed into its component and transmitted over 
#individual ROS topics

import rospy
from std_msgs.msg import String
import socket
from sensor_msgs.msg import Imu, NavSatFix, NavSatStatus
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point, Pose

def getMsg():
	
	navsat = NavSatFix()
	navsat.header.stamp = rospy.Time.now()
	#Create a list of ROSTopic names
	topicList = ['dow', 'gpst', 'latitude', 'longitude', 'height', 'check', 'sats', 
	'dxx', 'dyy', 'dzz', 'dxy', 'dyz', 'dxz', 'delay', 'ftest']
	
	#Create an empty array of ROS publishers
	pub = []
	
	for i in range(len(topicList)):
		
		#Create a publisher for each topic
		pub.append(rospy.Publisher('/rtklib/' + topicList[i], String, queue_size=30))
		
	#Initialize the RTKLIB ROS node	
	rospy.init_node('rtklib_message', anonymous=True)
	
	#Define the publishing frequency of the node
	rate = rospy.Rate(10)
	
	#Create a socket
	sock = socket.socket()
	
	#Get the address of the local host
	host = socket.gethostname()
	
	#Connect to the RTKRCV server that is bound to port xxxx
	port = 5801
	sock.connect((host,port))
	
	while not rospy.is_shutdown():
		
		#Get the position message from the RTKRCV server
		msgStr = sock.recv(1024)
		
		#Split the message
		msg = msgStr.split()
		
		for i in range(len(msg)):
			
			#Publish over each topic
			pub[i].publish(msg[i])
		
		rate.sleep()
		
if __name__ == '__main__':
	try:
		#Run the publisher
		getMsg()
	except rospy.ROSInterruptException:
		pass
