# #purple practice 

# #task 1:create and display
# user_input=[]
# ran_ge= 4
# i= tuple(range(1,ran_ge))
# print("Please enter your three favorite dishes:")
# for x in i :
#     user_input1= input(f"input your favorite nigerian dish {x}: ")
#     user_input.append(user_input1)
# user_input_tuple = tuple(user_input)
# print(user_input_tuple)
# for v in user_input_tuple:
#         print(f"{v}\n")


# #task 2: Turple and input
# user_input=[]
# ran_ge= 6
# i= tuple(range(1,ran_ge))
# print("enter names of your five best friends below")
# for x in i :
#     user_input1= input(f"input your best friend {x}: ")
#     user_input.append(user_input1)
# user_input.reverse()
# user_input_tuple = tuple(user_input)
# print(user_input_tuple)


# #task3 turple operation
# user_input=[]
# ran_ge= 6
# i= tuple(range(1,ran_ge))
# print("enter names of five nigerian states below")
# for x in i :
#     user_input1= input(f"enter the number {x} nigerian: ")
#     user_input.append(user_input1)
# user_input_tuple = tuple(user_input)
# print(f"the first state in the turple is:  {user_input_tuple[0]}")
# print(f"the last state in turple is: {user_input_tuple[-1]}")
# print( "lagos" in user_input_tuple)


# #TASK4
# data=("First_name","Age","Favorite_color","Home_town")
# user_input = tuple(input("please input your details using the format as shown Firstname,Age,Favorite color,Hometown: ").split(",",))
# user_input1 = user_input
# First_name,Age,Favorite_color,Home_town = user_input1
# for x in user_input:
#     print(f"{x}")


# #TASK5
# #MODIFY TURPLE INDIRECTLY 
# user_input=[]
# ran_ge= 4
# i= tuple(range(1,ran_ge))
# print("enter names of 3 items on your shopping list: ")
# for x in i :
#     user_input1= input(f"input shopping item {x}: ")
#     user_input.append(user_input1)
# shopping_list = tuple(user_input)
# shop_convert = list(shopping_list)
# input("please input 2 more items to add to your shopping list")
# ran_ge= 3
# i= tuple(range(1,ran_ge))
# for x in i :
#     shopping_list1= input(f"input shopping item {x}: ")
#     shop_convert.append(shopping_list1)
# shopping_list= tuple(shop_convert)
# print(" | ".join(shopping_list))


#TASK6
#ATTENDANCE TRACKER
days_of_the_week =("Monday","Tuesday","wednesday","thursday","friday","saturday","sunday")
months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
user_input_name = input ("input your full name : ")
user_input_gender = input ("Are ypou a male or female: ")
user_input_track = input ("what course track did you enroll for: ")
user_input_month = int(input ("input Month using the format e.gmay is 05: "))
user_input_day = int(input ("current day number e.g (1-7): "))
correct_month = months_of_year[user_input_month -1]
correct_day=days_of_the_week[user_input_day -1]
print(f"Name:\t{user_input_name}\nGender:\t{user_input_gender}\nTrack:\t{user_input_track}\nmonth:\t{correct_month}\nDay:\t{correct_day}")
