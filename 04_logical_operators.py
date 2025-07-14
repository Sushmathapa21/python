# (and or & not) conditions

#and (return TRUE only if both the conditions are true.)
x = 5
print(x<10 and x>10) #returns FALSE because both the conditions are not true, which is the second one.
print(x<10 and x>4) #returns TRUE because both the conditions are true.

#or (return TRUE if any one of the given condition is true.)
x = 5
y = 10
print(x<7 or y<7) #returns TRUE even though the second condition is false.

#not ( return True if the condition is false and return false if the condition is true.)
x = 5
y = 10
print(not(x>7)) #returns TRUE because the condition is actually false. because not is given in the true condition.


