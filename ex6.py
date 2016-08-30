# Variable to hold a string with a format specifier
x = "There are %d types of people." % 10
# Variable to hold a string "binary"
binary = "binary"
# Variable to hold a string "don't"
do_not = "don't"
# We use the string variables binary and do_not in a statement
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the variable x
print x
# Print the variable y
print y

# Print x in another statement
print "I said: %r." % x
# Print y in another statement
print "I also said: '%s'." %y

# Assign a boolean variable hilarious
hilarious = False
# Assign a string variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the variable joke_evaluation passing hilarious
# as the variable for the format specifier
print joke_evaluation % hilarious

# Another string variable
w = "This is the left side of..."
# Yet another string variable
e = "a string with a right side."

# Combining the two string variables to print a bigger string
print w + e
