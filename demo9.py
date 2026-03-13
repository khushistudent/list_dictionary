# programed By : Khushi
# Roll No. 36
#List Assignment number : 9
#9	Write a program that takes a list of names and a "search_name" from the user. Print the index where the name is found, or "Not Found."
List_name=["a","b","c","d"]
search_name=input("enter name : ")
if search_name in List_name:
  print("Found",List_name.index(search_name))
else:
    print("not")