print("WELCOME TO THE VOTERS REGISTRATION PORTAL 2025")
data_base = set()
for i in range(50):
    user_input = input("Hello, kindly input your name: ").lower()
    if user_input in data_base:
        print("Alert!! you have registered before: ")
    else:
        data_base.add(user_input)
        num_unique_voters=len(data_base)
        print(f"Total number of unique voters is \t{num_unique_voters}")