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
compulsory=[]
resit = []
total_score = 0

try:
    no_compulsory=int(input("How many compulsory courses did you offer for this semester: "))
    for i in range(1,no_compulsory+1):
        compulsory1= input(f" input name of number {i} compulsory course: ")
        compulsory.append(compulsory1)
        score=float(input(f"what is your score in {compulsory1}: "))
        if score < 45 :
            resit1 = print (f"You have to resit {compulsory1}")
            resit.append(resit1)
        total_score += score
    average_score = total_score/no_compulsory
    #university requirement
    uni1= (average_score==university_pmark) or (average_score>university_pmark) and (len(resit)== 0)
    if uni1 == True:
        print("congratulations, You promoted to the next class")
    elif len(resit)>0:
        print(f"You have {len(resit)} resit(s) ")
    else:
        print("Advised to withdraw")
except ValueError:
    print("There is something wrong with your input")
except TypeError as e:
    print("Type erroooooooooorrrrr", e)
except Exception as e:
    print("Error:",e)




