#dictionarry of available items
store={"Book": 10, "Pen": 20, "Bag": 5}
#user input for what they want to buy followed by the quantity

print("HELLO!! WELCOME TO OUR STORE".center(100))
print("We have BOOKS,PEN,and BAGS ")
purchase_1 = input("kindly input what you are buying from us: ").title()
purchase_quantity = int(input(f"how many {purchase_1} are you buying: "))
#DO THE ASSIGNMENT OPERATION FOR REDUCING QUANTITY AFTER EVERY PURCHASE
#PRINT THE LITEMS AND QUANTITY AVAILABLE BEFORE PURCHASE AND AFTER PURCHASE
print(f"Before Purchase:\t{store}")
store[purchase_1] -= purchase_quantity
print(f"After purchase:\t\t{store}")
