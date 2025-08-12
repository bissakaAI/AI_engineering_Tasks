#Collecting user data
#specify the various data inputs of the user
# a print statement asking for price of garri per paint in naira
# store it in a variable and covert it to float
# write a print statement showing the amount in naira and kobo

first_name = input("what is your first name: ")
last_name = input("What is your last name: ")
Age_Years = input("how old are you: ")


print(f"Good day {last_name} {first_name} what is the price of garri per paint?")
price_input= input("Input the price per paint: ")
price_ofGarri = float(price_input)
price_naira = int(price_ofGarri//1)
price_kobo = int(price_ofGarri*100 -(price_naira*100))
print(f"The price of garri per paint is {price_naira} Naira {price_kobo} kobo")
