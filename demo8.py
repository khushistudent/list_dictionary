# programed By : Khushi
# Roll No. 36
#List Assignment number : 8
#8	Given a list of numbers 1-20, create a new list that contains only the even numbers.
Numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_number=[]
for i in Numbers:
    if i%2==0:
     even_number.append(i)
print(even_number)
