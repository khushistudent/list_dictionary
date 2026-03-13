# programed By : Khushi
# Roll No. 36
#List Assignment number :14
#14	Store prices of 5 items in a list. Calculate the total bill and the average price per item.
item_prices=[260,500,700,370,820]
#print(item_prices)
sum=0
average=0
for i in item_prices:
    sum+=i
print("Total bill = ",sum)
average=sum/len(item_prices)
print("Average price per item = ",average)
