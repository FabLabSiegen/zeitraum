import uno
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
doc = desktop.getCurrentComponent()

presentation = doc.getPresentation()
presentation.start()
while not presentation.isRunning():
	pass
presentation_controller = presentation.getController()
presentation_controller.gotoSlideIndex(6)
print("isRunning() == %s" % presentation_controller.isRunning())
