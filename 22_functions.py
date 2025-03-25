#return bhanechhi chei naya variable ra print statemnet chei dinai paryo.

#no parameter() and no return type
def addition():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1+num2
    print(result)

addition()

#eg:
# div:
def div():
    num1 = int(input("Enter the Num1: "))
    num2 = int(input("Enter the Num2: "))
    result = num1 / num2
    print(result)

div()

#no parameter() but return type
def addition():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1+num2
    return result #return use garda chei naya variable banaune.

finalresult = addition()
print(finalresult)
#tala ni func use garna milyo

#eg:
#mult with no parameter() but return type:
def mult():
    num1 = int(input("Enter the Num1: "))
    num2 = int(input("Enter the Num2: "))

    result = num1 * num2 #mathi parameter ma x,y define nagarexi tala ni use garna mildaina so num1 ra num2 de4fine garechhi tyei nai use garna parchha
    return(result)

final_result = mult()
print(final_result)

#parameter and no return type:
def addition(x,y):
    result = x+y
    print(result)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

addition(num1,num2)
addition(10,20)

#eg:
#addition with parameter() but no return type:
def add(x,y):
    add = x+y
    print(add)

num1 = int(input("Enter the Num1: "))
num2 = int(input("Enter the Num2: "))

add(num1,num2)

#parameter and and return type both:
def addition(x,y):
    result = x+y
    return result

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

finalresult = addition(num1, num2)
print(finalresult)

#eg:
#sub of two numbers with para() and return type:
def sub(x,y):
    result = x-y
    return result

num1 = int(input("Enter the Num1: "))
num2 = int(input("Enter the Num2: "))

final_result = sub(num1, num2)
print(final_result)


