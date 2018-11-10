import Tkinter
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import socket
import rospy
from std_msgs.msg import String

#Visualization application for the static rtk case
class App:
	def __init__(self,master):
		
		#This was a final test to demonstrate that the software can be extended
		#To include the GUI directly within the positioning node
		rospy.init_node('Bamn')
		
		#Initialize the publisher
		self.bamn_pub = rospy.Publisher('Bamn', String, queue_size = 30)
		
		
		#The Reference Rover and Base coordinates were hard coded in order to 
		#avoid "over engineering" as the intention is to eventually have this
		#information input in an "elegant" fasion
		self.ref = np.array([4641949.35634791,1393045.6421954,4133287.64031007])
		self.base = np.array([4641952.63326322,1393062.95794337,4133278.25700797])
		
		#Store a reference to the GUI within the obhject
		self.master = master
		
		#Create the network socket and bind to the "static_rtk" port		
		self.sock = socket.socket()
		host = socket.gethostname()
		port = 5802
		self.sock.connect((host,port))
		
		#Create 2 buttons and place them at the top of the GUI. These buttons 
		#change the view between baseline mode and rover mode
		buttonFrame = Tkinter.Frame(master)
		
		self.roverButton = Tkinter.Button(buttonFrame,text='Rover Mode',command=self.roverMode)
		self.roverButton.pack(side="left")
		
		self.baselineButton = Tkinter.Button(buttonFrame,text='Baseline Mode',command=self.baselineMode)
		self.baselineButton.pack(side='left')
		
		buttonFrame.pack()
		
		#Initialize the application to rover mode
		self.mode = 'rover'
		
		self.frame = Tkinter.Frame(master)
		self.frame.pack()
		
		#Create a text box to display the rover coordinates
		self.text = Tkinter.Text(master, height=5, width=20)
		output = 'x = 0\n\ny = 0\n\nz = 0'
		self.text.insert(Tkinter.END, output)
		self.text.pack(side='left')
		
		#Create the data structures to store the epoch-to-epoch results
		self.pos = [[],[],[]]
		self.dPos = [[],[],[]]
		
		self.bl = [[],[],[]]
		self.dBL = [[],[],[]]
		
		self.Cx = [[],[],[],[],[],[]]
		
		self.gpst = []
		self.ftest = []
		self.delay = []
		self.gdop = []
		
		#Create blank plots and store them as references within the object		
		self.fig = Figure()
		
		self.plt = []
		
		for i in range(231,237):
			
			self.plt.append(self.fig.add_subplot(i))
		
		#Add the plots to the application and add the toolbar at the bottom
		#In order to interact with the plots (e.g. zoom and translate the plots)
		self.canvas = FigureCanvasTkAgg(self.fig,master=self.master)
		self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
		self.toolbar = NavigationToolbar2TkAgg( self.canvas, master )
		self.toolbar.update()
		self.canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
	
	#This method switches the application's mode to rover mode, which is then
	#interpreted by the rtkPlot function to plot the rover state details
	def roverMode(self):
		
		self.mode = 'rover'

	#This method switches the application's mode to baseline mode, which is 
	#then interpreted by the rtkPlot function to plot the baseline state details
	def baselineMode(self):
		
		self.mode = 'baseline'
	
	#At each measurement epoch, get the output from RTKRCV, parse it, and use it
	#To compute the different quantities that are displayed	
	def getData(self):

		#WGS84 Parameters
		e2 = 6.69437999014e-3
		a = 6378137.0
		
		#Receive the message from RTKRCV
		msgStr = self.sock.recv(1024)
		
		#Parse the message
		msg = msgStr.split()
	
		#Compute the radius of curvature
		N = 1.0*a/np.sqrt(1-e2*(np.sin(float(msg[2])*np.pi/180.0)**2))
		
		#ECEF XYZ Pose		
		self.pos[0].append((N+float(msg[4]))*np.cos(float(msg[2])*np.pi/180.0)*np.cos(float(msg[3])*np.pi/180.0))
		self.pos[1].append((N+float(msg[4]))*np.cos(float(msg[2])*np.pi/180.0)*np.sin(float(msg[3])*np.pi/180.0))
		self.pos[2].append((N*(1-e2)+float(msg[4]))*np.sin(float(msg[2])*np.pi/180.0))
		
		#Reference Coordinate Discrepancies
		self.dPos[0].append(self.pos[0][-1] - self.ref[0])
		self.dPos[1].append(self.pos[1][-1] - self.ref[1])
		self.dPos[2].append(self.pos[2][-1] - self.ref[2])
		
		#Baseline and baseline discrepancy (same as reference coord discrepancy)
		self.bl[0].append(self.pos[0][-1] - self.base[0])
		self.bl[1].append(self.pos[1][-1] - self.base[1])
		self.bl[2].append(self.pos[2][-1] - self.base[2])
		self.dBL[0].append(self.bl[0][-1] - (self.ref[0] - self.base[0]))
		self.dBL[1].append(self.bl[1][-1] - (self.ref[1] - self.base[1]))
		self.dBL[2].append(self.bl[2][-1] - (self.ref[2] - self.base[2]))
		
		#Covariance matrix output from RTKRCV
		self.Cx[0].append(float(msg[7]))
		self.Cx[1].append(float(msg[8]))
		self.Cx[2].append(float(msg[9]))
		self.Cx[3].append(float(msg[10]))
		self.Cx[4].append(float(msg[11]))
		self.Cx[5].append(float(msg[12]))
		
		#Norm of the covariance matrix diagonal elements
		self.gdop.append(np.sqrt(self.Cx[0][-1]*self.Cx[0][-1] + self.Cx[1][-1]*self.Cx[1][-1] + self.Cx[2][-1]*self.Cx[2][-1]))

		#Store other GNSS relevant data
		self.gpst.append(float(msg[1]))
		self.ftest.append(float(msg[14]))
		self.delay.append(float(msg[13]))
		
		#Test out publishing over a rostopic without using a ROS based loop
		self.bamn_pub.publish("BAMN")
		
		#Call the function again after 1000 ms
		self.master.after(1000,self.getData)
		
	#At each measurement epoch, replot the requested quantities with the newly
	#acquired values
	def rtkPlot(self):
	
		#If Rover mode is selected
		if self.mode == 'rover':
			
			#Datasets to be plotted and their labels
			datasets = [self.dPos[0], self.dPos[1], self.dPos[2], self.gdop, self.ftest, self.delay]
			titles = ['dx', 'dy', 'dz', 'GDOP', 'ftest', 'delay']
			
			#Plot each dataset
			for i in range(len(datasets)):
				
				self.plt[i].cla()
				self.plt[i].plot(range(len(datasets[i])),datasets[i])
				self.plt[i].set_title(titles[i])
			
			#Display rover coordinates
			output = 'x = ' + str(self.pos[0][-1]) + '\n\ny = ' + str(self.pos[1][-1]) + '\n\nz = ' + str(self.pos[2][-1])
			self.text.delete(1.0,Tkinter.END)
			self.text.insert(Tkinter.END, output)
			self.text.pack(side='left')
			
		#If baseline mode is selected	
		if self.mode == 'baseline':
			
			#Datasets to be plotted and their labels
			datasets = [self.bl[0], self.bl[1], self.bl[2], self.dBL[0], self.dBL[1], self.dBL[2]]
			titles = ['DX', 'DY', 'DZ', 'dDX', 'dDY', 'dDZ']
			
			#Plot each dataset
			for i in range(len(datasets)):
				
				self.plt[i].cla()
				self.plt[i].plot(range(len(datasets[i])),datasets[i])
				self.plt[i].set_title(titles[i])
			
			#Display the baseline info			
			output = 'x = ' + str(self.pos[0][-1]) + '\n\ny = ' + str(self.pos[1][-1]) + '\n\nz = ' + str(self.pos[2][-1])
			self.text.delete(1.0,Tkinter.END)
			self.text.insert(Tkinter.END, output)
			self.text.pack(side='left')
				
		#Draw the new plots
		self.canvas.draw()
		
		#Call the plotting function every seconds
		self.master.after(1000,self.rtkPlot)
		
#Main function
root = Tkinter.Tk()
root.wm_title("RTK Data Analyzer")
app = App(root)
root.after(1000,app.getData)
root.after(1000,app.rtkPlot)
root.mainloop()
