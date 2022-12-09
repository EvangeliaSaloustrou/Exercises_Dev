# Exercise 7 - Functions

'''
Create a lambda function that returns 2nd power of given number if its even
and run it on the given list
then print the result to the screen
'''

my_list= [*range(5)] 
SecondPower = lambda x : (x * x) 
for i in range(5):
    if my_list[i] % 2 == 0: 
        print(SecondPower(my_list[i]));
