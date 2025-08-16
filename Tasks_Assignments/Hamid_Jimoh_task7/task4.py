#collect user input and split it
#covert input to set
#create an empty dictionary
user_input = set(input("Please enter 3 names seperated by commas: ").split(","))
diction_input={x: len(x) for x in user_input} 
print(diction_input)