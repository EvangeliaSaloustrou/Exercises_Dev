# Methods - Exercise 3 🐍

# to convert a number to string we can use `str()` function this is called `casting`

# 1. cast num1 to string and assign to num1_str
# 2. check the length of the string
# 3. get the third element of string (the one in the 3rd order)
# 4. get the 3-5 elements of string (both inclusive) by string slicing
# 5. check if num2 in string (cast if necessary)
# 6. check if num3 in string (cast if necessary)
# 7. concatenate 0 to the string from left and assign to string_with_0
# 8. get the characters of string_with_0 from start to position 4 (end point exclusive)
# 9. get the characters of string_with_0 from position 5 until the end
# 10. use negative indexing to reach the "567" string_with_0


num1 = 1122334455666

# 1. cast num1 to string and assign to num1_str

num1_str = str(num1)

# 2. check the length of the string

len(num1_str)

# 3. get the third element of string (the one in the 3rd order)

num1_str[3]

# 4. get the 3-5 elements of string (both inclusive) by string slicing

num1_str[3:5]

# 5. check if num2 in string (cast if necessary)
# num2 has not been given
# let's assume that num2 = True

num2 = True
print(type(num2))
num2_str = str(num2)
print(type(num2_str))

# 6. check if num3 in string (cast if necessary)
# num3 has not been given
# let's assume that num3 = 33.2

num3 = 33.2
print(type(num3))
num3_str = str(num3)
print(type(num3_str))

# 7. concatenate 0 to the string from left and assign to string_with_0

string_with_0 = "0" + num1_str 

# 8. get the characters of string_with_0 from start to position 4 (end point exclusive)

string_with_0[:5]

# 9. get the characters of string_with_0 from position 5 until the end

string_with_0[5:]

# 10. use negative indexing to reach the "567" string_with_0

string_with_0[-9:-6]
