#name collectors 
#collect the names one by one
print("Hey guest, kindly input your full name ")
seminar_attendance = set()
for x in range(1,10000):
    user_input = input(f"Hey guest, kindly input your full name: ").lower()
    if user_input in seminar_attendance:
        print("input is registered")
    seminar_attendance.add(user_input)
    print(sorted(seminar_attendance))
    
