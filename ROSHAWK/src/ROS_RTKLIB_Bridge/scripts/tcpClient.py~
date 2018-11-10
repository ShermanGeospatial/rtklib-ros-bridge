#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import socket

def getMsg():
	
	pub = rospy.Publisher('tcpMsg', String, queue_size=30)
	
	rospy.init_node('tcpMsg', anonymous=True)
	
	rate = rospy.Rate(10)
	
	sock = socket.socket()
	
	host = socket.gethostname()
	
	port = 5800
	
	sock.connect((host,port))

	while not rospy.is_shutdown():
		
		msg = sock.recv(1024)		
		rospy.loginfo(msg)		
		pub.publish(msg)		
		rate.sleep()
		
if __name__ == '__main__':
	try:
		getMsg()
	except rospy.ROSInterruptException:
		pass
