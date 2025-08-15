#SETS IN PYTHON
#creating sets 
#1. using curly braces 
fruits = {"apple","banana","mango"}
print(fruits)

#using the set() constructor
numbers = set([1,2,3,4]) 
print(numbers)

#Creating an empty set ** must be set(), not {}
empty_set = set()
print(empty_set)

# from a string (duplicate removed automatically  )
letters = set("mississippi")
print(letters)

#set operations 
#adding elements 

colors = {"red","blue"}
colors.add("green")
print (colors)

#removing Elements 
colors.remove("blue") # removes an element ans raises an error if not found 
colors.discard("yellow")#removes if found, no error if missing
print(colors)

#pop an element 
colors = {"red","blue","green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining:", colors)


#clear a set 
colors.clear()
print(colors)

#Mathematical set operations 
set1 = {1,2,3,4}
set2 ={3,4,5,6}

#1. Union
print(set1 | set2)
print(set1.union(set2))

#intersection
print(set1-set2)
print(set1.difference(set2))

#symmetric difference 
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

#collecting unique visitors to an event 
visitors = set()
#Adding visitors 
visitors.add ("chinedu")
visitors.add("Aisha")
visitors.add ("chinedu")
print("Visitors: ",visitors)

# Checking if a visitor attended
# (Dont worry if you can't figure this part out yet. We will discuss it properly later in the course.)

name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")