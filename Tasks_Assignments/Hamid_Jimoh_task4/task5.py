#TASK5
#student score tracker
student_name = []
student_score =[]
user_input = input("please input the name of students: ").split(",")
student_name=user_input.copy()
print(student_name)
for x in student_name:
   student_score.append(float(input(f"what is {x} score: ")))
print(f"{student_name[0]}\t\t{student_score[0]}")
print(f"{student_name[1]}\t\t{student_score[1]}")
print(f"{student_name[2]}\t\t{student_score[2]}")