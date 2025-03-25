# #immutable i,.e, changable
# str = "" #empty str
# #indexing 
# x = "HELLO, WORLD"
# print(x[2]) #to print in separate lines.
# print(x[11])
# #or
# print((x[2]),x[11]) #to print in the same line.

# #slicing:
# a = "Hello World!"
# print(a[1:5]) #prints from 1 to 4 which is ello but 5th index is not included.
# print(a[:5]) # prints hello as nothing in the starting index prints eveything ahead of the index 5.
# print(a[7:]) # prints orld! as nothimng in the ending index prints everything after the index 7.

# # to make the string increase by the step size:
# s = "Hello World"
# print(s[::2]) #prints HloWrd as it skips 1 step because the step size is increased by 2.

# print(s[6::2]) #prints Wrd as it starts with 6 as we are only taking the word World and nothing after the colon in the end as we are taking everything after the index 6 and is increased by the step size of 2.

#len() #counts from the index 1. counts exactly the number of charcaters the string has.
# w = "Hello, World!"
# # print(len(w))
# for i in range(len(w)):
#     # print(i) #print i garyo bhaney chei numbers. #print w garyo bhaney chei tyo string teti choti chalchha.
#     print(w[i])

# #using while loop:
# y = "Hello World"
# i = 0
# while i < (len(y)):
#     print(y[i])
#     i += 1

# #to print the index of the given string. #prints from the starting to the ending position of the index.
# x = "Hello World"
# new = x[6:]
# print(new)
# for i in range(len(x)):
#     if x[i] == "W":
#         print("The position of W is: ",i)
#     elif x[i] == "d":
#         print("The position of d is: ",i)
#     elif x[i] == " ":
#         print("The position of ' ' is: ",i)
#     elif new[i] == "o":
#         print("The position of ' ' is: ",i+new)

# #using while loop:
# s = "Hello Worldoo"
# i = 0
# count = 0
# while i<(len(s)):
#     if s[i] == "o":
#         if count > 2:
#             print("index of o is: ", i)
#         count += 1    
#     i += 1

# counting the number of 'o' using while loop:
# s = "Hello Worldoo"
# i = 0
# count = 0
# while i < (len(s)):
#     if s[i] =="o":
#         count += 1
#         print("The count of 'o' is",count)
     
#     i += 1

# #without using indexing to find out the index;
# g = "Hello World"
# count = 0
# for i in g:
#     print(i,count)
#     count += 1

##using while loop:
# j = "Hello World"
# i = 0
# while i <(len(j)):
#     print(j[i])
#     i += 1

## n = "Hhello World"
# for i in n:
#     if i == "h" or i == "H":
#         print("The character is h or H")
#     else:
#         print("The character is not h or H", i)

## using while to check if the character is h/H or not:
# n = "Hello World"
# i = 0
# while i < (len(n)):
#     print(n[i])
#     if n[i] == "h" or n[i] == "H":
#         print("The character is h or H")
#     else:
#     i += 1
# print("The character is not h or H: ",n[i])

##using for loop to count the number of character in the string.
# s = "Hhhello World"
# count = 0
# for i in s:
#     if i == "h" or i == "H":
#         count += 1
# print("The count of h or H is: ", count)

##using while loop to count the number of character in the string.
# s = "Hhhello Worldh"
# i = 0
# count = 0
# while i< (len(s)):
#     if s[i] == "h" or s[i] == "H":
#         count += 1
#     i += 1 
# print("The count of h or H is",count) 

# #immutable datatype:
# s = "Hello"
# s= "h" + s[1:] #this is how we should change the character of the string as it is immutable.
# print(s)

# s = "Hello"
# s = s[0:]+ " " +"World" #will print in the order you add them.
# print(s)

# #replace()
# s = "Hello World"
# print(s.replace("World","Python")) #("old value", "new value")

# #lower()
# s = "Hello World"
# print(s.lower())

# #upper()
# s = "Hello World"
# print(s.upper())

# #title()
# s = "hello world"
# print(s.title())

# #.count(): counts the number of occurence of that particular item.
# fruits = ("apple", "cherry", "apple")
# a = fruits.count("apple")
# print(a)

# #index: returns the index of the first specified item from the tuple.
# fruits = ("apple", "cherry", "apple")
# x = fruits.index("apple") #returns 0 as the first value of apple lies in index 0
# print(x)

# #lstrip() removes the extra spaces from the left side.
# #rstrip() removes the extra spaces from the right side.
# #strip()  removes all the extra spaces from the left and the right side of the string but not from the middle.

# #to remove the "#" and return the output as "Hello World".
# x = "#################helloworld##############"
# a = (x.strip("#"))
# b = a[0:5] + " " + a[5:10]
# c = (b.title())
# print(c)

# x = "Hello World"
# a = x.lower()
# b = "#############"+ a[:5] + a[6:] + "#############"
# print(b)

x = "Hello World"
length = len(x)
pass

# #split()
# x = "Hello World" #space aghi ra pachi lai chhutta chhuttai words linchha.
# print(x.split())
# y = "Hello#World#python" #space nabhayera kunai special character bhako case ma
# print(y.split("#"))


# #join() #only same datatypes can be joined. i.e, strings and strings.
# x = ["Hello", "World", "Python"]
# a = "".join(x)
# print(a)
# b = ",".join(x)
# print(b)
# c = "#".join(x)
# print(c)
# d = " ".join(x)
# print(d)

#string methods
#.isdigit() #returns in the boolean value if it has all digits. #number nei huna paryo, ".,-" bhayo bhaney false return garchha.

#.islower()

#

# #f-string:
# a = int(input("Enter a num1:"))
# b = int(input("Enter a num2:"))
# print(f"The sum of {a} and {b} is: {a*b}")
































        



        