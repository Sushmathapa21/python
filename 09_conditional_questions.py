#Conditional question 1:

num1 = int(input("Enter a number1. "))
num2 = int(input("Enter a number2. "))
x = int(input("Enter 1 for addition, 2 for substraction, 3 for multiplication and 4 for division. "))
# print(type(x)) --- x should be in the int form.
if x == 1:
    add = num1 + num2
    print("The addition of num1 and num2 is ", add)
elif x == 2:
    sub = num1 - num2
    print("The subtraction of num1 and num2 is ", sub)
elif x == 3:
    mul = num1 * num2
    print("The multiplication of num1 and num2 is ", mul)
elif x == 4:
    div = num1 / num2
    print("The division of num1 and num2 is ", div)
else:
    print("Invalid")

# 2nd question:

x = int(input("Enter a Number: "))
if x > 0:
    print("The given number is positive.")
elif x < 0:
    print("The given number is negative.")
elif x == 0: #this line can have elif or else, any of the condition.
    print("The given number is zero.")
#else statement is not mandatory.

# 3rd question:

x = int(input("Enter a Number: "))
if x%2 == 0:
    print("The given number is even.")
else:
    print("The given number is odd.")

#when the statements are exchanged:

x = int(input("Enter a Number: "))
if x%2 != 0:
    print("The given number is odd.")
else:
    print("The given number is even.")

