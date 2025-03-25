student = {
    "name": "Alice",
    "age": 20,
    "grades":{
        "math": 90,
        "history": 85,
        "science": 95
    },
    "contact": {
        "email": "alice@example.com",
        "phone": ["123-456-7890", "123456789", "987654321"]
    }
}
sum = 0
for k,v in student.items():
    if k == "grades":
        print(v)
        for i in v.values():
            sum += i
print(sum)

for k,v in student.items():
    if k == "contact":
        for x,y in v.items():
            if x == "phone":
                for i in range(len(y)):
                    print(f"number{i+1} : {y[i]}")



student = {
    'name':"Alice",
    'age':20,
    'grades':{
        'math': 90,
        'history':85,
        'science':80
    },
    'contact':{
        'email':'alice@example.com',
        'phone':[123456789,987654321]
    }
    
}

for k,v in z.items():
    if k == "contact":
        for i,j in v.items():
            if i == "phone":
                for x in j:
                    print(x)
                # print(j)

student = {
    "roll1": {
    'name':"Alice",
    'age':20,
    'grades':{
        'math': 90,
        'history':85,
        'science':80
    },
    'contact':{
        'email':'alice@example.com',
        'phone':[123456789,987654321]
    }
    }  
}

for k,z in student.items():
    print(k)
    print(z)

    for k,v in z.items():
        if k == "contact":
            for i,j in v.items():
                if i == "phone":
                    for x in j:
                        print(x)
                    


student = {
    'name':"Alice",
    'age':20,
    'grades':{
        'math': 90,
        'history':85,
        'science':80
    },
    'contact':{
        'email':'alice@example.com',
        'phone':[123456789,987654321]
    }
}

name = input("Enter the name: ")
age = int(input("Enter the age: "))

grade = {}
math = int(input("Enter the marks of math: "))
history = int(input("Enter the marks of history: "))
science = int(input("Enter the marks of science: "))
["grade"]["math"] = math
["grade"]["history"] = history
["grade"]["science"] = science

contact = {}
email = input("Enter the email: ")

phone = []
p1 = int(input("Enter the phone number1: "))
p2 = int(input("Enter the phone number 2: "))

["contact"]["email"] = email
["contact"]["phone"] = phone

["student"]["name"] = name
["student"]["age"] = age
["student"]["grade"] = grade
["student"]["contact"] = contact






