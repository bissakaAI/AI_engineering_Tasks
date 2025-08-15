items = ["rice","yam","oat","milk"]
item_price_dict = {}
for i in items:
    users_price= input(f"what is the price of {i}: ")
    item_price_dict[f"{i}"]=users_price
    print(item_price_dict)
need_toupdate=input("did you make a mistake you want to update? ")
for x in items:
    if need_toupdate  :
        item_toupdate =input("what is the item you want to update: ").lower()
        new_price = input(f"what is the new price of {item_toupdate}: ")
        item_price_dict[item_toupdate] = new_price
print(item_price_dict)