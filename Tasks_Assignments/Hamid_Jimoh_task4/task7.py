#TASK 7
#LIST MANIPULATION
five_cities=["oyo","Ibadan","Abeokuta","Ikeja","Ogbomosho"]
user_input = input("please enter a  city you want me to add: ")
five_cities[2]= user_input
five_cities.pop()
five_cities.insert(0,"saki")
print(five_cities)