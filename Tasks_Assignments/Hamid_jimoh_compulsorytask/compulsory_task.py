#INPUT SECTION
#i first need to collect student details 

student_name =input("what is your name: ").title() #in tittle case
student_age = int(input("How old are you as at today: ")) #age has to be integer
student_gender = input("Are you a male or female: ").lower() 

#collect extra information about the student
collect_hobbies = input("what are your hobbies? kindly seperate each hobby with a comma: ").split(",")

#ask for guardians information name,phone number and address
guardian_name =input("what is your guardians name: ").title() #in tittle case
guardian_address =input("input guardians address: ")
guardian_gender =input("what is your guardians gender?: ")
relationship_with_guardian= input("what is your relationship with guardian: ")
guardian_phone =input("kindly input guardians phone number: ")

scores = set()
Hobbies = set() # has to be a set since duplicate is not allowed

#since output is a list i need a code to pick each one and add it into the set hobbies
for hobby in collect_hobbies:
    Hobbies.add(hobby)


# i want to first create a fixed set of subjects ,lets start with 3 
#which means i need a tuple sice it is fixed 
list_of_subject = ("Physics","mathematics","chemistry")

#aloop that asks for the scores in each subject one after the other and adds it to and empty list of scores 
for subjects in list_of_subject:
    score= float(input(f"what is your score in {subjects}: "))
    scores.add(score)
#calculate the average score
average_score = sum(scores)/len(scores)

#create a dictionary to store each students profile
student_data ={"Student name: ": student_name,
               "Age": student_age,
               "gender": student_gender,
               "hobbies": list(Hobbies)
               }
guardian_data = {
    "Guardian name": guardian_name,
    "Relationship with guardian": relationship_with_guardian,
    "guardian address": guardian_address,
    "Gender" :guardian_gender,
    "Number": guardian_phone
}

course_details = {
    list_of_subject:scores for list_of_subject,scores in zip(list_of_subject,scores)
}
database_per_student = {"student_data":student_data,
                        "guardian_data":guardian_data,
                        "course_details":course_details }

database={student_name:database_per_student}
course_details["Average_score"]=average_score

#OUTPUT SECTION
print("\n\t \t === STUDENT PROFILE ===")
print(f"You have {len(Hobbies)} hobbies")
print(Hobbies)
print(f"The average score of the 3 subjects is: {average_score}")

print (database)

