# #immutable (not-changeble):

# tup = ()
# tup = (1,)
# print(type(tup))

# #to change the items in the tuple, change the datatype in list and then again change it to tuple after changing the requirement.
# a = (1)
# print(type(a)) #type = int and not tuple
# x = (1,) #1, rakhnu pracha if you want only 1 in tuple. 
# print(type(x))

# #to change the items in the tuple:
# tup = ("sushma", "thapa", "sush")
# lst = list(tup)
# lst[2] = "girl"
# tup = tuple(lst)
# print(tup)

# # #to change the variable of the tuple: unpacking.
# fruits = ("apple", "banana", "Cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# #use "*" to assign the same color to every other variable.
# fruits = ("apple", "banana", "Cherry", "strawberry")
# (green, yellow, *red) = fruits 
# print(green)
# print(yellow)
# print(red)

# #multiply tuple: multiplies the number of occurence in the tuple.;
# fruits = ("apple", "cherry")
# mult = fruits*2
# print(mult)
    
# #to add tuples: concatenate(+)
# tup1 = ("sush", "thapa")
# tup2 = ("hi", "bye")
# tup3 = tup1+tup2
# print(tup3)

# #.count(): counts the number of occurence of that particular item.
# fruits = ("apple", "cherry", "apple")
# a = fruits.count("apple")
# print(a)

#index: returns the index of the first specified item from the tuple.
fruits = ("apple", "cherry", "apple")
x = fruits.index("apple") #returns 0 as the first value of apple lies in index 0
print(x)
 

