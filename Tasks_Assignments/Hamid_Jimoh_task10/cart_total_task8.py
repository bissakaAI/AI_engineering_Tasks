#task3
items = ["book","pen","bag"]
prices =[500,100,5000]
cart_t = {}
cart_total=0
count ={}

try:
    for i in items:
        item1=int(input((f"how many {i} do you want to buy")))
        count.update({i:item1})
        cart_t.update({i:item1* prices[items.index(f"{i}")] })
        cart_total += cart_t[i]
    print(f"you picked {count["book"]} books, {count["pen"]} pens, and {count["bag"]} bags \nTotal Price: {cart_total}")
except TypeError:
    print("calculation cant be performed on the type")
except Exception as e:
    print("this is a typeerror")