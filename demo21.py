# programed By : Khushi
# Roll No. 36
#List Assignment number :21
#21	"A teacher stores marks of students in a list
#
#marks = [78, 65, 89, 90, 56]
#
#Write a program to:
#
#Print all marks
#
#Find total marks
#
#Find average marks
#
#Find highest marks
#
#Find lowest marks"
marks = [78, 65, 89, 90, 56]
print("all marks = ",marks)
sum=0
avg=0
for i in marks:
    sum+=i
print("Total marks = ",sum)
avg=sum/len(marks)
print("average marks = ",avg)
marks.sort()
#print(marks)
print("highest marks = ",marks[-1])
print("lowest marks = ",marks[0])