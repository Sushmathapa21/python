# # using if:
# x = 1
# if x == 1:
#     print("The value of x is 1. ") # (give indentation as a single tab button.)

# # using if and else:
# a = 5
# if a == 5:
#     print("The value of a is 5. ")
# else: #else ma normally kei condition aaudaina, else means every other conditions besides the stated ones.
#     print("The value of a is not 5. ")

# #using if, elif and else:
# b = 10
# if b > 10:
#     print ("b is more than 10. ")
# elif b < 10:
#     print("b is less than 10. ")
# elif b == 10:
#     print("b is euqual to 10. ")
# else: #(else ma kaile ni condition hudaina as it is the last condition to be followed if none of the other satisfies.)
#     print("Invalid")

# classwork:

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
user_input = int(input("Enter '1' for addition\n Enter '2' for Subtraction\n Enter '3' for multiplication\n Enter '4' for division\n"))
if user_input == 1:
    print(f"The addition of num1 and num2 is {num1 + num2}")
elif user_input == 2:
    print(f"The subtraction of num1 and num2 is {num1 - num2}")
elif user_input == 3:
    print(f"The multiplication of num1 and num2 is {num1 * num2}")
else:
    print(f"The division of num1 and num2 is {num1 / num2}")

