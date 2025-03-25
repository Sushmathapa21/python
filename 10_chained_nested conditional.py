#chained conditional:

x= 5
if x < 10:
    print("x is less than 10.")
if x > 3:
    print("x is more than 3.")

#nested conditional: #not suggested.

x = 5
if x > 0:
    if x < 10:
        print("x is a positive single-digit number.")
    else:
        print("x is a positive double digit number.")
else:
    print("x is not a negative number. ")

#without using nested:

x = int(input("Enter a number: "))
if x > 0 and x < 10:
    print("x is a positive single-digit number.")
elif x >= 10:
    print("x is a positive number but not a single-digit number.")
elif x < 0 :
    print("x is a negative number.")
else:
    print ("The number is zero.")


    