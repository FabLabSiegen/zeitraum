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
	presentationController = None

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

	def isPresentationRunning(self):
		running = False
		if self.doc != None:
			presentation = self.doc.getPresentation()
			presentation.start()

			timeout = time.time() + 10 # 10 seconds
			while not presentation.isRunning():
				if time.time() > timeout:
					running = False


			self.presentationController = presentation.getController()
			running = True
		return running

	def gotoSlide(self, i):
		if self.presentationController != None:
			self.presentationController.gotoSlideIndex(i)
		else:
			self.connect()
			self.isPresentationRunning()

	def getNumTotalSlides(self):
		if self.presentationController != None:
			return self.presentationController.getSlideCount()
		else:
			self.connect()
			selt.isPresentationRunning()

beamer = Presentation("192.168.1.11", "2002")
if not beamer.isPresentationRunning():
	print("Beamer Presentation not running!")

monitor1 = Presentation("192.168.1.12", "2002")
if not beamer.isPresentationRunning():
	print("Monitor1 Presentation not running!")

monitor2 = Presentation("192.168.1.13", "2002")
if not beamer.isPresentationRunning():
	print("Monitor2 Presentation not running!")

numSlides = beamer.getNumTotalSlides()
slide = 0
language = 0
numLanguages = 3
languagePins = [0, 1, 2]

while(True):
	try:
		inputNum = int(input("Slide: "))
		if inputNum in languagePins:
			language = inputNum
			print("Changing language to " + str(language))
		else:
			slide = inputNum - numLanguages
			print("Changing slide to " + str(slide))
		changeToSlide = (language * numSlides) + slide
		beamer.gotoSlide(changeToSlide)
		monitor1.gotoSlide(changeToSlide)
		monitor2.gotoSlide(changeToSlide)
	except Exception:
		print(str(sys.exc_info()))
	pass
