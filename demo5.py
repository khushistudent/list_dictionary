# programed By : Khushi
# Roll No. 36
#List Assignment number : 5
#5	Create a list of 10 random integers. Use a for loop to print each number multiplied by 2.
import random
random_int=[]
for count in range(1,11):
  temp=random.randrange(1,100)
  random_int.append(temp)
print(random_int)
for i in range(len(random_int)):
   print(random_int[i]*2)