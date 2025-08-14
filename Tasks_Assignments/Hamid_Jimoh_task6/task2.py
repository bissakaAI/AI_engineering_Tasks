#name collectors 
#collect the names one by one
print("Hey guest, kindly input your full name ")
i= tuple(range(1,100000))
seminar_attendance = set()
seminar_attendance2 =set()
for x in i:
    user_input = input(f"Hey guest, kindly input your full name: ")
    seminar_attendance.add(user_input)
    names= list(seminar_attendance)
    print(names)
    sorted_names = names.sort()