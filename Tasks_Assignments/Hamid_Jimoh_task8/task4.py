student= {}
Name= input("please input your name: ")
Age =float(input("please input your Age: "))
student.update({"Name:":Name,"Age": Age})
scores =[70,80,90]
student["Scores"] =scores
Avg_score = ((scores[0] + scores[1] + scores[2])/3)
passed = Avg_score>=50
teenager = (Age>=13) and (Age <=19)

print(f"Student Record:\t{student}\nName:\t{Name}\nPassed:\t{passed}\nTeenager:\t{teenager}")