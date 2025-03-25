#unordred : cannot be specified by index or keys.
#unchangable : no modifications
#no duplicate values: duplicate values will only be printed once.
#can contain different datatypes.
# ** True & 1 are considered same values in sets hence considered duplicate.**
#if "Ture" & "1" then returns "True or 1" only.
# ** False & 0 are considered same values in sets hence considered duplicate.**
#if "False" & "0" then returns "False or 0" only.
#Duplicate not allowed: Sets cannot have two items with the same value.
#The set() Constructor : with double brackets (()).
#set ma for loop matrai

# set = set() #empty set
# a = type(set)
# print(a)

#####set methods:

# .add() #to add the element. last ma bascha
# .update() #for concatenation of two set of item of the variables.
# .remove() #returns ERROR when the item is not present in the set.
# .discard() #doesnot return error and returns the same set.
# .pop() #randomly euta item select garera euta item hataucha as there is no index
# .clear() empty numchha set as san item clear huncha
# .copy() returns the copy of the set.
# del 

#join
# .union() or |
# set1 = {1,2,3,4,5}
# set2 = {"apple", "orange", "cherry"}
# set3 = {"dog", "cat"}
# set4 = set1 | set2 | set3
# set4.union(set1,set2,set3)
# print(set4)

##intersection: makes a new variable.
##.intersection() or &
# set1 = {1,2,3,"dog",4,5}
# set2 = {"apple", "orange", "cherry", "dog"}
# set3 = {"dog", "cat"}
# set4 = set1.intersection(set2,set3)
# print(set4)

##.intersection_update() : doesn't make a new variable.
# set1 = {"apple", "banana", "dog"}
# set2 = {"apple", "dog", "cherry"}
# set3 = {"dog", "cat"}
# set1.intersection_update(set2,set3)
# print(set1)

#.isdisjoiont()
#intersection chhaina bhney - True
#intersection chha bhaney - False

#.issubset()
#returns true is the other set contains the elements of this particular set.
#else returns False.

#.issuperset()
#returns true if all the items in the particular set exists in the original set.
#else returns False.

#.union(): makes a new variable.
#returns all the items of all the sets while returning the duplicate values only once.

#.update(): without making a new variable.
#returns all the items of all the sets while returning the duplicate values only once.

#symmetric_difference(): makes a new variable.
#returns all the items of the sets besides the inttersected items.

#.symmetric_difference_update() : without making a new variable.
#returns all the items of the sets besides the inttersected items.

#.difference(): makes a new variable.
#difference garchha hence intersected items aaudaina but from the item that is being differentiated.

#.difference_update(): doesn't make a new variable.
#difference garchha hence intersected items aaudaina but from the item that is being differentiated.

#.intersection(): makes a new variable.
#returns only the intersected items.

#.intersection update(): doesn't make a new variable.
#returns only the intersected items.


