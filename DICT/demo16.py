# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 16
#Allow a user to input a name and a phone number via input() and store it in a dictionary until they type "exit".
Contact={}
while True:
    Name=input("Enter your name : ")
    if Name=="exit":
       break
    Phone_Number=int(input("Enter your phone number : "))
    Contact[Name]=Phone_Number
print("Contact = ",Contact)