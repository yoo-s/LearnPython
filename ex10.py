tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
apple = "apple\'s"
pear = "pear\'s"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fruit = "%s and %s cores - They\'re the best kind!" % (apple, pear)

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fruit

'''while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,'''