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
input("do you have distinctions in 5 relevant subject in WAEC/WASSCE including MATH and ENGLISH ")
subjects = input("list the 5 courses seperated by commas: ").split(",")
first_sub = input(f"what is your grade in{subjects[0]}")
second_sub= input(f"what is your grade in{subjects[1]}")
third_sub=input(f"what is your grade in{subjects[2]}")
forth_sub=input(f"what is your grade in{subjects[3]}")
fifth_sub=input(f"what is your grade in{subjects[4]}")

#Eligibility check
"""this checks using logical operators if the user meets certain creiteria and uses it to determine if they are eligible or not """
eligibility = ((first_sub == "a") or (first_sub =="b")) and ((second_sub == "a") or (second_sub =="b")) and ((third_sub == "a") or (third_sub =="b")) and ((forth_sub == "a") or (forth_sub =="b")) and ((fifth_sub == "a") or (fifth_sub =="b")) and (citenzenship=="nigeria") and(sch_status == "no") and (enrolment == "yes") and (score>=70)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")




