import json
import csv
from pathlib import Path
workspace=Path("workspace_files")
workspace.mkdir(exist_ok =True) 
file_path = workspace/"notes.txt"


f = open(file_path,"w",encoding="utf-8")
f.write("This is the journey of my AI career")
f.close

# #(B) Safe-create using 'x' (uncomment to try once)
# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()

f = open(file_path,"w",encoding="utf-8")
f.write("check items below \n")
f.write("Apple \n")
f.write("clocking system \n")
f.write("banana \n")
f.close()


f=open(file_path,"a", encoding="utf-8")
f.write("This is the next line in this file\n")
f.write("Maggi \n")
f.close()

f = open(file_path,"r",encoding="utf-8")
content =f.read()
print(content)
f.close


#Read line-by-line
f = open(file_path,"r",encoding="utf-8")
print("firstline:", f.readline().rstrip())
print("second line:",f.readline().rstrip())
f.close()

f= open(file_path,"r",encoding="utf-8")
list = f.readlines()
f.close()
print("lines list:",[line.rstrip() for line in list])


f = open(file_path, "r", encoding="utf-8")
for line in f:
    print("-->", line.rstrip())
f.close()

#using the open() as f :best practice 
#this automatically closes the file even if an error happens .
#write safely
with open(file_path,"w", encoding= "utf-8") as f:
    f.write("My to-do list\n")
    f.write("-Revise python file handling\n")
    f.write("-Practice error handling within a function\n")
    f.write("-Practice JSON & CSV\n")


with open(file_path,"a", encoding= "utf-8") as f:
    f.write("--> Build a small project\n")


try:
    with open(workspace /"missing_file.txt", "r") as f:
        content = f.read()
        print("file content: ", content)
except FileNotFoundError:
    print("oops! That file doesnt exist yet")
    print("lets create it first ")

    #now create the file
    with open(workspace/"missing_file.txt","w",)as f:
        f.write("Now i exist!")
    print("File created successfully")




#check if our file exists 
if file_path.exists():
    print(f"Found the file: {file_path.name}")

    #Get some information ABOUT THE FILE 
    file_size = file_path.stat().st_size
    print(f"File size: {file_size} bytes")

    #Read and show the content 
    with open(file_path, "r", encoding ="utf-8") as f:
        content = f.read()
        print(f"content preview: {content[:50]}...")
else: 
    print(f"file {file_path.name} doesn't exist")
    print("you might want to create it first!")

#if notes.txt exists 





#create some student data (like a mini database )
student_data = {
    "name": "Oyindamola",
     "age": 16,
     "courses": ["Python","Data Science","Web Development  "],
     "grades": {"Python":"A","Data Science": "B+", "Web Development": "A-"},
     "is_graduated": False
}


#save the data to a json file 
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding= "utf-8") as f:
    json.dump(student_data, f, indent= 2)
print("Student data saved to JSON file!")

#Now read it back 
with open(json_file, "r", encoding= "utf-8") as f :
    loaded_data = json.load(f)

print("\n Data read from JSON file ")
print(f"Student name: {loaded_data["name"]}")
print(f"Age: {loaded_data["age"]}")
print(f"Courses: {",".join(loaded_data["courses"])}")
print(f"Python grade: {loaded_data['grades']['Python']}")




workspace = Path("workspace_files")
csv_file = workspace/"students.csv"

#create sample student data 
students = [
    ["Name", "Age", "Course", "Grade"],  # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "JavaScript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
]

#wrrite data to a csv file
with open(csv_file,"w",newline="", encoding= "utf-8") as f :
    writer = csv.writer(f)
    writer.writerows(students) #write all rows at once m

print("Student data written to csv file")

# Read the CSV file back
print("\nReading CSV file:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row_number,row in enumerate(reader):
        if row_number== 0:
            print(f"Headers: {'|'.join(row)}")
            print("-"*40)
        else: #Data rows
            name,age, course,grade =row
            print(f"{name} ({age} years) - {course}: {grade}")



#working with multiple files at once 
from pathlib import Path
workspace= Path("workspace_files")
input_file = workspace/"original.txt"
output_file = workspace/ "processed.txt"

#create an input file with some text
sample_text = """hello world
python programming
file handling
file handling tutorial
learning is fun"""
with open(input_file,"w", encoding="utf-8") as f:
    f.write(sample_text)
print("created input file")

# with open(output_file, "w", encoding="utf-8") as f:
#     print("output ok")

#process the file: read from input, write processes version to output 
with open(input_file,"r",encoding="utf-8") as infile,\
     open(output_file,"w", encoding="utf-8") as outfile:
    
    line_number = 1 
    for line in infile:
        #Process eachline:make it uppercase and add line numbers 
        processed_line =f"line {line_number}: {line.strip().upper()}\n"
        outfile.write(processed_line)
        line_number +=1

print("File processing complete!")

# Show the results
print("\nOriginal file:")
with open(input_file, "r", encoding="utf-8") as f:
    print(f.read())

print("\nProcessed file:")
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())



#Moving around inside a file 

workspace = Path("workspace_files")
file_path = workspace / "story.txt"

# Create a sample story file
story = """Once upon a time, there was a lady  who was very curious and inquisitive, 
she just want to know how things work behind the scene. 
Eventually she had an opportunity to hopp into the world of programming for the first time.
She started with python, now she codes in Python every day.
One day, she discovered file handling.
It opened up a whole new world of possibilities!
The end."""

with open(file_path,"w", encoding="utf-8") as f:
    f.write(story)
print("Created a story file!")

# Now let's explore moving around in the file
with open(file_path, "r", encoding="utf-8") as f:
    print("\nFile positioning demo:")

    # Read first 20 characters
    first_part = f.read(20)
    print(f"First 20 characters: '{first_part}'")

    # Check where we are now
    current_position = f.tell()
    print(f"Current position in file: {current_position}")

    # Jump to the beginning
    f.seek(0)
    print(f"After seeking to beginning: position {f.tell()}")
    f.seek(50)
    rest_of_line = f.readline()
    print(f"Reading from position 50: '{rest_of_line.strip()}'")

    # Go back to beginning and read the first line
    f.seek(0)
    first_line = f.readline()
    print(f"First line: '{first_line.strip()}'")