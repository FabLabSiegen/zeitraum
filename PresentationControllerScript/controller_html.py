#!/bin/python3
import subprocess

#constants
numLanguages = 3#number after the last language pin number, first pin that shows a slide
languagePins = [0, 1, 2] # de, en, nl

#variables
language = "de"#current language, is an often changed variable in the code
slide = 0#current slide, is an often changed variable in the code

#function to rewrite the currentSlide.js file that defines what slide should be shown.
def writeFile():
	try:
		file = open("/home/pi/Desktop/share/zeitraum/Presentation_HTML/currentSlide.js", "w")
		file.write("var index = '" + str(slide) + "';\n")
		file.write("var lang = '" + str(language) + "';")
		file.close()
	except Exception:
		print("Unable to write file.")
		print(str(Exception))

#loop that goes and goes and goes, hopefully never stopping
while(True):
	try:
		inputString = input("Slide: ")#asks for a number
		if(inputString): #Checks if the String is empty or not, when two leonardos fire at the same time, say 15 and 7 then this can result in a 157 and an empty line, the empty line made this go boom
			inputNum = int(inputString)#converts the input to a number, since only numbers are input, this should not crash
			if inputNum in languagePins:
				if inputNum == 0:
					language = "de"
				elif inputNum == 1:
					language = "en"
				elif inputNum == 2:
					language = "nl"
			else:
				slide = inputNum - numLanguages
				print("Changing slide to " + str(slide))
			writeFile()
	except Exception:
		print(str(sys.exc_info()))
	pass
