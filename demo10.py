# programed By : Khushi
# Roll No. 36
#List Assignment number :10
#10	Given a list of 10 student marks, count how many students scored above 40.
Student_marks=[45,89,76,45,34,23,56,78,89,30,90] #8
count=0
for i in range(len(Student_marks)):
    if Student_marks[i]>40:
     count+=1
print("Total Student scored above 40 = ",count)
     
