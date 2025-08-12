# #string quotes
# name = 'Ada' 

# #Double quotes 
# greeting ="Hello"

# #Triple quotes (for multy-line strings)
# story ='''Once upon a time, 
# there was a coder named Ada.'''

# #String with numbers and symbols
# password = "p@sswords123"

# print(name, greeting, story,password)

#indexing

# word ="python might just be the mother of all the programing languages but you wouldnt know since she didnt breast feed you.Dont stop with that but rather advance into the future of ai and data science with out the no issue contribution. Stop givin excuses for your own failure but rayther take responsibility and overcome the problem you face"
# print(word[-23]) 
# print(word[23]) 




# #slicing 
# word = "python might just be the mother of all the programing languages but you wouldnt know since she didnt breast feed you.Dont stop with that but rather advance into the future of ai and data science with out the no issue contribution. Stop givin excuses for your own failure but rayther take responsibility and overcome the problem you face"
# print(word[0:6])
# print(word[0:])
# print(word[:6])
# print(word[::2])
# print(word[::-1])


# #Concatenation

# a = "Hello"
# b = "world"
# print(a + "" + b)

# #REPITITION
# word ="Hi!"
# print(word *3)

#MEMBERSHIP
# text = "Python programming"
# print("python" in text.lower())
# print ("java" not in text)

# #find()/ rfind()
# text = "Hello world"
# print(text.find("l"))
# print(text.rfind("l")) #this finds the last occurence of a letter

#index()/ rindex

# text ="Hello world i am a good world"
# print(text.index("ran"))#same as find( but throws an error code if not found)

# #this basically just checks if a specified word or letter starts or end a string
# filename = "data.csv"
# print(filename.startswith("data")) #true
# print(filename.startswith("qqat"))# false
# print(filename.endswith(".csv")) #true

# word = "\"e only person with a weird taste\""
# print(word.upper())
# print(word.lower())
# print(word.title())
# print(word.strip())
# print(word.replace())

# name = "Ada Balogun"
# print(name.upper())  

# sentence = "python is amazing"
# print(sentence.lower()) 

# text = "  Abuja    is the on      " #it only removes white spaces at the begining and end of the string ...it doesnt remove the ones inbetween words
# print(text.strip())

# #replace

# message = "i love java"
# print (message.replace("java","python"))

# #swapcase
# message = "i love java"
# print (message.swapcase())

# #lstrip
# text = "   Nigeria"
# print(text.lstrip()) 

# #rstrip
# text = "   Nigeria       "
# print(text.rstrip())

# #split
# fruits= "mango orange banana apple"
# print(fruits.split())
# list_fruits = fruits.split()
# print(list_fruits[2])


# rsplits
# text = "one,two.three,four"
# print(text.rsplit(",",1)) #this one basically splits from the right  and there is argument for specifying how many words is being splited 
# #note that it also has argument for secifying the symbol it sees to know where to split


# #splitline
# #splits a string into a list at each newline
# lines = "Line 1\nLine 2\nLine 3"
# print(lines.splitlines())

# #join()
# words = ["i","love","you"]
# print(" ".join(words)) 

#center() centers the string 
# text = "python"
# print(text.center(200," "))


# #ljust()
# #rjust()
# #the above 2 lefts and right align a  string simulteneously
# text = "Python is th efuture "
# print(text.rjust(100, " "))  

#zfill()
# num ="42"
# print(num.zfill(7)) #pads a numeric string on the left with zeros till it reach a given lenth 

# #isalpha()
# print("Lagos".isalpha())  # True
# print("Lagos123".isalpha())  # False

# #isdigit
# print("Lagos".isdigit())  # True
# print("123".isdigit())  # False

# #isalnum 
# print("python 3".isalnum())




word = "word of assertion"
w_ord= set(word)
print(w_ord)