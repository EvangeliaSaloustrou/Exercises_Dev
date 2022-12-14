# Data Structures 🐍

'''
Remember `list`,`set`,`dictionary` are mutable and `tuple` is immutable
`list`,`tuple` elements can be reached by index  
for `dictionary` it is not an option to reach by index the element key has to be known to reach  
and for `set` the items cannot be reached directly but it is possible to iterate.
'''
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}


'''
1. print the lengths of `list1`,`tuple1`,`set1`,`dict1`
2. print the first element of `list1` and `tuple1`
3. print the value of `lion` key of `dict1`
4. change the 2nd position element of `list1` to "rabbit"
5. try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
6. add "monkey" to `list1`
7. remove "rabbit" from `list1`
8. in `dict1` the number of feet is written as value to each animal the fixh has wrong value just fix it.
'''
#1
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))

#2
print(list1[0])
print(tuple1[0])

#3
dict1["lion"]

#4
list1[1] = "rabbit"

#5
'''
'tuple' object does not support item assignment.
Tuples are immutable.
If we want to change a value in a tuple,
we can convert it into a list, change it, and convert it back into tuple.
'''
y = list(tuple1)
y[1] = "rabbit"
tuple1 = tuple(y)

print(tuple1)

#6
list1.append("monkey")

#7
list1.remove("rabbit")

#8
dict1["fish"] = 0
print(dict1)