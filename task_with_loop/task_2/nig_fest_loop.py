#task9
#Ask for festival name
#Location
#month held
fest_option =input("Do you know any festival and the respective location it is celebrated. Pick (Yes/no): ").lower()
if fest_option == "yes":
    Fest_name= input("what is the name of the festival in question: ")
    Location = input("Where is the festival celebrated: ")
    Month_held = input("which month of the year does it take place: ")
    fest_quoted = (f'\"{Fest_name}\"')
    print (f"{fest_quoted} festival")
    print (f"celebrated in",Location,"every", Month_held)
else:
    print("Thank you for trying to participate,but the program only needs people with festival information")


