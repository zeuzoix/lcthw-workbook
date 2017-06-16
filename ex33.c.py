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

create_list(8, 1)
create_list(10, 2)
create_list(6, 3)
