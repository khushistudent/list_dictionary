# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 21
#"A small shop sells 5 items. You need to create a program that acts as a POS (Point of Sale) system.
# Tasks:
# The Database: Create a dictionary called menu where keys are item names (e.g., ""Samosa"", ""Tea"", ""Coffee"") and values are their prices.
# The Shopping List: Create an empty list called cart.
# The Input Loop: Use a while loop to ask the user to type an item name to add to their cart. Type ""done"" to stop.
# Validation: If the user types an item not in the menu, print ""Item not available.""
# The Bill: After ""done"" is typed, loop through the cart list. For each item, look up its price in the menu dictionary and calculate the total sum.
# Final Output: Print a ""Receipt"" showing the items bought and the final total price."
menu={"Samosa":20,"Tea":10,"Coffee":15}
cart=[] #empty list
total=0
while True:
    user=input(" enter item : ")
    if user=="done":
      print(cart)
      break
    elif user in menu:
            cart.append(user)
            #print(cart)
    else:
        print("item is not available")
for item in cart:
     value=menu[item]
     total+=value
print("Recipt ")
for key,value in menu.items():
     if key in cart:
          print(key,value)
print("Final Total Price : ",total)    
