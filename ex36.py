# Where are you, my ______?
# A text adventure game

import time

def intro():
	print "There are some things you need to know."
	print "You lost your kitten."
	print "You need to find your kitten."
	print "Go~~~!"
	print " "
	time.sleep(3)
	start()

def start():
	print "You stand facing north towards the farmhouse. There's a cornfield \
to your left and a barnhouse to your right. Behind you is a stream with a small \
wooden bridge across it, and across the stream in the distance is a white windmill."
	print "Type 'help' for list of possible actions."
	print " "
	
	action = ['N', 'S', 'E', 'W', 'help']

	do="something stupid" # assing a value to the variable to make testing it possible
 
	while do not in action:
		do = raw_input("> ")
 
	if do == "N":
		farmhouse()
	elif do == "W":
		cornfield()
	elif do == "E":
		barnhouse()
	elif do == "S":
		cross_stream()
	elif do == "help":
		help()
	else:
		print "Unfortunately, you don't know how to do said action."

def help():
	print "'N' = go north \n'S' = go south \n'E' = go east \n'W' = go west"
	start()

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

	do = raw_input("> ")


intro()