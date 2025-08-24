#number 9
user_input=input("input any sentense: ").lower()
vowels= ("a","e","i","o","u")
vowel_count= 0
try:
    for x in vowels:
        vowel_a = user_input.count(x)
        vowel_count += vowel_a 
    print(vowel_count)
except Exception as e:
    print("you inputed a different type of data ")

finally:
    print("thank you for using the vowel count service")