from pathlib import Path
#to do list
""" Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user input

 """

# #trying to store the list in a txtfile instead of a list 
# path = Path.cwd()
# with open(path,"x",encoding="utf-8") as f:
#     f.writelines(to_do)
    
#list to store the tasks 
to_do= []
path = Path.cwd()/"txt_file.txt"

#view to do list 
def  view_todo():
    if to_do != [] :
        print("==========To do List==========")
        for x, y in enumerate(to_do):
            print(f"{x+1}.\t{y}")
            print("----------------")
    
    else:
        print("\nthere is currently nothing in your to do list\n")
#Add task
def add_task():
    task = input("What task do you want to add to your to_do list? ")
    #trying to store the list in a txtfile instead of a list 
    f = open(path,"a",encoding="utf-8")
    f.writelines(f"{task}\n")
    print("Your task has been added to to_do_list ✅")
    



#now when a user does a task on the to_do list you want to remove it from the to_do list 
def perform_task():
    perform = input("Which task do you want to perform from your to_do list?: ")
    if perform in to_do:
        print("Good luck with the task")
    status =input("Are you done with task? (yes/no)").lower()
    if status == "yes":
        print("weldone")
        to_do.remove(status)
    elif status == "no":
        print("you can do it, keep pushing")
    else:
        print("invalid input")


#Removing task
def remove_task():
    task= input("please input the task you want to remove")
    if task in to_do:
        to_do.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")

while True:
    try:
        print("What do you want to do :\n1. Add task\n2. View to do list \n3. Exit\n4.Remove task")
        user_choice = input("Please pick any choice from 1 - 4 ")

        if user_choice == '1':
            add_task()
        # elif user_choice == '2':
        #     view_todo()
        # elif user_choice == '3':
        #     print("exiting app....")
        #     break
        # elif user_choice == '4':
        #     remove_task()
        # else:
        #     print("Invalid choice! Please select a valid option.")

    except Exception as e :
        print(e)