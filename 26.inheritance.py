#inheritance:
#parent-child relationship. #parent class ko child class ma sab parchha but child class ko qualities animal ma hunna.
#single inheritance:
class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def bark(self):
        return "Dog barks."
    
my_dog = Dog()
print(my_dog.speak()) 
print(my_dog.bark())

#multiple inheritance: # parents(father/mother) but only 1 child.


#multilevel inheritance: "grandparent, parent and child."

#super() #calls the methods of the parents.