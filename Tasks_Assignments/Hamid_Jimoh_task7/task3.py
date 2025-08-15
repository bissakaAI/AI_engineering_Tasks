import random
#create a turple and store the days of the week
days_of_the_week =("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
days_picked =[]

#ask user for there activities and the day the activity will take place and store it in a variable
for i in range(3):
    rand_selection = random.choice(days_of_the_week)
    if rand_selection not in  days_picked:
        days_picked.append(rand_selection)
        activity_ =input(f"please specify the activities for {rand_selection} ): ")