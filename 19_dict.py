#ordered/ changable & no duplicates.
# empty dic: 
dict = {}
print(type(dict))

#stores data values in - key : value pairs.
dict = {"name": "Sush", "age": 20}
print(dict)
print(dict["age"]) #to print the specifict values.

#mixed dict
mixed_dict = {"one": 1, "2": 2,(1,2): "tuple"}
print(mixed_dict[(1,2)])
print(mixed_dict.get((1,2)))

#duplicate values overwrites existing values.
dict = {"name": "sush", "age": 20, "name": "Sushma"}
print(dict["name"])

#to get the values through keys:
dict = {"name": "Sush", "age": 20}
print(dict["name"])
#or
print(dict.get("name"))

#The values in dictionary can contain any data types.

#dict constructer()







# dict = {}
# user_input = 
# while True:
#     print("Enter 0 to EXIT."
#     "Enter 1 to ADD the value"
#     "Enter 2 to UPDATE the value"
#     "Enter 3 to REMOVE the value"
#     "Enter 4 to to VIEW dictionary.")
#     if 

mixed_dict = {
    1 : "one",
    "2" : "two",
    (1,2) : "tuple"
}

print(mixed_dict.get((1,2)))
print(mixed_dict[(1,2)])
      
student = {}
user_input = int(input(" press 1 to ADD any key value pairs \n press 2 to Update any key value pairs \n press 3 to DELETE any key value pairs \n "))
while True:
    key = int(input("Enter the key: "))
    value = int(input("Enter the value "))
    if user_input == 1:
        student[key] = value
       
    elif user_input == 2:
        key = int(input("Enter the key for which value should be updated: "))
        value = int(input("Enter the new value: "))
        student[key] = value
        
    elif user_input == 3:
        key = int(input("Enter the key for which value should be updated: "))
        value = int(input("Enter the new value: "))
        student.pop(key)

    else:
        print("Invalid")

    print(student)


    
    







