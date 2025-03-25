#exception
#python ma built in error ni hunchha.
#exceptions : user le error garda aaune error.
#exceptions handling:
#try block: use garnai paryo try le chei check garchha condition ani if error aauchha bhaney chei it will send it to the except block.
#except block: esle chei error ko nam linchha ani tyo case ma k garney bhanera bhanchha.
#error ko nam thachaina bhaney, except exception as e garney
# where exception ma error bhanera diney ani as euta variable rakhexi what the error id tyo dinchha
# like: except Exception as e:
            #print(e)

# like: if x<1 :
            #raise exception("error")

#custom: kaile error aaudaina 
#creation of custom exception to handle different cases:

# class negative_error(Exception):
#     def __init__(self,message):
#         super().__init__(message)



#changing the input str to int if the value provided is int while concatenation.

try:
    n1 = input("Enter the num1: ")
    n2 = input("Enter the num2: ")
    if n1.isdigit() and n2.isdigit(): #checks if the provided value is in int or not.
        result = int(n1) + int(n2)
        # print(type(result)) #int

    else:
        result = n1 + n2

    print(result)


except Exception as e:
    print(e)








