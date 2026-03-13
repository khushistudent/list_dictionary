# programed By : Khushi
# Roll No. 36
#List Assignment number :16
#16	Store marks of 5 students in a list and calculate the average marks.
marks=[98,80,87,65,70]
avg=0
sum=0
for i in marks:
    sum+=i
#print(sum)
avg=sum/len(marks)
print("Average of marks = ",avg)