#TASK6
#ATTENDANCE TRACKER
days_of_the_week =("Monday","Tuesday","wednesday","thursday","friday","saturday","sunday")
months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
user_input_name = input ("input your full name : ")
user_input_gender = input ("Are ypou a male or female: ")
user_input_track = input ("what course track did you enroll for: ")
user_input_month = int(input ("input Month using the format e.gmay is 05: "))
user_input_day = int(input ("current day number e.g (1-7): "))
correct_month = months_of_year[user_input_month -1]
correct_day=days_of_the_week[user_input_day -1]
print(f"Name:\t{user_input_name}\nGender:\t{user_input_gender}\nTrack:\t{user_input_track}\nmonth:\t{correct_month}\nDay:\t{correct_day}")
