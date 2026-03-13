# programed By : Khushi
# Roll No. 36
#List Assignment number :19
#19	"A teacher stored attendance of students in a list (1 = present, 0 = absent).
#Example: [1,1,0,1,0,1,1]
#
#
#Write a program to:
#
#Count total present
#
#Count total absent
#
#Print attendance percentage"
attendance=[1,1,0,1,0,1,1]
count_absent=0
count_present=0
for i in attendance:
    if i==1:
        count_present+=i
    else:
     count_absent+=1
attendance_percent=count_present/len(attendance)*100
print("attendance Percentage = ",attendance_percent)
print("Present = ",count_present)
print("Absent = ",count_absent)