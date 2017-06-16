def create_list(n, step):
        i = 0
        numbers = []

        while i < n:
                print "At the top i is %d" % i
                numbers.append(i)
                
                i = i + step
                print "Numbers now: ", numbers
                print "At the bottom i is %d" % i

        print "The numbers: "

        for num in numbers:
                print num

def create_list_1(n, step):
        i = 0
        numbers = []

        for i in range(0, n, step):
                if i != 0:
                        print "At the bottom i is %d" % i

                print "At the top i is %d" % i
                numbers.append(i)
                print "Numbers now: ", numbers
                
        print "At the bottom i is %d" % i
        print "The numbers: "

        for num in numbers:
                print num

create_list_1(8, 1)
create_list_1(10, 2)
create_list_1(6, 3)
