# #comparison operators

# a= 10
# b=20
# print(a==b)
# print(a!= b)
# print(a>b)
# print(a<b)
# print(a>=10)
# print(a<=25)

# #use case example -student exam results
# score =75 
# print(score >= 50)
# print(score <50)
# print(score ==100)

# #assignment Operators 
# #they are used to assign values to variables.they can also combine an opertation with assignment,so instead of writing x = x +5 we can write x +=5
# x = 10
# print("Initial value:", x)
# x += 5
# print("After x += 5:", x)
# x -= 2
# print("After x -= 2:", x)
# x *= 3
# print("After x *= 3:", x)
# x /= 4
# print("After x /= 4:", x)
# x %= 3
# print("After x %= 3:", x)
# x = 4
# x **= 2
# print("After x **= 2:", x)
# x //= 3
# print("After x //= 3:", x)

# #USE CASE EXAMPLE
# #define variable
# balance = 1000
# deposit =200 
# withdraw =150

# balance +=deposit 
# balance -= withdraw
# print (balance)


# #LOGICAL OPERATORS 
# #they are used to combine conditional statements
# x=10
# y=20
# #and operator
# print(x>5 and y>15)
# #or operator 
# print(x<5 or y >15)
# #not operator
# print(not(x==10))

# #use case example1 -scholarship eligibilitty 
# #define variables 
# age = 17
# score =85 
# #must be younger than 118 and score above 80
# eligible =(age<18) and (score>80)
# print(eligible)

#use CASE EXAMPLE2: EVENT ACCESS 
age = 22 
has_ticket= False 
can_enter = (age>=18) and (has_ticket or age<25)
print("Acccess Granted:", can_enter)