#list can have int, str or both in it. it is also mutable hence, we can always change the value of the items in the list.
#creating a list of integers:
x = [1, 2, 3, 4, 5]
print(x[1])

#creating a list of strings:
y = ["apple", "banana", "cherry"]
print(y[1])

#Creating a list of int, str, boolean and float:
z = [21, "Sushma", True, 3.147]
print(z[2])

# print(x,y,z)


#replacing the value:
fruits = ["apple", "banana", "cherry"]
fruits[1] = "Orange"
print(fruits)

#append() #adds the item at the last.
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)

#.count(): counts the number of occurence of that particular item.
fruits = ("apple", "cherry", "apple")
a = fruits.count("apple")
print(a)

#index: returns the index of the first specified item from the list.
fruits = ("apple", "cherry", "apple")
x = fruits.index("apple") #returns 0 as the first value of apple lies in index 0
print(x)

#assignment1: to ask the name of the fruits with the user and exit the program when the user presses 0
fruit_list = []
while True:
        x = input("Enter fruits name or press 0 to exit: ")
        if x != "0":
                fruit_list.append(x)
        else:
                print(fruit_list)
                break #to break the loop as it goes infinite times.


#assignment2:
num = [1,2,3,4,5,6,7,8,9,10]
while True:
        choice = input("Enter y to replace the numbers and press any other keys to exit it.")
        if choice.lower() == "y":
                old_value = int(input("Enter the value to be replaced: "))
                new_value = int(input("Enter the new value: "))
        for index in range(len(num)):
                if num[index] == old_value:
                        num[index] = new_value
        else:
                break
print(num)

#list comprehension:
#syntax:
#newlist = [expression for item in iterable if condition == True]

#que1:
num = [1,2,3,4,5,6]
newlist = [x for x in num if x%2 != 0 ]
print(newlist)

# que2: power
output = [1,4,9,16,25,36]
num = [1,2,3,4,5,6]
newlist = [x**2 for x in num if True ]
print(newlist)

#que3:
num = [1,1,1,2,2,2,2,3,4,5,6]
x = int(input("Enter the number you want to remove from the list: "))
newlist = [i for i in num if i != x]
print(newlist)

#to return the items in the list which has more than equal to 4 letters.
list = ["apple", "dog", "monkey", "nose", "rudolph" ]
newlist = [x for x in list if (len(x)) >= 4]
print(newlist)

# to return "even" in place of even numbers in the list.
num = [1,2,3,4,5,6]
newlist = [x if x%2 != 0 else "even" for x in num]
print(newlist)

# .sort() : ascending order ma janchha (1-10) (A-Z then a-z)
# .sort(reverse = True) : for descending order (10-1) (z-a) (Z-A)
# x = sorted(variable, reverse = True) : returns a new sorted list.

#to return the indexed value of the index.
x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(x[0][0])                
print(x[1][1])                
print(x[2][2])                

#to print sum of the variable:
num = [1,2,3]
print(sum(num))     

#sum             
num = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
total = 0
for i in num:
    total += sum(i)
print(total)

#multi:
num = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
total = 1
for i in num:
    for x in i:
        total = total * x
print(total)

#sum of (3,5,9):
num = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
sum = 0
for i in num:
    for x in i:
        if x == 3 or x == 5 or x == 9:
            sum += x
print(sum)

#sum of any numbers entered by the user from the list:
num = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
sum = 0
user_input = int(input("Enter the number you want the sum of: "))
while user_input != 0:
    for i in num:
        for x in i:
            if x == user_input:
                sum += x
    user_input = int(input("Enter the number you want the sum of: "))    
print(sum)

   




