#FRUIT COLLECTOR
print("hey user, kindly input your 5 favorite fruits")
ra_nge =tuple(range(1,6))
i = 1
favorite_fruits = set()
for i in ra_nge:
    user_input = input(f"kindly input your  favorite fruits {i}: ")
    i=i+1
    favorite_fruits.add(user_input)
print(f"Hey User Your favorite fruits are {favorite_fruits}")

    