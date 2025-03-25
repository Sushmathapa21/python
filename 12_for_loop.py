# #used when you want to use something repeatedly, #iteration
# #range(start,end,step)
# #for loop : over a sequence. 
# result = 0
# for i in range (5):
#     result = result + i
#     # print(i)
# print("result", result)
 
# #result - 1*2*3*4*5
# num = int(input("Enter a Number: "))
# result = 1
# for i in range(num): #we can put range here. (20, 80) will print from 20 to 79. strating should always be less than the end.
#     if i != 0:
#         result = result * i
# print(result)

# #odd and even count in between the range of numbers.
# start = int(input("Enter the start Number: "))
# end = int(input("Enter the end Number: "))
# odd = 0
# even = 0
# for x in range (10,20):
#     if x%2 == 0:
#         even = even + 1
#         print("Even")
#     else:
#         odd = odd + 1
#         print("odd")
# print("even count",even)
# print("odd count", odd)

# #counting a or A.
# name = "abc and aaa aaa"
# a_count = 0
# for x in name:
#     if x == "a" or x == "A":
#         print(x)
#         a_count = a_count + 1
# print("a_count",a_count)

# #Print all numbers from 1 to 20 using a for loop.
# i = 0
# for i in range(1,21):
#     print(i)

# #Calculate the sum of all even numbers between 1 and 100.
# i = 0
# even = 0
# for i in range (1,101):
#     if i%2 == 0:
#         even = even + i
# print("even_count", even)
# #or
# even = 0
# for i in range(2, 101, 2):  # Starts from 2, goes up to 100, increments by 2
#     even += i
# print("even_count", even)

# # x = "Programming is fun!"
# # vowel_count = 0
# # for i in x:
# #     if x == "a" or "e" or "i" or "o" or "u":
# #     i = vowel_count + 
# #     print("vowel count is ", vowel_count)
# #     print(i)

# i = 0
# num = int(input("Enter a Number: "))
# for i in range(1,11):
#     result = num * i   
#     print(result)

# #vowels count:
# vowels = ["a", "e", "i", "o", "u"]
# vowel_count = 0
# word = input("Enter a Word: ")
# for i in word:
#     if i in vowels:
#         vowel_count = vowel_count + 1
# print(vowel_count)

# # 1
# # 12
# # 123
# # 1234
# # 12345
# for r in range(6):
#     for c in range(r):
#         print(c+1,end = "")
#     print("\n")

# # 12345  
# # 1234    
# # 123     
# # 12      
# # 1     
# n = 5
# for r in range(6):
#     for c in range(r):
#         print(c+1, end = "")
#         n = n -1
#     print(n) 

# # 54321
# # 4321
# # 321
# # 21
# # 1
# n = 5
# for r in range(n):
#     for c in range(n-r):
#         print(n-c, end="")
#     print("\n")

# # 1
# # 12
# # 123
# # 1234
# # 12345
# # 1234
# # 123
# # 12
# # 1
# rows = 10
# n = int(rows / 2) #5
# for r in range(rows): #10
#     if r < n: #0---4 n = 5
#         for c in range(r):
#             print(c+1,end="")
#     else:#after 4 r 5 6 7 8 9 
#         for x in range(r): #5,4,3
#             print(x+1,end="")
  
#     print("")
    
# #to print the numbers from the list.
# list = [1,4,9,16,25,36,49,64,81,100]   
# for i in list:
#     print(i)  

# #to find x in the tuple.
# tuple = (1,4,9,16,25,36,49,64,81,100)
# index = 0
# x = int(input("Enter x: "))
# for i in tuple:
#     print(i)
#     if i == x:
#         print("x found:",i)
#         break
# print("loop ended.")

# #to find x in the tuple.
# tuple = (1,4,9,16,25,36,49,64,81,100)
# index = 0
# x = int(input("Enter x: "))
# for i in tuple:
#     print(i)
#     if i == x:
#         print("x found at index:",index)
#     index += 1
# print("loop ended.")

# #even numbers in betweeen 1-100
# for i in range(2,101,2):
#     print(i)

# #print numbers from 100-1:
# for i in range(100,0, -1):
#     print(i)

# #multiplication table:
# num = 0
# i = 0
# num = int(input("Enter a Number you want the multiplication of: "))
# for i in range(1,11):
#     multi = num *i
#     print(f"{num}*{i}={multi}")

# #pass statement: used to pass the statement without an error.
# for i in range(5):
#     pass


# print("hehe")

# #multiplication table:
# num = int(input("Enter a number you want the multiplication of: "))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}") 

# #greet the people whose name starts with 's' in the list:
# l = ["Ram", "Sushma", "Sunil", "krishna"]
# for i in l:
#     if (i.startswith("S")):
#         print(f"Greetings! {i}")

# #star pattern:
# n = 3
# for r in range(3):
#     for c in range(r):
#         print()

# #prime number finding:
# n = int(input("Enter a number: "))
# for i in range(2, n):
#     if n%i == 0:
#         print("not prime")
#     else:
#         print("prime")



    





    







