#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import socket

#This function executes continuously, receiving a message via TCP port 5800
#and publishing the data as a ROSTopic

def getMsg():
	
	#Create a ROS Publisher Object Instance
	pub = rospy.Publisher('tcpMsg', String, queue_size=30)
	
	#Initialize the ROS Node tcpMsg
	rospy.init_node('tcpMsg', anonymous=True)
	
	#Define the ROS Node publishing rate in Hz
	rate = rospy.Rate(10)

	#Create a new socket, get the localhost name, and define the TCP port to
	#connect to
	sock = socket.socket()	
	host = socket.gethostname()	
	port = 5800
	
	#Connect to the tcp 5800 on the localhost 
	sock.connect((host,port))

	#Loop until the shutdown command (ctrl-c) is detected, receive the message
	#over tcp port 5800 and publish it as the tcpMsg topic in ROS
	while not rospy.is_shutdown():
		
		msg = sock.recv(1024)		
		rospy.loginfo(msg)		
		pub.publish(msg)		
		rate.sleep()

#Main Function
if __name__ == '__main__':
	try:
		getMsg()
	except rospy.ROSInterruptException:
		pass
	
	
