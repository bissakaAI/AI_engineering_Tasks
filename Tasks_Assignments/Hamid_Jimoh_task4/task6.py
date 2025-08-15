#TASK6
#WORD ANALYZER

user_input = input("Hi User please inpt a word: ")
print(len(user_input))
check_upper = user_input.isupper()
check_lower = user_input.islower() 
check_if_title = user_input.title()
user_input_reversed = list(user_input)
print(user_input_reversed[::-1])
