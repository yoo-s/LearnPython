print "What\'s your favorite fruit?",
fruit = raw_input()
print "What\'s your favorite ice cream flavor?",
flavor = raw_input()
print "What sport do you like?",
sport = raw_input()

print "So, you love %ss, %s ice cream and do %s." % (fruit, flavor, sport)

if flavor == "strawberry":
	print "Really?? So do I!"