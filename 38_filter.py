#filter

numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x%2 == 0, numbers))
print(result)

numbers = [1,2,3,4,5,6,7,8,9,10]
def even_odd(n):
    return n % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(map(even_odd, numbers))
print(result)



