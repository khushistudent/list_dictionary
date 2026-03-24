# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 15
#Given a dictionary of employees and their salaries, increase every salary by 10% and update the dictionary
employess={"emp1":1000,"emp2":2000,"emp3":3000}
print(employess)
print("===============================================================")
for name ,salary in employess.items():
    employess[name]=employess[name]+salary*10//100
print("update the dictionary : ",employess)