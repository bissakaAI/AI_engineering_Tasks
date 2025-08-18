#task3
items = ["book","pen","bag"]
prices =[500,100,5000]
cart_t = {}
cart_total=0

item1=int(input((f"how many {items[0]} do you want to buy")))
item2 =int(input((f"how many {items[1]} do you want to buy")))
item3=int(input((f"how many {items[2]} do you want to buy")))
cart_t.update({"book":item1*prices[0] ,"pen":item2*prices[1]  ,"bag":item3*prices[2] })
print(cart_t)
cart_total += cart_t["book"]
cart_total += cart_t["pen"]
cart_total += cart_t["bag"]
print(f"you picked {item1} books, {item2} pens, and {item3} bags \nTotal Price: {cart_total}")
