#task4
#name organizer 
user_input = input("please input the name of students and  seperate with spaces not commas: ").lower()
user_input_spli =user_input.split(" ")
user_input_spli.sort()
print(user_input_spli)
for y in user_input_spli:
     print(f"{y}\n")