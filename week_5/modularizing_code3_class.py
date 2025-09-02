# class Student:
#     def __init__(self,name,course,level):
#         print("creating a new student....")
#         self.name =name
#         self.course =course
#         self.level=level
#         print(f"Student {name} has been created! ")

# kemi = Student("kemi Adebayo","Computer Science",300)

# class NigerianStudent:
#     def __init__(self,name,state,course):
#         print(f"Step!:Creating students object...")
#         self.name =name #step 2: Assign name to this object
#         self.state_of_origin = state 
#         self.course = course
#         self.student_id =self.generate_id()
#         print(f"step 6: {self.name} from {self.state_of_origin} is ready ")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000,9999)}"
    

# ayo = NigerianStudent("Ayo daniel", "Lagos", "Street Statistics")
# tayo = NigerianStudent("Al", "gos", "atistics")
# print(ayo.student_id)


# class PhoneUser:
#     def __init__(self,name,network):
#         self.name = name 
#         self.network = network
#         self.airtime = 0
#         print(F"{self.name} joined {self.network} network")

#     def buy_airtime(self,amount):
#         self.airtime += amount 
#         return f"{self.name} now has #{self.airtime} airtime"


# #Creating multiple users 
# abeeb = PhoneUser("Abeeb Bakare","MTN")
# onisemo = PhoneUser("Onisemo Williams", "Airtel")

# print(abeeb.buy_airtime(500))
# print(onisemo.buy_airtime(1000))
# print(abeeb.airtime)
# print(onisemo.airtime)

class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name                   
        self.course = course              
        self.level = level                
        self.state_of_origin = state_of_origin  
        self.cgpa = 0.0                    

#Types of attributes 
#1. Instance attributes-unique to each object

student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)  
print(student2.name) 

class Student:
    university ="Federal University of Technology Akure"

    def __init__(self,name,course):
        self.name = name 
        self.course = course 
print(Student.university)
print(student1.university)