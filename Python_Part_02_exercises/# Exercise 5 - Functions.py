# Exercise 5 - Functions

''''
Import random function
Create a function random_list_summer creates n elemented list 
with min value = -100 max value = 100 it has to print the list first and 
sum all the elements of it default element number is 15
Don't forget to call the function
'''

import random 

def random_list_summer(n):
    random_list = []
    ListSum = 0 
    for i in range(0,n):
        random_list.append(random.randint(-100,100));
        ListSum = ListSum + random_list[i]
    print('The random list is:' , random_list[:])
    return ListSum

n = 15
print('Give me the size of the list in numbers:')
print('The sum of the list is',random_list_summer(n));