from javax.swing import JFrame, JLabel, ImageIcon
from java.awt import BorderLayout, Toolkit
from datetime import date
from org.python.core import imp
import sys


def getImage(url):
	return Toolkit.getDefaultToolkit().getImage(sys.classLoader.getResource(url))

		

class MainWindow(JFrame):
	def __init__(self):
		self.title = 'Dracula!'
		self.size = (300,200)
		self.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
		self.setLayout(BorderLayout())

		image = JLabel(ImageIcon(getImage("resources/dracula.png")))
		self.add(image, BorderLayout.CENTER)

		todaysdate = JLabel("Todays date is "+str(date.today()))
		self.add(todaysdate, BorderLayout.SOUTH)

		self.visible = True



sys.setClassLoader(imp.getClassLoader())
MainWindow()
