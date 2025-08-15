print("WELCOME TO THE VOTERS REGISTRATION PORTAL 2025")
data_base = set()
i = 0
for i in range(50):
    user_input = input("Hello, kindly input your name: ")
    if user_input in data_base:
        print("Alert!! you have registered before: ")
    else:
        data_base.add(user_input)
        i = i+1
        print(data_base)