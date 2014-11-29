from sys import argv

script, user_name, age = argv
prompt = 'Your answer? '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print "Are you really %s years old?" % (age)
reply = raw_input(prompt)

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You said %r regarding your age. Interesting.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, reply, lives, computer)