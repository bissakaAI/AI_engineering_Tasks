# my_module/main.py

import first
import second

#lets use the function in the first.py file 
print("====== MATH FUNCTIONS=====")
print("sum: ", first.add(2,3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))


#lets use the functions in the second.py file

print ("======STRING FUNCTIONS======")
print(second.greet("Hamid"))
print("reverse of python: ", second.reverse_string("python"))
print("character count in sentense: ", second.count_characters("adamawa is boiling"))
print("word count in a sentence ", second.count_words("Adamawa is boiling"))