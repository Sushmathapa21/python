# #while : condition based. true nabhaye samma. while ma last ma +=1 dherai jaso chhaincha.
# count = 0
# while count < 5:
#     print(count)
#     count += 1 # count = count + 1

# # from (1-5)
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# # print("loop ended.")

# # from (1 -100)
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# #from (100-1)
# i = 100
# while i >= 1: #stopping condition
#     print(i)
#     i -= 1

# #multiplication table:
# i = 0
# multi = 0
# num = int(input("Enter a Number you want the multiplication of: "))
# while i <= 9:
#     # print(i)
#     multi = num * i
#     i += 1
#     print(f"{num} * {i} = {multi}")

# #printing the length of the list.
# list = [1,4,9,16,25,36,49,64,81,100]
# x = 0
# while x < len(list):
#     print(list[x])
#     x +=1

# #printing the length of the list.
# list = ["superman", "batman","spiderman"]
# i = 0 #initialization
# while i < len(list):
#     print(list[i])
#     i += 1

# #printing the length of the tuple and printing a particulaar number with it's index.
# tuple = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i < len(tuple):
#     # print(tuple[i])
#     if (tuple[i]== x):
#         print("36 Found at index",i)
#         break
#     i += 1

# #to print even or odd numbers:
# i = 0
# while i <= 10:
#     if i%2 == 0:
#         print("Even numbers",i)
#         i +=1

# #printing sum until pressed 0.
# sum = 0    
# num = 1
# while num != 0:
#     num = int(input("Enter Number: "))
#     sum = sum+num
# print("sum",sum)

# #printing substraction until pressed 0.
# sub = 10
# num = 1
# while num != 0:
#     num = int(input("Enter Number: "))
#     sub = sub - num
#     print("sub", sub)

# #skiping 5 from the range of 1 numbers using continue.
# i = 1
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)   

# #question 1:
# num = int(input("Enter any numbers and press 0 to exit."))
# while num != 0:
#     num = int(input("Enter the Number: "))
#     if num == 0:
#         break
# print("exited from the loop.") 

# #question 2:
# sum = 0
# while True:
#     num = int(input("Enter the Number: "))
#     sum = sum + num
   
#     if num == 0:
#         print("sum",sum)
#         break
# print("Exited from the loop.")

# #sum of numbers:
# num = 0
# sum = 0
# while True:
#     num = int(input("Enter the Number: "))
#     # print(num)
#     # num += 1
#     sum = sum + num
#     num += 1
#     print("sum", sum)

# #sum of n natural numbers:
# sum = 0
# n = 5
# for i in range(n+1):
#     if i == 0:
#         continue
#     print(i)
#     sum = sum + i
# print("The sum of natural numbers are: ",sum)

# #multiplication table using while loop:
# i = 1
# num = int(input("Enter a number you want the multiplication of: "))
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i += 1

#sum of first n natural numbers:
num = 1
while num >= 1:
    sum = num + sum
    print(num)
    num += 1  















