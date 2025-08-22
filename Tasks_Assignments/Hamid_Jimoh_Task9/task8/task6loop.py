#minimum age for admission is 16 2025/26 replacing 18 from 2025
#University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening
#The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 
"""Breakdown of the Admission Process:
1. UTME:
Candidates must score 200 or above in the UTME and choose UNILAG as their first choice. 
2. O'Level Requirements:
Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
3. Post-UTME:
Eligible candidates participate in the university's online Post-UTME screening. 
4. Departmental Cut-off Marks:
After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
(This can range from 200 to 320). 
5. Final Admission:
Candidates who meet the departmental cut-off marks are offered admission. 

- Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.utme_score"""

name = input("What is your full name: ").title()
Age = int(input("How old are you: "))
utme_score =float(input("What is your score in UTME (JAMB)"))
subjects = []
grades = []
correct_answer = []
utme_admis_status = 0

o_level_qualification=input("do you have minimum of C  in 5 relevant subjects in your O'Level including Mathematics and English ")
if o_level_qualification == "yes":
    for i in range(1,2):
        subject = input(f"Input the subject {i}: ")
        subjects.append(subject)
        grade = input(f"what is your grade in {subject}: ").lower()
        grades.append(grade)
print (grades)
for x in grades:

    if x != "a" and x != "b" and x != "c":
         grade_eligibility = False
         break
    else:
      grade_eligibility =True

if grade_eligibility == True and Age >= 16  and utme_score >= 200 :
    utme_admis_status = True
    #this part is for those that have passed the set pass mark for utme of 200
    #congratulate them for making it this far and tell them to do their best in the post UTME
    print("CONGRATULATIONS, YOU HAVE PASSED THE FIRST ROUND OF THE ADMISSION PROCESS".center(100))
    print("This is an incredible one.You came out ontop despite the hudles and you deserve to be celebrated")
    print("Welcome to the next stage of the admission process")
    
else:
    print("Dear Candidate you do not meet the required minimum qualification set by JAMB, kindly review the requirements and try again during the next intake")

#POST UTME 
if utme_admis_status == True:   
    university_choice =input ("Is your University first choice UNILAG? (yes/no): ").lower()
    if university_choice == "yes" :
        #The post utme questions
        print("Welcome to the online post utme Examination")
        exam_question= input("what is the first planet in the solar system?").title()
        if exam_question == "Mercury":
            correct_answer.append("correct")
        else:
            correct_answer.append("wrong")

#when you are done with exam i want your total score to show 
#count the number of correct in the list 
if utme_admis_status == True:
    count =0
    for x in correct_answer:
        if x == "correct":
            count += 1
    total_score = count/1 * 50    + (utme_score/8) 
    print (total_score)
