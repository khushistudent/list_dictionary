# programed By : Khushi
# Roll No. 36
#List Assignment number :15
#15	A week's temperatures are stored in a list. Find how many days were "Hot" (above 35°C)
temperatures=[35,45,55,46,23,36]
days=0
for i in temperatures:
    if i>35:
     days+=1
print(days,"days were Hot")
    
