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

# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name                   
#         self.course = course              
#         self.level = level                
#         self.state_of_origin = state_of_origin  
#         self.cgpa = 0.0                    

# #Types of attributes 
# #1. Instance attributes-unique to each object

# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# print(student1.name)  
# print(student2.name) 

# class Student:
#     university ="Federal University of Technology Akure"

#     def __init__(self,name,course):
#         self.name = name 
#         self.course = course 

# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# print(student1.university)

# class Student:
#     def __init__(self, name, course, level):
#         # Attributes
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False
    

#      # Method: action the student can do
#     def pay_school_fees(self):                   
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     # Method: another action
#     def register_courses(self):                   
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
    
#       # Method: calculates CGPA
#     def calculate_cgpa(self, grades):           
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"
    
# # Using methods
# Abiodun = Student("Abiodun Akinola", "Gistology", 600)
# print(Abiodun.pay_school_fees())        
# print(Abiodun.register_courses())       
# print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5])) 


# #i want to create a bankaccount class:
# import random
# class Bankaccount:
#     minbalance= 1000
#     bank_name = "Hamfinance"
#     def __init__(self,name,type_of_account):
#         self.name=name
#         self.balance = Bankaccount.minbalance
#         self.type_of_account=type_of_account
#         self.account_number =self.accnumber_generation()

#     def accnumber_generation(self):
#         accnumber= ""
#         list_r = []
#         for x in range(0,10):
#             list_r.append(x)
#         while len(accnumber)<10:
#             accnumber += str(random.choice(list_r))
#         return accnumber
    
#     def deposit(self,amount):
#         if amount >0:
#             self.balance += amount
#             return f"you have succesfully deposited {amount} into  {self.name}'s {self.type_of_account}'s account. "
#         return "invalid deposit amount"
#     def transfer(self,receiver,amount):
#         if amount>0 and amount<=self.balance:
#             self.balance -= amount #remove money
#             receiver.balance += amount #receiver receives money
#             return "trnsfer succesful"
#         return "insuffucient balance"
#     def withdraw(self, amount):
#         """Remove money from the account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount  # Method changes attribute
#             return f"₦{amount:,} withdrawn from {self.name}'s account. New balance: ₦{self.balance:,}"
#         return "Insufficient funds or invalid amount"

# adunni_account = Bankaccount("Adunni Olaleye","savings")
# tolu_account = Bankaccount("adeniyi toluwani","savings")

# print(f"Owner: {adunni_account.name}")
# print(f"Bank: {adunni_account.bank_name}")
# print(f"Account Number: {adunni_account.account_number}")

# print(tolu_account.deposit(5000))
# print(tolu_account.balance)
# print(tolu_account.withdraw(2000))
# print(tolu_account.transfer(adunni_account,1000))
# print(adunni_account.balance)

# ade =Bankaccount("a adeyemi","current")

# print(ade.balance)


# class NigerianBankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.owner = owner
#         self._balance = initial_balance        # Protected attribute
#         self.__pin = "1234"                   # Private attribute
#         self._transaction_history = []        # Protected attribute
    
#     # Public methods - anyone can use these
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             self._transaction_history.append(f"Deposited ₦{amount:,}")
#             return f"₦{amount:,} deposited successfully"
#         return "Invalid deposit amount"
    
#     def withdraw(self, amount, pin):
#         if self.__verify_pin(pin):  # Uses private method
#             if amount <= self._balance:
#                 self._balance -= amount
#                 self._transaction_history.append(f"Withdrew ₦{amount:,}")
#                 return f"₦{amount:,} withdrawn successfully"
#             return "Insufficient funds"
#         return "Invalid PIN"
    
#     def check_balance(self, pin):
#         if self.__verify_pin(pin):
#             return f"Current balance: ₦{self._balance:,}"
#         return "Invalid PIN"
    
#     # Private method - only the class can use this
#     def __verify_pin(self, entered_pin):
#         return entered_pin == self.__pin
    
#     # Protected method - subclasses can use this   
#     def _get_transaction_history(self):       #this is a getter ...
#         return self._transaction_history.copy()


# # Using the encapsulated account
# ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# # These work - public interface
# print(ibrahim_account.deposit(10000))      # ₦10,000 deposited successfully
# print(ibrahim_account.withdraw(5000, "1234"))  # ₦5,000 withdrawn successfully
# print(ibrahim_account.check_balance("1234"))   # Current balance: ₦55,000


# Parent class - Base Nigerian Person
class NigerianPerson:
    def __init__(self, first_name, last_name, state_of_origin):
        self.first_name = first_name
        self.last_name = last_name
        self.state_of_origin = state_of_origin
        self.can_speak_english = True
    
    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
    
    def greet(self):
        return "Good morning!"
    
    def speak_local_language(self):
        return "I speak my local language"

# Child class 1 - Nigerian Student inherits from NigerianPerson
class NigerianStudent(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, course, level):
        # Inherit parent's initialization
        super().__init__(first_name, last_name, state_of_origin)
        # Add student-specific attributes
        self.course = course
        self.level = level
        self.cgpa = 0.0
    
    # Override parent method with student-specific version
    def introduce(self):
        parent_intro = super().introduce()  # Get parent's introduction
        return f"{parent_intro}. I'm a {self.level} level {self.course} student"
    
    # Add student-specific methods
    def study(self):
        return f"{self.first_name} is studying {self.course}"
    
    def take_exam(self):
        return f"{self.first_name} is writing {self.course} exam"

# Child class 2 - Nigerian Worker inherits from NigerianPerson
class NigerianWorker(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, job_title, company):
        super().__init__(first_name, last_name, state_of_origin)
        self.job_title = job_title
        self.company = company
        self.salary = 0
    
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I work as a {self.job_title} at {self.company}"
    
    def work(self):
        return f"{self.first_name} is working as a {self.job_title}"
    
    def receive_salary(self, amount):
        self.salary += amount
        return f"{self.first_name} received ₦{amount:,} salary"

# Child class 3 - Nigerian Teacher (inherits from NigerianWorker)
class NigerianTeacher(NigerianWorker):
    def __init__(self, first_name, last_name, state_of_origin, subject, school):
        # Teacher is a type of worker
        super().__init__(first_name, last_name, state_of_origin, "Teacher", school)
        self.subject = subject
        self.students = []
    
    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}. I teach {self.subject} at {self.company}"
    
    def teach(self):
        return f"Teacher {self.first_name} is teaching {self.subject}"
    
    def grade_students(self):
        return f"Teacher {self.first_name} is grading {self.subject} assignments"
    
    # Using inheritance
# Create different types of people
student = NigerianStudent("Kemi", "Adebayo", "Lagos State", "Computer Science", 300)
worker = NigerianWorker("Chinedu", "Okafor", "Anambra State", "Software Developer", "Sail Innovation Lab")
teacher = NigerianTeacher("Chris", "Ekwugum", "Lagos State", "Data Science", "Sail Innovation Lab")

# All inherit basic Nigerian person abilities
print("=== Basic Inherited Methods ===")
print(student.greet())                    # Good morning! (inherited)
print(worker.speak_local_language())      # I speak my local language (inherited)
print(teacher.greet())                    # Good morning! (inherited)

print("\n=== Customized Introductions ===")
print(student.introduce())    # Customized for students