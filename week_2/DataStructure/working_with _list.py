# #method 1 : Using square braclets
# empty_list =[1]
# print(empty_list) 

# #Method 2 : using the list()  constructor
# empty_list2 = list()
# print(empty_list2) 

# #creating a list with initial elements 
# #list of integers
# numbers= [1,2,3,4,5]
# print(numbers)

# #list of strings

# fruits= ["apple","banana","cherry"]
# print (fruits)

# #Mixed data types 
# mixed_list  =["Alice", 25 ,5.5,True]
# print(mixed_list)

# creating a list from another sequence

# #from a string (each character becomes ann element)
# chars=list("hello world")
# print(chars)


# #list from a turple and a range
# #we need to first define the turple and range before coverting to list
# my_turple = (10,20,40)
# list_turple = list(my_turple)
# print(list_turple)

# num_range = list(range(5))
# print(num_range)

# #creating a list using list comprehension 
# #squares of numbers 0-4
# squares= [x**2 for x in range(5)]
# print(squares)

# #even numbers between 0-10

# evens =[x for x in range(1,11) if x%2 ==0]
# print(evens)


# #creating a nested list
# #important for matrices or grouped data

# matrix = [[1,2],[3,4],[5,6]]
# print(matrix)


# #accessing elements in a nested list 
# print(matrix[0])
# print(matrix[0][1])


# #characteristics of a list 
# #1) ordered colection 
# fruits = ["mango", "orange", "banana"]
# print(fruits)       # ['mango', 'orange', 'banana']
# print(fruits[0]) 
# print(fruits[2])   

# #allows duplicate 

# items =["rice","beans","rice"]
# print (items)

# #3) mutable
# numbers =[1,2,3]
# numbers[1] = 20 
# print(numbers)

# #4) can contain different data types 
# mixed= [10,"Nigeria", 3.24,True]
# print(mixed)

# #can be nested 
# nested_list = [[1,2],["a","b"]]
# print(nested_list)
# print(nested_list[0:2])

# #dynamic size
# names = ["Ada"]
# names.append("chidi")
# print(names)


# #concatenation

# list1 = [1,2,3]
# list2=[4,5]
# result = list1 + list2
# print(result)

# #repetition 
# nums =[1,2]
# repeated = nums*3
# print(repeated)

# #indexing 

# fruits=["apple","banana","cherry"]
# print(fruits[0])
# print(fruits[-1])

# #slicing

# numbers =[0,1,2,3,4,5]
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[::2])

# #membership
# colors =["red", "green","blue"]
# print("green" in colors )
# print("yellow" not in colors )


# #length len()
# items = ["pen","book","laptop"]
# print(len(items))

# #min and max 
# num= [3,7,8,2,4,11,1]
# print (min(num))
# print(max(num))

# #sum
# numbers = [1,2,4,56,]
# print(sum(numbers))

# #list comprehension
# #this create sa list in a single line 
# squares= [x**2 for x in range(5)]
# print(squares)

# #create a duplicate list 
# a =[1,2,3]
# b = a.copy()
# print (b)

# #dot append() method

# fruits = ["apple","banana"]
# fruits.append("cherry")
# print(fruits)

# #dot insert()
# fruits = ["apple","banana"]
# fruits.insert(1,"orange")
# print(fruits)

# #dot extend()
# fruits = ["apple","banana"]
# tropical= ["mango","pineapple"]
# fruits.extend(tropical)
# print(fruits)

# # remove()
# fruits = ["apple","banana","cherry"]
# fruits.remove("cherry")
# print(fruits)

# # pop()
# fruits = ["apple","banana","cherry"]
# last_fruit=fruits.pop(1)
# print(last_fruit)               #removes and return element at a given index

# print (fruits) #the pop i.e removal has been effected 


# # dot clear 

# fruits = ["apple","banana","cherry"]
# fruits.clear()
# print(fruits)


# #dot index   
# #returns the index of the first occurence of a value 

# fruits = ["apple","banana","cherry"]
# position = fruits.index("banana")
# print(position)

# #dot count()
# fruits = ["apple","banana","cherry"]
# print(fruits.count("apple"))  #check diff between sring argument and variable arguments 

# #dot sort 
# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)  
# # Output: [1, 2, 3, 4]


# # sort in descending order 
# numbers = [3, 1, 4, 2]
# numbers.sort(reverse=True) #default argument would be reverse=false
# print(numbers)  

# fruits = ["apple", "banana", "cherry"]
# fruits.reverse()
# print(fruits)                       #this one reverses the order of the list
# # Output: ['cherry', 'banana', 'apple']

# fruits = ["apple", "banana", "cherry"]
# new_list = fruits.copy()
# print(new_list) 
