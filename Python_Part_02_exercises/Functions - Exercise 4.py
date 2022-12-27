# Functions - Exercise 4 🐍

'''
Now create a fuction for John Doe and his family that greets every one in the family.   
Since it will  usually John Doe the name and surname parameter must be defaulted   
and when someone else comes it has to greet the new comer with name surname parameters which were overwritten. 
Make it possible.  
The function have to print `"Hello John Doe"` where John and Doe is parametric   
Greet each our John first then the people in the list with for loop and the function   
What you have to use
- for loop 
- function 
- string operation 
- list index

Output format 
```
Hello John Doe!
Hello Tristram Mcbride!
Hello Baldwin Preston!
Hello Wally Collins!
```
'''
def greet(name="John", surname="Doe"):
    print("Hello {} {}!".format(name, surname))

greet()

family = [("Tristram", "Mcbride"), ("Baldwin", "Preston"), ("Wally", "Collins")]
for member in family:
    greet(member[0], member[1])