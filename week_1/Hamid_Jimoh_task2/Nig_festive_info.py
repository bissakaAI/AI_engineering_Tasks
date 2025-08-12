#task9
#Ask for festival name
#Location
#month held

Fest_name= input("what is the name of the festival in question: ")
Location = input("Where is the festival celebrated: ")
Month_held = input("which month of the year does it take place: ")
fest_quoted = (f'\"{Fest_name}\"')
print (f"{fest_quoted} festival")
print (f"celebrated in",Location,"every", Month_held)

