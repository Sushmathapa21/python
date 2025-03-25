#only inheritance needed in python.

# class variable:
#     def __init__(self,name,age): #("init" ra "self" chei hunai parcha constructor lai) #constructer (sure huney kura haru.)
        # self.name = name

class person:
    # per = 1 #class attribute #if sabai ko condition funfill hunchha bhaney.

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        return(f"Hello, my name is {self.name} and i am {self.age} years old.")  

# print(person.per) #calling class attribute.

#creating instances(objects) of the person class.
person1 = person("sushma",20)  
person2 = person("Sush",21)  

#acessing instances variables and calling functions.
print(person1.name)
print(person2.age)

message = person1.greet()
print(message)

