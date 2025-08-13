#creating turples 
#using parentheses()
#Example 1: turples with multiple lines 
fruits = ("apple","banana","cherry")
print(fruits)

#without parentheses(turple packing)

numbeer =1,2,3
print(numbeer)

#single-item turple(must include a comma)
single_item =("apple",)
print(single_item) 
print(type(single_item))

#using the turple() constructor 
fruits_list =["apple","banana","cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

#characteristics of tuples 
##ordered 
color =("red","green","blue")
print(color[0])

#immutable
#color[1]="yellow"

#allow duplicates
numbers = (1,2,2,3,4)
print(numbers)

#mixed data types 
mixed = ("apple",3,True,5.6)
print(mixed)

#nested turples 

nested =(("a","b"),(1,2))
print(nested)

#turple operations 
#1. indexing 
fruits =("apple","banana","cherry")
print(fruits[1])
print(fruits[-1])

#2. Slicing

print(fruits[0:2])
print(fruits[::-1])

#3. concatenation

turple1=(1,2)
turple2 =(3,4)
result = turple1 +turple2
print(result)

#4. repition
nums=(1,2)
print(nums*3 )

#5. Membership

fruits=("apple","banana","cherry")
print("banana" in fruits )
print("grape" not in fruits )

# 6. Iterations
for fruit in fruits:
    print(fruit)


#UNPACKING TUPLES 
person =("john",25,"Nigeria") 
name,age,country=person 
print(name)
print(country)

#turple methods 
#turples have only 2 methods 
#dot count() and dot index 
numbers = (1,2,2,3,4)
print(numbers.count(2))
print(numbers.index(3))

#converting between list and turples 
t= (1,2,3)
lst = list (t)
lst.append(4)
print(lst)

#list back to tuple
t = tuple(lst)
print(t)

nums = (4, 1, 7, 3)

print(len(nums))   # 4
print(max(nums))   # 7
print(min(nums))   # 1
print(sum(nums))   # 