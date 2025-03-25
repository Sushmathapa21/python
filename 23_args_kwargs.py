#using *args in the parameter() to put all the values in the args

def addition(*args):
    x = sum(args) #prints the sum of the args.
    return x

final = addition(1,2,3,4,5,6,7,8,9,10,11,12) #calling the func()
print(final) #printing the func()



#**kwargs() #dict