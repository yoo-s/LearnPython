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
	
	action = ['n', 's', 'e', 'w', 'help']

	do="puppies" # assing a value to the variable to make testing it possible
 
	while do not in action:
		do = raw_input("> ")
 
	if do == "n":
		farmhouse()
	elif do == "w":
		cornfield()
	elif do == "e":
		barnhouse()
	elif do == "s":
		cross_stream()
	elif do == "help":
		help()
	else:
		print "Unfortunately, you don't know how to do said action."

def help():
	print "'n' = go north \n's' = go south \n'e' = go east \n'w' = go west"
	start()

def farmhouse():
	print "You open the door and step inside the house. It's quiet here except \
for the soft ticking of the grandfather clock positioned at a corner."

def cornfield():
	print "You're at the edge of a large cornfield. A lonely \
scarecrow stands in the middle, crows pecking at its ragged clothes. \
You feel scared you might find zombies lurking around inside."

def barnhouse():
	print "The moment you enter the barnhouse, something whooshes past your \
face by inches. You jump back startled, and look up to see a beautiful barn \
owl perch itself on a wooden beam near the ceiling."

def cross_stream():
	print "You cross the little wooden bridge curving over the gently trickling \
stream. You're now looking at a vast grassy plain, and far in the middle of \
the plain stands a white windmill slowly turning in the breeze."

	do = raw_input("> ")


intro()