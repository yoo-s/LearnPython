i = 0
numbers = []
maxnum = 5
add = 2

def numlist(letter, num, incr, listing):
    for letter in range(0, 5):
    # while letter < num:
        print "At the top i is %d" % letter
        listing.append(letter)

        # letter = letter + incr
        print "Numbers now: ", listing
        print "At the bottom i is %d" % letter

numlist(i, maxnum, add, numbers)

print "The numbers: "

for num in numbers:
    print num