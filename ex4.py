# Variable to hold how many cars are available
cars = 100
# Variable to hold the space in a car
space_in_a_car = 4.0
# Variable to hold the number of drivers
drivers = 30
# Variable to hold the number of passengers
passengers = 90
# Variable to hold cars not driven
cars_not_driven = cars - drivers
# Variable to hold cars driven
cars_driven = drivers
# Variable to carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Variable to hold average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
