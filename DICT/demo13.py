# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 13
#Given a dictionary of items and prices, find and print the name of the cheapest item.
prices={
    "Book":50,
    "Pen":40,
    "Notebook":45
}
print(min(prices,key=prices.get),end=" ")
print(min(prices.values()))
