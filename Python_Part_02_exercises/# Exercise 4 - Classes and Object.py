"""
# Classes and Objects - Exercise 4 🐍

Let's inherit Dog class from Animal 
add name(private) attribute to Dog class 
and then bark method to print `woof woof`

print name_of_dog 
make it bark
count the legs 

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

class Dog(Animal):
    def __init__(self, name, leg_count):
        self._name = name
        super().__init__(leg_count)
    
    def bark(self):
        print("woof woof")

# create dog object with name and leg count
dog = Dog("Bruno", 4)

# print name of dog
print(dog._name)

# make dog bark
dog.bark()

# count legs of dog
dog.count_legs()

#OUTPUT

"""
Animal object was created
Bruno
woof woof
Number of legs: 4
"""