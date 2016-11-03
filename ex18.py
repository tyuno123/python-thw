# Names, Variables, Code, Functions

# this one is like your scrupts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# ok that *arg is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" %arg1

#this one takes no arguments
def print_none():
    print "I got nothing"

print_two("Homo", "Sapien")
print_two_again("Kappa", "Donger")
print_one("LeL")
print_none()
