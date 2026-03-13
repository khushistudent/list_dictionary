# programed By : Khushi
# Roll No. 36
#List Assignment number :13
#13	Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)
list_age=[12,24,34,18]
under_newage=[]
above_newage=[]
for i in list_age:
 if i>=18:
     above_newage.append(i)
    
 else:
      under_newage.append(i)
print("minors (under 18) = ",under_newage) 
print("adults (18 and above) = ",above_newage)     
