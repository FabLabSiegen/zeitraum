#!/bin/python3

import uno
import time
import sys

localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)

class Presentation:
	ip = None
	port = None
	doc = None
	presentation_controller = None

	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.connect()

	def connect(self):
		try:
			ctx = resolver.resolve("uno:socket,host=" + self.ip + ",port=" + self.port + ";urp;StarOffice.ComponentContext")
			smgr = ctx.ServiceManager
			desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
			self.doc = desktop.getCurrentComponent()
			print(self.ip + " | connected.")
		except Exception:
			print(self.ip + " | " + str(sys.exc_info()))

	def presentationRunning(self):
		running = False
		if self.doc != None:
			presentation = self.doc.getPresentation()
			presentation.start()

			timeout = time.time() + 10 # 10 seconds
			while not presentation.isRunning():
				if time.time() > timeout:
					running = False


			self.presentation_controller = presentation.getController()
			running = True
		return running

	def gotoSlide(self, i):
		if self.presentation_controller != None:
			self.presentation_controller.gotoSlideIndex(i)
		else:
			self.connect()
			self.presentationRunning()

beamer = Presentation("192.168.1.11", "2002")
if not beamer.presentationRunning():
	print("Beamer Presentation not running!")

monitor1 = Presentation("192.168.1.12", "2002")
if not beamer.presentationRunning():
	print("Monitor1 Presentation not running!")

monitor2 = Presentation("192.168.1.13", "2002")
if not beamer.presentationRunning():
	print("Monitor2 Presentation not running!")

while(True):
	try:
		slide = int(input("Slide: "))
		beamer.gotoSlide(slide)
		monitor1.gotoSlide(slide)
		monitor2.gotoSlide(slide)
	except Exception:
		print(str(sys.exc_info())
