import data
import utils

data.add_student("Hamid","AI Engineering")
data.add_student("Esther","AI Engineering")

#print formatted student records
for s in data.get_students():
    print(utils.format_student(s))