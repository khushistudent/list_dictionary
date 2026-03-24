# programed By : Khushi
# Roll No. 36
#Dictionary Assignment number : 17
#Given a dictionary with some duplicate values, find a way to print all the unique values.
values={"A":90,"b":100,"b":90,"A":70,"C":78,"C":89}
print(dict(set(values.items())))