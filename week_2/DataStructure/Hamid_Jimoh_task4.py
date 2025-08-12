# #TASK1
# #YOUR FAVOURITE LIFE QUOTE
# user_input = input ("hi user kindly input your favourite quote: ")
# print(f"\"{user_input.title()}\"")

# #TASK2
# #shopping list manager 
# Empty_list =[]
# shoping_items1 =input("please input what you are shopping: ")
# shoping_items2 =input("please input what you are shopping next: ")
# shoping_items3 =input("please input what you are shopping next: ")
# shopping_list=[shoping_items1,shoping_items2,shoping_items3]
# Empty_list=shopping_list.copy()
# print(Empty_list)

# #TASK3
# #WORD COUNTER
# user_sentense = input ("Hey user kindly input your sentense ")
# user_sentensesplited = user_sentense.split()
# word_count = user_sentensesplited.index(user_sentensesplited[-1]) +1 
# print (word_count)

# #task4
# #name organizer 
# user_input = input("please input the name of students and  seperate with spaces not commas: ").lower()

#TASK5
#student score tracker
user_input = input("please input the name of students: ")
user_input_list = user_input.split()
for x in user_input_list:
   scores= list(input(f"what is{x} score: "))
print(f"{user_input_list}\n{scores}")

