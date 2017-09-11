#!/bin/python3

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
		inputNum = int(input("Slide: "))
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
