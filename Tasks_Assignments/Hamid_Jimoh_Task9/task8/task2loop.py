#collect user details and scores
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))
"""The code above asks user for there name,age and test score and stores it in the variables name,age and scores respectively """



#take an input statement to ask them there country of citizenship,enrollment,scholarshoip status and academic qualificATION
citenzenship = input("please enter your country of citizenship: ").lower()
enrolment =input("are you curently enrolled in a full time undergraduate program at an accredited university in nigeria?: ").lower()
sch_status=input("are you currently a beneficiary of any other scholarship by any oil and gas industry? ").lower()
#ANOTHER INPUT ASKING THEM FOR THE NAMES OF S5 subjects for there o level and asking fif they have A or B
o_level_qualification = input("do you have distinctions in 5 relevant subject in WAEC/WASSCE including MATH and ENGLISH (yes/no) ")
subjects =[]
grades=[]
status =[]
if o_level_qualification == "yes":
    for i in range(1,6):
        subject = input(f"Input the subject {i}: ")
        subjects.append(subject)
        grade = input(f"what is your grade in {subject}: ").lower()
        grades.append(grade)

print(grades)
#Eligibility check
"""this checks using logical operators if the user meets certain creiteria and uses it to determine if they are eligible or not """
eligibility1 =  (citenzenship=="nigeria") and(sch_status == "no") and (enrolment == "yes") and (score>=70)

for x in grades:
        if  x == "a" or x == "b":
            status.append(True)

for x in status:
    if x == False:
        eligibility2 =False
        break
    else:
         eligibility2= True
        
eligibility = (eligibility1 == True ) and (eligibility2 == True)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


