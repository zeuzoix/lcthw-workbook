import sys

def print_info(keyword):
        print "Example of %s\n" % keyword

def example_and():
        print "True and False is %r" % (True and False)
        print "True and True is %r" % (True and True)
        print "False and True is %r" % (False and True)
        print "False and False is %r" % (False and True)

def example_as():
        with open("ex15_sample.txt") as f:
                data = f.read()
                print data

def example_assert():
        #assert (False), "Error!"
        assert (True), "Error!"
        print "No Assert"

def example_break():
        while True:
                break
        print "break exited infinite loop"

def example_class():
        class person(object):
                def __init__(self, name):
                        self.name = name;

        p1 = person('Jonah')
        p2 = person('Rachel')

        print p1.name
        print p2.name

def example_continue():
        i = 1
        while True:
                if (i > 10):
                        break;
                else:
                        if (i % 2 == 0):
                                i+=1
                                continue
                        print "%d" % i
                        i+=1
def example_del():
        a = [0, 1, 2, 3, 4, 5]
        print a
        del a[2]
        print a

def example_elif():
        x = 2
        if x == 1:
                print "1"
        elif x == 2:
                print "2"
        else:
                print "Everything else"

def example_else():
        x = 2
        if x == 1:
                print "1"
        else:
                print "Everything else"

def example_except():
        random_list = [ 's', 0, 2 ]
        for entry in random_list:
                try:
                        print "The entry is", entry
                        r = 1/int(entry)
                except:
                        print "Oops!", sys.exc_info()[0], sys.exc_info()[1], "occured."
                        print "Next entry"
                        print
        print "The reciprocal of ", entry, "is", r

#example_and()
#example_as()
#example_assert()
#example_break()
#example_class()
#example_continue()
#example_del()
#example_elif()
#example_else()
example_except()
