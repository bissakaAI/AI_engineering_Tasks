#task 5:Modify tple indirectly 
user_input=[]
print("enter names of 3 items on your shopping list: ")
user_input1= input(f"input shopping item 1: ")
user_input2= input(f"input shopping item 2: ")
user_input3= input(f"input shopping item 3: ")
user_input4= input(f"input shopping item 4: ")
user_input5= input(f"input shopping item 5: ")
user_input.append(user_input1)
user_input.append(user_input2)
user_input.append(user_input3)
user_input.append(user_input4)
user_input.append(user_input5)
shopping_list = tuple(user_input)
shop_convert = list(shopping_list)
input("please input 2 more items to add to your shopping list")
user_input6= input(f"input shopping item 6: ")
user_input7= input(f"input shopping item 7: ")
user_input.append(user_input6)
user_input.append(user_input7)
shopping_list= tuple(shop_convert)
print(" | ".join(shopping_list))


