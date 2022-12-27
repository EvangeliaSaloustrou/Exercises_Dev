"""
# Classes and Objects - Exercise 3 🐍

Again let's keep talking on Animal class we have.  
with 3 methods we just reached the number of legs   
to prevent direct interactin with the class variables   
most of the other programming languages have encapsulation.  
But in python we don't have it 
instead we use `_` prefix for it as convention   
it is also same for the methods   
  
`_legs` this shows us not to touch this variable its up to you 
if you want to change it you can but `_`asks you politely not to do it. 

Change the `number_of_legs` to conventional private variable 
and call from another method
"""
class Animal:
    def __init__(self, leg_count):
        self._leg_count = leg_count
        print("Animal object was created")
    
    def runs(self):
        print("Running started")
    
    def count_legs(self):
        print("Number of legs: {}".format(self._leg_count))
    
    def return_legs(self):
        return self._leg_count
    
    def change_legs(self, new_leg_count):
        self._leg_count = new_leg_count

# create animal object with leg count
animal = Animal(4)

# call count_legs method of animal object
animal.count_legs()

# call return_legs method of animal object and print the result
print(animal.return_legs())

# change the number of legs using change_legs method
animal.change_legs(6)

# call count_legs method again to see the updated number of legs
animal.count_legs()



# OUTPUT

"""
Animal object was created
Number of legs: 4
4
Number of legs: 6
"""
