# Mix of Python and Java Imports
from javax.swing import JFrame, JLabel, ImageIcon
from java.awt import BorderLayout
from datetime import date
from org.python.core import imp
import sys

# The basic Swing GUI
class MainWindow(JFrame):
	def __init__(self):
		self.title = 'Dracula!'
		self.size = (300,200)
		self.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
		self.setLayout(BorderLayout())
		
		image = ImageIcon(getResource("resources/dracula.png"))
		# Standard Image load, except getResource must be used to access
		# resources within the Jar file.
		label = JLabel(image)
		self.add(label, BorderLayout.CENTER)

		todaysdate = JLabel("Todays date is "+str(date.today()))
		# Get current date using Python's Standard datetime module
		self.add(todaysdate, BorderLayout.SOUTH)
		self.visible = True


if __name__ == "JythonApplication":
	# Set the ClassLoader for use of getResource
	sys.setClassLoader(imp.getParentClassLoader())
	# Alias long function for cleaner code
	getResource = sys.classLoader.getResource
	# Initialise the GUI
	MainWindow()
