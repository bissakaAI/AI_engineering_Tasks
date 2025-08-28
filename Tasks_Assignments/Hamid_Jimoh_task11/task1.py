from pathlib import Path
import csv
#Take the name  and phone number and track and age 
#INPUT
dictionary={}
def participant_details():
    Participant_name = input("Good day Participant.What is your name")
    if Participant_name == "":
        print("You have to input your name")
    else:
        dictionary["Name"]= Participant_name
    try:
        Age = int(input("Input your Age in years"))
        if Age == "":
            print("You have to input your Age")
        else:
            dictionary["Age"]=Age
    except  ValueError:
        print("Error: You have to input a Number")
    except Exception as e:
        print (e)

    Track = input("Which Track are you enrolled in")
    dictionary["Track "]=Track

    phone_number = int(input("Please input your phone number "))

    if (len(str(phone_number))+1) <11:
        print("Invalid input!! Phone number needs to be 11 digits")
    elif (len(str(phone_number))+1) >11:
        print("Invalid input!! Phone number needs to be 11 digits\n You have inputed more than 11 digits")
    else:
        dictionary["Phone Number"]=phone_number
    print("Thank you for Inputing your details. Your data has been saved ")
    print(dictionary)
participant_details()
curren_directory1 =Path.cwd()
curren_directory = curren_directory1/"Tasks_Assignments/Hamid_Jimoh_task11"
file_name = curren_directory/Path("csvfolder")
file_name.mkdir(exist_ok=True)
csv_file = file_name/"task1.csv"

#to append the details of input to contack_details but as a dictionary
# dictionary = {"Name: ":name, "Age": Age, "Phone Number": phone_number, "Track ":Track}

contact_detail = [    ]
contact_details = [  ['Name','Age','Track' ,'Phone Number'],  ]

for key,value in dictionary.items():
    contact_detail.append(value)

contact_details.append(contact_detail)
    


# #CREATING FILE
# print(contact_details)
# with open(csv_file,"w",newline="", encoding="utf-8") as f:
#      writer = csv.writer(f)
#      writer.writerows(contact_details)

with open(csv_file, "r", newline="" ,encoding="utf-8") as f:
    writer = csv.reader(f)
    for row_num, row in enumerate(writer):
        if row_num== 0:
            print(f"Headers: {'|'.join(row)}")
            print("-"*40)
        else: #Data rows
            name,age,Track,Phone_number =row
            print(f"{name} ({age} years) - {Track} --- {Phone_number}")

