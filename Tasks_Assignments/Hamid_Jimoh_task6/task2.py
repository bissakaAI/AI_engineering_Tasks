#name collectors 
#collect the names one by one
print("Hey guest, kindly input your full name ")
i= tuple(range(1,100000))
seminar_attendance = set()
for x in i:
    user_input = input(f"Hey guest, kindly input your full name: ").lower()
    if user_input in seminar_attendance:
        print("input is registered")
    seminar_attendance.add(user_input)
    print(sorted(seminar_attendance))
    
