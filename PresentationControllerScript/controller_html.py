#!/bin/python3
import subprocess

numLanguages = 3
languagePins = [0, 1, 2] # de, en, nl
language = "de"
slide = 0

def writeFile():
	try:
		file = open("/home/pi/Desktop/share/zeitraum/Presentation_HTML/currentSlide.js", "w")
		file.write("var index = '" + str(slide) + "';\n")
		file.write("var lang = '" + str(language) + "';")
		file.close()
	except Exception:
		print("Unable to write file.")
		print(str(Exception))

while(True):
	try:		
		inputNum=subprocess.check_output(["read " "-s " "-n " "1 " "-r " "rep " "&& " "echo " "\"$rep\" "], shell=True)[0]
		if(inputNum>57):
			inputNum -=87#a-z to start from 10, a is 97 in ascii
		else:
			inputNum -=48#0-10 to start from 0, 0 is 48 in ascii
		#reads one buttonpress and only one button, changed the arduinos to buttonpresses to enable gradual changes for direct perception of reaction during software changes down the line
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
