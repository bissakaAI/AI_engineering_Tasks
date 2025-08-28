from pathlib import Path
# import os 

# print("file path: ",os.getcwd())

# absolute_path = r"c:\Users\ncc67888"
# #relative path
# relative_path = "my_path.py"
# print("absolute path : ",absolute_path)
# print("relqtive path: ", relative_path)

# folder = r"C:/Users/Chris/Desktop"
# filename= "my_path.py"

# path = os.path.join(folder,filename)
# print("Full path:", path)
# #This way, python handles slashes (/ vs \) automatically.

# path = "mypath.py"
# if os.path.exists(path):
#     print("yes, the file exists")

# else:
#     print("file not found")


#using pathlib (modern way)
#current working directory


print("current directory:",Path.cwd())

#create  a path object 
file = Path("mypath.py")
#check if it exists
print("File exists: ", file.exists())

#combine paths
folder = Path("C:/Users/Chris/Desktop")
full_path = folder/"myfile"
print("Full path:", full_path)

#get parent folder of current file
print("parent folder: ",Path.cwd().parent)
#list all files ina a directory
for file in Path.cwd().iterdir():
    print(file)