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

1) cast num1 to string and assign to num1_str
num1_str = str(num1)

2) check the length of the string
print(len(num1_str))

3) get the third element of string (the one in the 3rd order)
print(num1_str[2])

4) get the 3-5 elements of string (both inclusive) by string slicing
print(num1_str[2:5])

5) check if num2 in string (cast if necessary)
num2 = "223"
if num2 in num1_str:
    print("num2 found in num1_str")
else:
    print("num2 not found in num1_str")

6) check if num3 in string (cast if necessary)
num3 = "999"
if num3 in num1_str:
    print("num3 found in num1_str")
else:
    print("num3 not found in num1_str")

7) concatenate 0 to the string from left and assign to string_with_0
string_with_0 = "0" + num1_str
print(string_with_0)

8) get the characters of string_with_0 from start to position 4 (end point exclusive)
print(string_with_0[:4])

9) get the characters of string_with_0 from position 5 until the end
print(string_with_0[4:])

10) use negative indexing to reach the "567" string_with_0
print(string_with_0[-3:])