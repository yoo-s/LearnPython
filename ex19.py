def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You hve %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def strawberrycake(cream, strawberries):
	print "You're making a strawberry cake. Yum!"
	print "You need %s tbsp of cream," % cream
	print "As well as %s strawberries." % strawberries
	print "Now you're ready to make the batter!\n"

strawberrycake(10, 30)
strawberrycake("nine", "fifteen")
strawberrycake(6 + 3, 2 * 4)
strawberrycake(int(raw_input("How much cream? ")), int(raw_input("How many strawberries? ")))
creamy = int(raw_input("Cream? ")) + 5
berries = int(raw_input("Berries? ")) * 3
strawberrycake(creamy, berries)