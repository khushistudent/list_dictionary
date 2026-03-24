# programed By : Khushi
#Dictionary Assignment number : 14
# Roll No. 36
#Create a dictionary inventory = {'Pens': 10, 'Erasers': 5}. Ask the user which item they bought and decrease that item's count by 1
inventory = {'Pens': 10, 'Erasers': 5,'Book':55,'Notebook':30}
ask=input("enter item name :")

#if ask in inventory:
#    inventory[ask]=inventory[ask]-1
#    print("Updated Dict : ",inventory)
#else:
#    print("not found")
for key,value in inventory.items():
    if ask==key:
     inventory[key]=value-1
print("Update Dict :",inventory)