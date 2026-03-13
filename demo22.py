# programed By : Khushi
# Roll No. 36
#List Assignment number :22
#22	"Marks of students are stored in a list.
#
#marks = [78, 35, 90, 40, 55]
#
#Write a program to:
#
#Print PASS if marks ≥ 40
#
#Print FAIL if marks < 40
#
#Count how many students passed"
marks = [78, 35, 90, 40, 55]
count=0
for i in marks:
    if i>=40:
        print(i," - Pass")
        count+=1
    else:
     print(i," - fail") 
print(count,"N0. of students passed")