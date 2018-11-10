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
	
	port = 5801
	
	sock.bind((host,port))
	
	sock.listen(5)
	
	while True:
		c, addr = sock.accept()
		print 'Got connection from', addr
		msg = c.recv(1024)
		print msg
		c.close()
		
if __name__ == '__main__':
	try:
		getMsg()
	except rospy.ROSInterruptException:
		pass
