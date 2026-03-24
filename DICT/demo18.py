# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 18
#"Create a program to manage student marks using dictionary.

# Features

# Store student name and marks

# Display all students

# Search student

# Find topper

# Calculate class average"
student="Khushi","Nidhi","Shreya","Priya"
marks=98,56,78,90
a=dict(zip(student,marks))
print("Store student name and marks : ",a)
name=0
maximum=0
sum=0
for i in marks:
     sum+=i
#print(sum)
for key,value in a.items():
     if value>maximum:
          maximum=value
          name=key
print("Display all students ",a.keys())
print("topper : ",maximum,name)
search_name=input("enter name : ")
for key,value in a.items():
     if search_name==key:
          print("Search name  : ",key)
          break
     else:
          print("not Found in the dictionary")
          break
avg=0
avg=sum/len(a)
print("Calculate class average : ",avg)