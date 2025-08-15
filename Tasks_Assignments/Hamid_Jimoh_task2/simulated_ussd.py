#simulated ussd menu interaction
#Dislay welcome message
#ussd code input an store in a variable
#print options to select from
#print select from the options shown
print("\t\tWELCOME TO THE USSD SERVICE\n\t\tEkabor si service wa")
Ussd_code = input("Enter ussd code: ")
print("1. My account\n2. Check balance\n3. Buy Data\n4. Gift data/Aitime\n5. Next ")
print("Please kindly pick from the option 1-5: ")
choice_1 = int(input(""))
print(f"Nice, you have selected option {choice_1}")
print("Do you want to buy Data?\nHow much Data do you want to buy")
balance = int(input(""))
price_pergb = 200
num_gig = balance/price_pergb

print(f"You have sucesfully purchased {num_gig} gb of data")