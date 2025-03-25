# file I/O
#python can be used to perfom operations on a file. (read & write data)
# types of all Files
#Text File: .txt, .docx, .log, etc
#Binary File: .mp4, .png, .jpeg, etc
#at last end ma memory ma chei bits (0,1) mei gayera save hunchha.

#mode:
#r  = read
#r+ = read & overwrite existing data.(pointer start ma huuncha.)(no truncate)
#w  = write by truncating(file ma bhako sab hatayera overwrite garcha)
#w+ = read & overwrite (truncate hunchha)(sab data del hunchha.)
#a  = append (sabai end ma store hunchha with all the data.)
#a+ = read & append (pointer at the end.)(no truncate)

#use readlines most of the time.

#to open a file:
# f = open("file name", "mode") 
#file name ma file ko naam and mode ma read("r") or write("w") mode. by default chei read mode ma hunchha if not specified.
# f = open("sample1.txt", "r")
# data = f.read() #returns the data of the file in form of a string
# print(data)
# print(type(data)) #str
# f.close() #to close the opended data.


# f = open("/Users/bhuwanthapa/Downloads/broadwaypython/sample1.txt")
# data = (f.read())
# print(data)
# print(type(data))
# #esari basya huncha
# """
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!
# """
# # print(data[7:14])
# # print(data[47:55])
# # print(data[70:75])

# # value = data.split()
# # print(value[1])
# # print(value[8])
# # print(value[-1])


# data = data.replace("Hello", "Hi").replace("testing", "tested").replace("Good", "Bad")
# print(data)

#read
# # readline()
# f = open("/Users/bhuwanthapa/Downloads/broadwaypython/sample1.txt")
# data1 = (f.readline())
# print(data1)  #returns the first line

# data2 = (f.readline()) 
# print(data2) #returns the second line.

# f = open("/Users/bhuwanthapa/Downloads/broadwaypython/sample1.txt")
# for i in f:
#     print(i)

# # #to return each line in form of list
# f = open("/Users/bhuwanthapa/Downloads/broadwaypython/sample1.txt")
# data = (f.readlines()) 
# # print(data)
# lst = []
# for i in data:
#     lst.append(i.strip("\n"))
# print(lst) 

#using list comprehension:



# #write garda tya already chha bhaney tya bhako data sab hatera naya data store hunchha.
# #chaina bhaney banaidinchha
# f = open("/Users/bhuwanthapa/Downloads/broadwaypython/sample100.txt", mode = "w")
# f.write("This is the file created by the write mode. \n")
# f.write("This comes in the second line.")


# create: 'x'
# x le paila banako file cha bhaney naya file banauna didaina. same file chha bhaney error dinchha. file chhaina bhaney naaya create gardinchha.

# # to create a txt file and ask user to enter data and store it.
# f = open ("/Users/bhuwanthapa/Downloads/broadwaypython/sample.txt", mode = "a")
# while True:
#     user_input = int(input("press 1 to write and press 0 to exit: "))
#     if user_input == 0:
#         print("Exited.")
#         break
#     elif user_input == 1:
#         text = input("Enter the text: ")
#         f.write(text)
#         f.write("\n")
#     else:
#         print("Invalid")

# deleting a file:
#using the os module.(it is the pre-installed module)
#module is the file written by another programmer, that we generally has a function we can use.
# if we want to install a module from the internet then, (pip/pip3 install modulename)
# import os
#os.remove(filename)

#to create a file and write:
# with open ("practice.txt", "w") as f:
#     f.write("Hi Everyone\nwe are learning File I/O.")
#     f.write("\nusing python\nI like programming in python.")
    
# #to replace "python" to "java" by using reading the file and then replacing the words.
# def replace():
#     with open("practice.txt", "r") as f:
#         file = f.read()
#         output = file.replace("python", "Java")
#         print(output)
#     #replacing the words in the actual file.    
#     with open("practice.txt", "w") as f:
#         f.write(output)
# replace()

##to check if the word "learning" exist in the txt file.    
# with open ("practice.txt", "r") as f:
#     data = f.read()
#     if "learning" in data:
#         print("Yes! The word 'learning' present in the text.")
#     else:
#         print("No! The word 'learning' is not present in the text.")

# #or
# def check():
#     word = "learning"
#     with open ("practice.txt", "r") as f:
#         data = f.read()
#         if (data.find(word)) != -1: #!= -1 mean its is equal to something which implies there is presence of that certain thing.
#             print("Found")
#         else:
#             print("Not found")
# check()

#to check in which line does the particular word "learning" exist.
# def check_line():
#     word = "learning"
#     line_no = 1
#     with open ("practice.txt") as f:
#         while True:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_line()


with open ("practice.txt", "r") as f:
    data = f.read()
    for i in data:
        str = str(i)
        if i%2 == 0:
            print("even")
            print(i.count())
        else:
            print("odd")







