i = 0
numbers = []
maxnum = 5

def numlist(letter, num, listing):
    while letter < num:
        print "At the top i is %d" % letter
        listing.append(letter)

        letter = letter + 1
        print "Numbers now: ", listing
        print "At the bottom i is %d" % letter

numlist(i, maxnum, numbers)

print "The numbers: "

for num in numbers:
    print num