# Classes and Objects - Exercise 1 🐍

'''
Let's create Animal class and then create the 
animal object that runs and having 4 legs

create animal object with leg count 
when created print 
`"Animal object was created"`
and then call `runs` method of it and it prints 
`"Running started"`

'''
class Animal:
    def __init__(self, leg_count):
        self.leg_count = leg_count
        print("Animal object was created")
    
    def runs(self):
        print("Running started")

# create animal object with leg count
animal = Animal(4)

# call runs method of animal object
animal.runs()