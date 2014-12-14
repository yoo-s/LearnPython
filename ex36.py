# Where's My Kitten?
# A text adventure game

def start():
	print "There are some things you need to know."
	print "You lost your kitten."
	print "You need to find your kitten."
	print "Go~~~!"
	print " "
	print '''You stand facing the farmhouse. There's grassy fields to your left and a barnhouse to your right. Behind you is a stream with a
	small wooden bridge across it, and across the stream in the distance is a white windmill.'''
	print "Type 'help' for list of possible actions."
	print " "
	
	action = raw_input("> ")

	if "farmhouse" in action:
		farmhouse()
	elif "fields" or "left" in action:
		grassy_fields()
	elif "barnhouse" or "right" in action:
		barnhouse()
	elif "cross" or "stream" in action:
		cross_stream()
	elif action == "help":
		help()
	else:
		print "Unfortunately, you don't know how to do said action."

def help():
	print "You can go in directions north, south, east, and west. You can look at your surroundings, "