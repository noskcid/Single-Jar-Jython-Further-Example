from java.awt import SystemTray, TrayIcon, Toolkit, PopupMenu, MenuItem
from javax.swing import JFrame
from java.lang import ClassLoader
from org.python.core import imp
import sys
import urllib
from external import foo

class AboutWindow(JFrame):
	def __init__(self):
		self.title = 'About'
		self.size = (300,200)
		self.defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE
		self.visible = True
		

class TrayApp(object):
	def __init__(self):
		sys.setClassLoader(imp.getClassLoader())
		self.tray = SystemTray.getSystemTray()
		self.icon = TrayIcon(Toolkit.getDefaultToolkit().getImage(sys.classLoader.getResource("resources/default.png")))
		#self.icon = TrayIcon(Toolkit.getDefaultToolkit().getImage("resources/default.png"))
		self.menu = PopupMenu("Menu")
		self.menu.add(MenuItem(foo(), actionPerformed=self.showAbout))
		self.menu.add(MenuItem(__name__))
		self.menu.add(MenuItem("-"))
		self.menu.add(MenuItem("Quit", actionPerformed=self.quit))
		self.icon.setPopupMenu(self.menu)
		self.tray.add(self.icon)

	def showAbout(self,event):
		AboutWindow()

	def quit(self,event):
		sys.exit(0)

if __name__ == "JythonApplication":
	TrayApp()
