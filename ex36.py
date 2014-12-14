# Where's My Kitten?
# A text adventure game

def start():
	print "There are some things you need to know."
	print "You lost your kitten."
	print "You need to find your kitten."
	print "Go~~~!"
	print " "
	print "You stand facing north towards the farmhouse. There's grassy fields to your left \
and a barnhouse to your right. Behind you is a stream with a small wooden \
bridge across it, and across the stream in the distance is a white windmill."
	print "Type 'help' for list of possible actions."
	print " "
	
	action = raw_input("> ")

	if "farmhouse" in action or "north" in action:
		farmhouse()
	elif "fields" in action or "left" in action or "west" in action:
		cornfield()
	elif "barnhouse" in action or "right" in action or "east" in action:
		barnhouse()
	elif "cross" in action or "stream" in action or "south" in action:
		cross_stream()
	elif action == "help":
		help()
	else:
		print "Unfortunately, you don't know how to do said action."

def help():
	print "You can go in directions north, south, east, and west. You can look \
at your surroundings, read anything readable, open things, etc. for starters."

def farmhouse():
	print "You open the door and step inside the house."

def cornfield():
	print "You're standing at the edge of a large cornfield."

def barnhouse():
	print "You enter the barnhouse."

def cross_stream():
	print "You cross the little wooden bridge curving over the gently trickling \
stream. You're now standing in a vast grassy plain, and far in the middle of \
the plain stands a white windmill slowly turning in the breeze."

	action = raw_input("> ")


start()