# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 10
# 10 Given a dictionary of student names and their marks, print only the names of students who scored above 75
Student_marks={"Khushi":57,"Arya":98,"Kashish":88,"Ruchi":67}
for key,value in Student_marks.items():
     if value>75:
          print(key,"=",value)
