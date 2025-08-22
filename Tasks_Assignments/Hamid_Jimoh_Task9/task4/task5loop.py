#TASK5
#student score tracker
student_name = []
student_score =[]
for name in range(1,4):
   user_input = input(f"please input the name of student {name}: ")
   student_name.append(user_input)
for x in student_name:
   student_score.append(float(input(f"what is {x} score: ")))
count = 0
for x in range(0,3):
   print(f"{student_name[x]}\t\t{student_score[x]}")
