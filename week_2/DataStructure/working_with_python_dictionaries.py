#using curly braces 
student ={
    "name": "Ada",
    "age": 20,
    "course": "Computer science"
}
print(student)

#2. using the dict() constructor
student_info =dict(name="john", age=25,course="maths")
print(student_info)

#3. empty dictionary
empty_dict={}
print(empty_dict)

#DICTIONARY COMPREHENSION
#{key_expression: value_expression for items in iterable if condition }

#create a dictionary of numbers and their squares 
squares_num = {x: x**2 for x in range (1,6)}
print(squares_num)

#with condition 
#dictionary of even numbers and their cubes 
even_cube = {x: x**3 for x in range(1,10) if x%2 == 0}

#form existing dictionaries 
students = {"Ada":85,"John":40,"Musa":65}
#Filter students who passed (score >= 50)
passed_students ={name: score for name ,score in students.items() if score >= 50}
print(passed_students)

#using string keys 
names = ["Ada","John","Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

#accesssing  dictionary items
 # define a dictionary
student = {"name":"A", "age":20,"course":"computer science"}
#using key to access a dictionary 
print(student["name"])

#using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "not found"))


#Modifying Dictionaries 
student ["age"]= 21 #changes the value 
student["grade"] = "A" #adds new key--value pair
print (student)

#removing items from dictionaries 
#1. using (pop)
student.pop("grade")
#2. using popitem() removes last inserted key-value
student.popitem()
print(student)

#using del keyword 
del student["course"]
#using clear() - removes all items 
student.clear()
print (student)

#DICTIONARY METHODS 
person={"name":"emeka","age":30}
#1. keys()
print(person.keys())

#values()
print(person.values())
#items()
print(person.items())

#update()
person.update

#nested dictionaries 
students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}

print(students["student1"]["name"])  # Access nested data

#looping through dictionaries 
#define a dictionary
student={"name":"Ada","age": 20, "course":"Computer Science"}

#loop through keys 
for k in student:
    print (k)

#loop through values 
for k in student.values():
    print (k)

#loop through key -value pairs
for key , value in student.items():
    print(f"{key}: {value}") 

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"name: {student["name"]}")
print(f"Subjects: {' and '.join(student['subjects'])}")



