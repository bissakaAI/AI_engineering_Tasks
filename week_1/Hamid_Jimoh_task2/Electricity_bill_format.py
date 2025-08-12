#Electricity bill formatter
#creates input for full name unit consumed and cost per unit
Customer_full_name =input("Please enter Customers full name: ")
Unit_used = int(input("Enter unit consumed: "))
Cost_punit = float(input("what is the cost per unit: "))

Bill = Unit_used * Cost_punit

print(f"  RECEIPT FOR THE MONTH\nCustomers Name\t{Customer_full_name}\nUnit used\t{Unit_used}\nTotal Bill\t{Bill} Naira")
