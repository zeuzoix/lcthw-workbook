# Import the argv module
from sys import argv

# Unwrap argv into script, filename
script, filename = argv

# Open a file object called txt
txt = open(filename)

# Print statement with the filename
print "Here's you file %r:" % filename
# Read the file object and print it
print txt.read()

# Get another file from the user using _raw_input_
print "Type the filename again:"
# Save the filename in file_again
file_again = raw_input("> ")

# Open a file object called txt_again
txt_again = open(file_again)

# Read the file object and print it
print txt_again.read()
