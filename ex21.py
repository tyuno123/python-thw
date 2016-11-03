# Functions can return something

def add(a,b):
    print "Adding %d + %d" %(a,b)
    return a+b
def subtract(a,b):
    print "Subtracting %d - %d" %(a,b)
    return a-b
def multiply(a,b):
    print "Multiplying %d * %d" %(a,b)
    return a*b
def divide(a,b):
    print "Dividing %d / %d" %(a,b)
    return a/b

print "Lets do some math with functions!"

age = add(10,6)
height = subtract(4, 19)
weight = multiply(65, 5)
iq = divide(400,4)

print "Age %d, Height %d, Weight %d, IQ %d" %(age, height, weight, iq)

# A puzzle for the extra credit
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "This becomes: ", what, "Can you do it by hand?"
