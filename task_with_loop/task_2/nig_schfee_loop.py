#simulated ussd menu interaction
#Dislay welcome message
#ussd code input an store in a variable
#print options to select from
#print select from the options shown

print("Use *312# to start the ussd service")
Ussd_code = input("Enter ussd code: ")
Balance= 2000
balance = 2 
price_pergb = 1000
if Ussd_code == "*312#":
    print("\t\tWELCOME TO THE USSD SERVICE\n\t\tEkabor si service wa")
    print("1. My account\n2. Check balance\n3. Buy Data\n4. exit ")
    print("Please kindly pick from the option 1-5: ")
    choice_1 = int(input(""))
    if choice_1 == 1:
        print(f"Nice, you have selected option {choice_1}")
        print("1. My number\n2. My plan\n3. personal details")
        choice_2 = int(input(""))
        if choice_2 == 1:
            print("09023671234")
        elif choice_2==2:
            print("You are on better talk plan")
        elif choice_2==3:
            print("Your name is Hamid")
            print("you are from ibadan")
            print("your nin is not linked yet")
        else:
            print("kindly input a valid choice")
    elif choice_1 == 2:
        print(f"Nice, you have selected option {choice_1}")
        print(f"Your curent Balance is {Balance} Naira and {balance} gb")
    elif choice_1 == 3:
        print(f"Nice, you have selected option {choice_1}")
        print("1. Do you want to buy Data?\n2. Do you want to buy airtime?")
        choice_3 =int(input(""))
        if choice_3 == 1:
            amount_data = float(input("Input the amount you want to buy in Gb"))
            charges = amount_data * price_pergb
            if charges > Balance:
                print("Insufficient funds")
            else:
                print("Data topup sucessful")
                Balance-=charges
        elif choice_3==2:
            amount_airtime = float(input("Input the amount you want to buy in Naira"))
            if amount_airtime > Balance:
                print("Insufficient funds")
            else:
                print("Airtime topup sucessful")
                Balance-= amount_airtime

    else:
        print("exiting service")
else:
    print("Invalid ussd")

print(f"Thank you for using our service")