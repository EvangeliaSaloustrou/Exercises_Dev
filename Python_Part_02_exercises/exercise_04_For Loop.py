# Iterators - Exercise 4 🐍


# iterate each elements of `list1`,`tuple1`,`set1` and print them out 

# for the `dict1` iterate all elements but only print the ones who are living on land
# in the form of `x lives in y`



list1 = ["lion", "monkey", "dog","fish"]

for x in list1:
  print(x)


tuple1 = ("lion", "monkey", "dog","fish")

for a in tuple1:
  print(a)


set1 = {"lion", "monkey", "dog","fish"}

for b in set1:
  print(b)


dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for key, value in dict1.items():
    if str(value).startswith("la"):
        print(key, value)
