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
    def __init__(self, runs, legs = 4):
        self.runs = runs
        self.legs = legs

animal = Animal(runs, 4)
animal.runs(runs)
print("Animal object was created")

def runs(self):    
    print("Running started")