# programed By : Khushi
# Roll No. 36
#List Assignment number :11
#11	Take a list like [-5, 3, -2, 8]. Create a new list where all negative numbers are converted to positive.
list=[-5,3,-2,8]
newlist=[]
for i in list:
    if i>0:
      newlist.append(i)
    else:
        i*=-1
        newlist.append(i)
print(newlist)