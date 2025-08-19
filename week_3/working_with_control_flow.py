# age =20 
# if age >=18:
#     print("you are eligible to vote")

# wallet = 480
# price=500
# if wallet >= price:
#     print("purchase successful")
# else:
#     print("insufficient balance")


# score = 85 
# if score>= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")


# age = 19 
# citizen = False
# if age >= 18:
#     if citizen:
#         print("you can vote")
#     else:
#         print("you must be a citizen to vote")
# else:
#     print("too young to vote")


# #looooooooooooooooooooooopppppppppppppppppppppppp
# #iterates through each element in a LIST
# fruits =["apple","banana","orange"]
# for fruit in fruits:
#     print(f"I Like {fruit}")

# coordinates =(0.34654,-0.48585,0.57477)
# for point in coordinates:
#     print(f"Point: {point}")

# student ={"name":"tunde","age":16,"grade":"A"}
# for key,value in student.items():
#     print(f"{key}: {value}")


# word ="PYTHON"
# for char in word:
#     print(char)


# #while loopppppppppppp
# # Using while loop

# ## Documenting my thoughts##
# # Let the loop start with count = 1
# # Let it keep printing until count is greater than 5
# # Let the loop terminate when the condition is no longer true

# ## My code

# count=1
# while count <= 5:
#     print("Number:",count)
#     count +=1

# num = 1
# while num <= 10:
#     print(num,end=" ")
#     num +=1

# timer =10
# while timer >0:
#     print("Countdown",timer)
#     timer -=1


# # While with User Input
# ## Keep asking until the user enters a correct password.
# password = ""
# while password != "python123":
#     password =input("Enter the password: ")

# print("Access Granted!")

# while True:
#     name =input("Enter your name (type 'exit' to quit): ")
#     if name.lower()=="exit":
#         print("Goodbye!!")
#         break
#     print(f"Hello,{name}")

# for num in range(1, 10):
#     if num == 5:
#         break
#     print(num)

# for num in range(1, 10):
#     if num == 5:
#         continue
#     print(num)

# for num in range (1,6):
#     if num==3:
#         pass
#     else:
#         print(num)


# #lets try while true again
# while True:
#     print("\nMenu:")
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Exit")

#     choice = input ("choose an option")
#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("Goodbye")
#     elif choice == "3":
#         print("Exiting program...")
#         break
#     else:
#         print("Invalid choice. Try again.")


# while True:
#     age=input("Enter your age: ")
#     if age.isdigit():
#         print(f"your age is {age}")
#         break
#     else:
#         print("Invalid input. please enter a number.")


# #lets make a guess 
# secret = "python"
# while True:
#     guess = input ("Guess the secret word: ")
#     if guess.lower() == secret:
#         print("correct! you guessed the word ")
#         break
#     else:
#         print("Wromg! Try again.")

# balance = 10000000000
# while True :
#     print("\nATM Menu:")
#     print("1. Check Balance")
#     print("2. Withdraw")
#     print("3. Exit")

#     choice = input("Enter choice: ")
#     if choice == "1":
#         print(f"your balance is: {balance}")
#     elif choice == "2":
#         amount = int(input("Enter withdrawal amount: "))
#         if amount <= balance:
#             balance-=amount
#             print(f"withdrawal successful.New balance: {balance}")
#         else:
#             print("insufficient funds")
#     elif choice == "3":
#         print("Thank you for using our ATM. Goodbye!")
#         break
#     else:
#         print ("invalid option. try again")