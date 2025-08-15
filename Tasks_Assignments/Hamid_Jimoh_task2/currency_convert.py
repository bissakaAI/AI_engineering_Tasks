#Ngeria currency converter

Amount_Naira= float(input("How much in Naira is to be converted: "))
Exchange_dollar =float(input("What is the current exchange rate of dollar to Naira: "))
Exchange_pounds =float(input("What is the current exchange rate of pounds to Naira: "))

Naira_exchanged_dollar = Exchange_dollar *Amount_Naira
Naira_exchanged_pounds = Exchange_pounds *Amount_Naira

print(f"CURRENCY CONVERTER\nAmount in naira\t \t{Amount_Naira}\nAmount in dollar\t{Naira_exchanged_dollar}\nAmount in pounds\t{Naira_exchanged_pounds}")
