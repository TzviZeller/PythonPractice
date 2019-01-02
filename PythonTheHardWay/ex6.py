x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"
y = "Those who knoe %s and those who %s" % (binary,do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." %y)

hilarious = False
joke_evolution = "Isnt %r"

print(joke_evolution % hilarious)

w = "This is the left side of .."
e = "a string with a right side."

print(w + e)
