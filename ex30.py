people = 30
cars = 40
trucks = 15

if cars > people:
        print "We should take cars."
elif cars < people:
        print "We should not take cars."
else:
        print "We can't decide."

if trucks > cars:
        print "That's too many trucks."
elif trucks < cars:
        print "Maybe we could take trucks."
else:
        print "We still can't decide."

if people > trucks:
        print "Alright lets just take trucks."
else:
        print "Fine, let's stay at home instead."
