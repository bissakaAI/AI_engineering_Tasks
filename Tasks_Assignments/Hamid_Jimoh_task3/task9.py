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