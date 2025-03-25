# factorial
# 0! = 1
# 1! = 1
# n! = n * (n-1) *......* 5 * 4 * 3 * 2 * 1 

#factorial = n * factorial(n-1)

def factorial (n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number you want the factorial of: "))
print(f"The factorial of {n} is {factorial(n)}") #factorial(n) is calling the function.


