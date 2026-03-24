# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 19
#"Create a simple phone book using a dictionary where name is the key and phone number is the value.
# Features
# Students should implement:
# Add new contact
# Display all contacts
# Search contact by name
# Delete a contact"
Simple_book={"Aman":9919456756,"Anuj":8976878676,"Sumit":8765456743}
print(Simple_book)
# Add new contact
Simple_book.update({"Amit":9076896507})
print("Display all  contact : ",Simple_book)
# Search contact by name
Search=input("enter name : ")
for key,value in Simple_book.items():
    if Search==key:
     print(key,value)
     break
else:
       print("not")
# Delete a contact
Simple_book.pop("Aman")
print(Simple_book)