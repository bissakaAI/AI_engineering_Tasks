database ={

}



for i in range (1,3):
    user_input={}
    courses=[]
    user_name= input(f"input name your name: ")
    user_age = int(input(f"input name your age: "))
    user_gender = input(f"input name your gender: ")
    num_of_courses = int(input("how many courses are you registring for"))
    for i in range(1,num_of_courses):
        user_courses = input(f"input name of course you are registring: ")
        courses.append(user_courses)
    user_input["course"]=courses
    user_input["Name"]=user_name
    user_input["Gender"]=user_gender
    user_input["age"]=user_age
    print(user_input)
    database_key =user_name
    database_value= user_input
    database[database_key] = database_value
    print(database)

for key,value in database.items():
    print(f"{key}:\t{value}\n")