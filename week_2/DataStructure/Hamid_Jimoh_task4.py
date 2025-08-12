#TASK1
#YOUR FAVOURITE LIFE QUOTE
user_input = input ("hi user kindly input your favourite quote: ")
print(f"\"{user_input.title()}\"")

#TASK2
#shopping list manager 
Empty_list =[]
shoping_items1 =input("please input what you are shopping: ")
shoping_items2 =input("please input what you are shopping next: ")
shoping_items3 =input("please input what you are shopping next: ")
shopping_list=[shoping_items1,shoping_items2,shoping_items3]
Empty_list=shopping_list.copy()
print(Empty_list)

#TASK3
#WORD COUNTER
user_sentense = input ("Hey user kindly input your sentense ")
user_sentensesplited = user_sentense.split()
word_count = user_sentensesplited.index(user_sentensesplited[-1]) +1 
print (word_count)

#task4
#name organizer 
user_input = input("please input the name of students and  seperate with spaces not commas: ").lower()
user_input_spli =user_input.split(",")
print(user_input_spli)
user_input_spli.sort()
print(user_input_spli)
for x in user_input_spli:
     print(f"{x}\n")
    


#TASK5
#student score tracker
student_name = []
student_score =[]
user_input = input("please input the name of students: ").split(",")
student_name=user_input.copy()
print(student_name)
for x in student_name:
   student_score.append(float(input(f"what is {x} score: ")))
print(f"{student_name[0]}\t\t{student_score[0]}")
print(f"{student_name[1]}\t\t{student_score[1]}")
print(f"{student_name[2]}\t\t{student_score[2]}")

#TASK6
#WORD ANALYZER

user_input = input("Hi User please inpt a word: ")
print(len(user_input))
check_upper = user_input.isupper()
check_lower = user_input.islower() 
check_if_title = user_input.title()
user_input_reversed = list(user_input)

print(user_input_reversed[::-1])


#TASK 7
#LIST MANIPULATION
five_cities=["oyo","Ibadan","Abeokuta","Ikeja","Ogbomosho"]
user_input = input("please enter a  city you want me to add: ")
five_cities[2]= user_input
five_cities.pop(-1)
five_cities.insert(0,"ondo")
print(five_cities)

