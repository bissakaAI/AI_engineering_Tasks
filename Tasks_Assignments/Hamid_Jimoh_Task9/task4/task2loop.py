#TASK2
#shopping list manager 
Empty_list =[]
count = 1
for x in range(1000000):
    promt_input =input("Do you want to add something to the shopping list? yes/no ").lower()
    if promt_input == "yes":
        shoping_item =input(f"please input the number {count} item you are shopping: ")
        Empty_list.append(shoping_item)
        count+=1
    elif promt_input == "no":
        print("Thank you for using our service")
        break
print(f"Find your shopping list below\n{Empty_list}")
