# More Variables and Printing

my_name = 'William Y.'
my_age = 22
my_height = 173
my_weight = 75
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." %my_name
print "He's %d cm tall." %my_height
print "He's %d kg heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#This line is tricky, try to get it exactly right.
print "If I add %d, %d and %d I get %d." %(my_age, my_height, my_weight,
                                            my_age + my_height + my_weight)
