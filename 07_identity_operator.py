# memory location ko basis ma check garchha. 
# value eutai bhayeni location eutai chhaina bhneny false aaucha.

#is:
num1 = [1,2,3] #location = 001
num2 = [1,2,3] #location = 002
result = num1 is num2
print(result) #returns False because num1 doesn't have same objects as num2, even if they have the same content, because their location is different.

num1 = [1,2,3] 
num2 = [1,2,3]
a = num1 == num2 # -> True because x is equal to y but,
b = num1 in num2 
c = num1 is num2 # -> False because eventhough they have the same objects they're not same.

print(a,b,c)


# is not:
num1 = [1,2,3] #location = 001
num2 = [1,2,3] #location = 002
result = num1 is not num2 # TRUE because num1 is not num2
print(result)

num1 = [1,2,3] #location = 001
num2 = [1,2,3] #location = 002
result = num1 != num2 # FALSE because num1 is equal to num2
print(result)