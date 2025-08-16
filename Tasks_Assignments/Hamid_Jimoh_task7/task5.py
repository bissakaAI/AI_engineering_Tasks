#collect names one after the other and store in a list
#collect the coresponding numbers one by one and store it in a list too

#create an empty dictionary
user_inputed= []
user_inputed2 = []
user_input11 = input("Please enter the name that you have their phone numbers: ").lower()
user_inputed.append(user_input11)
user_input21 = int(input(f"Please enter {user_input11}'s phone number: "))
user_inputed2.append(user_input21)
user_input12 = input("Please enter the name that you have their phone numbers: ").lower()
user_inputed.append(user_input12)
user_input22 = int(input(f"Please enter {user_input12}'s phone number: "))
user_inputed2.append(user_input22)
user_input13 = input("Please enter the name that you have their phone numbers: ").lower()
user_inputed.append(user_input13)
user_input23 = int(input(f"Please enter {user_input13}'s phone number: "))
user_inputed2.append(user_input23)
#convert the items in a list to turple
phone_number =tuple(user_inputed2)
names = tuple(user_inputed)

data_base = dict(zip(names,phone_number))
print(data_base)

user_prompted = input("whose number do you need: ").lower()
prompted_ans=data_base.get(user_prompted,"name not found")
print (prompted_ans)
