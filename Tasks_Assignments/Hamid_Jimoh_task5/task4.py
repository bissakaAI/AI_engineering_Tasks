#TASK4 turple unpacking
data=("First_name","Age","Favorite_color","Home_town")
user_input = tuple(input("please input your details using the format as shown Firstname,Age,Favorite color,Hometown: ").split(",",))
user_input1 = user_input
First_name,Age,Favorite_color,Home_town = user_input1
print(f"first name: {First_name} \nAge: {Age} \nFavorite colour: {Favorite_color} \nTown: {Home_town}")
