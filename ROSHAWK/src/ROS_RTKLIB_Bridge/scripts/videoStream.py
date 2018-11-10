import cv2

cap = cv2.VideoCapture('192.168.0.104:8081')
print cap
while(True):
	ret, frame = cap.read()
	
	if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('gray',grayResize)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
