# Exercise 2 - Classes and Object

'''
Now continue with the Animal class we had used before

Add a method to count the legs count_legs which prints the number of legs

Add a method to count the legs return_legs which returns the number of legs

Print number of legs directly from number_of_legs variable of the object
'''

class Animal:

    def __init__(self, number_of_legs, runs):   
        self.number_of_legs = number_of_legs
        self.runs   =   runs
    
    def count_legs(self):       
        print('The number of legs is: ', self.number_of_legs);
    
    def return_legs(self):
        return self.number_of_legs;
        
animal = Animal(4, "runs"); 


animal.count_legs();
print(animal.return_legs())
