#TASK1
"""the first part checks if num1 is equal to num2 and prints either True or False """

"""The second output checks if num1 is not equal to num2 and if it is not equal to  it gives True else if it is equal to num2 it prints False"""

"""this one checks if num1 is greater than num2  and if it is true it prints True but if num1 is less than it prints False"""
""" this checks if num1 is less than num2, if it is true then it prints True but if it is not true it prints out False """

#use cases 

"1. it can be used in speed limit detection to check if a car exceeds a specified speed "
"2. it can also be used in the school to automatically check if  a student pass or fails a course and should either repeat the course or promote "
"3. it can be used to check for punctuality in an office.where each worker clocks in and at the end ofg the month it displays how many time they came after the specified resumption time "

#code for checking for number 2 (if a student pass or fails )
"in the university of ibadan the pass mark is set for departments then faculty then the school "
"so in thius case we will be setting the school pass mark to 45  the department pas mark to 60 and faculty passs mark to 50"


university_pmark=50
physics=float(input("what is your score in physics: "))
math=float(input("what is your score in math: "))
chemistry=float(input("what is your score in chemistry: "))
average_score = (physics+math+chemistry)/3
#university requirement
uni1=print (f"Will the student carry over? {average_score==university_pmark}")
uni2= print (f"Will the student carry over? {average_score>university_pmark}")
print(f"Will the student promote?{uni1==True or uni2 == True}" )
# print(f"Will the student carry over?{uni1 == "False" and uni2 == "False"}" )



