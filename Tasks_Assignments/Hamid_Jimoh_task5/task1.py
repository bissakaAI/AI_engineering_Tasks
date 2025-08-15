#task 1:create and display
user_input=[]
print("Please enter names 3 of your favorite nigerian dishes:")
user_input1= input(f"input name of favorite dish 1: ")
user_input2= input(f"input name of favorite dish 2: ")
user_input3= input(f"input name of favorite dish 3: ")
user_input.append(user_input1)
user_input.append(user_input2)
user_input.append(user_input3)
user_input_tuple = tuple(user_input)
user_input_tuple1= ",".join(user_input_tuple)
print(user_input_tuple1)
user_input_tuple2="\n".join(user_input_tuple)
print(user_input_tuple2)