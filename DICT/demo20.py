# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 20
#"Create Attendance System where 

# Faculty should:

# Add attendance for 5 students

# Count total present students

# Display absent students"
Attendence={"Mansi":"present","Arya":"absent","Kashish":"present","Shaivi":"absent","Ruchi":"present"}
count=0
for key,value in Attendence.items():
    if value=="present":
        count+=1
print("Total count of present setudent")
print("Count present students : ",count)
print("====================================")
print("display absent student")       
for key,value in Attendence.items():
    if value=="absent":
        print(key,value)
