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


utme_score =input("What is your score in UTME (JAMB)")
input("do you have minimum of C  in 5 relevant subjects in your O'Level including Mathematics and English ")
subjects = input("list the 5 courses seperated by commas: ").split(",")
first_sub = input(f"what is your grade in {subjects[0]}: ")
second_sub= input(f"what is your grade in {subjects[1]}: ")
third_sub=input(f"what is your grade in {subjects[2]}: ")
forth_sub=input(f"what is your grade in {subjects[3]}: ")
fifth_sub=input(f"what is your grade in {subjects[4]}: ")

#this part is for those that have passed the set pass mark for utme of 200
#congratulate them for making it this far and tell them to do their best in the post UTME
"CONGRATULATIONS, YOU HAVE PASSED THE FIRST ROUND OF THE ADMISSION PROCESS".center(100)
"This is an incredible one.You came out ontop despite the hudles" 
"you deserve to be celebrated".center(80)
print("Welcome to the next stage of the admission process")