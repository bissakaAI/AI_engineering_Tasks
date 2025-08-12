#number1
#code to take input 
change_case = input("pleade input what you want in uppercase: ")
print(change_case.upper())


#number 2
word = "python"
print(f"{word[0]} and {word[-1]}")

#number3 

input("what is your name: ")
print("\"Hello,!\" where is the user's input")

#number 4
word = "i am next"
count = word.find(word[-1]) + 1
print(count)


#number5

word = "Hello World"
print(word.replace("World","Python"))


#TASK2
#number 6
word = "check me in python"
print("python" in word)

#number 7
#a program to reverse a string without using slicing
word = "check this reverse"
reversed_word= reversed(word)
reversed_word2= "".join(reversed_word)
print(reversed_word2)

#number8
word = "    i love allah   "
print(word.strip())

#number 9
user_input=input("input any sentense: ").lower()
vowels= ("a","e","i","o","u")
vowel_a = user_input.count("a")
vowel_e = user_input.count("e")
vowel_i = user_input.count("i")
vowel_o = user_input.count("o")
vowel_u = user_input.count("u")

vowel_count = vowel_a + vowel_e + vowel_i +vowel_o +vowel_u
print(vowel_count)


#number 10
string_word = "1234"
string_conv = int(string_word)
multi_string = string_conv * 2 
print(multi_string)



#TASK3
#number 11
fruits_string= "apple,banana,orange"
fruits_list =print(fruits_string.split())
print(fruits_string)

#number 12
user_input = input ("please input the sentence you want me to format: ").split()
print("\n".join(user_input))

#number 13
word = "i want a new home "
print(word.replace(" ","_"))

#number 14
word = "Banana"
count_b = word.count("a")
print(count_b)

#number 15

word ="\"https://\" the boy is a goat"

print(word.startswith("\"https://\""))