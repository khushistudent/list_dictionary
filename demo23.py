# programed By : Khushi
# Roll No. 36
#List Assignment number :23
#23	"A cricket player scored runs in 6 matches.
#Example: [45, 60, 10, 80, 55, 90]
#
#Write a program to:
#
#Find total runs
#
#Find highest score
#
#Count how many matches player scored more than 50 runs"
scored=[45, 60, 10, 80, 55, 98]
sum=0
count=0
for i in scored:
   sum+=i
   if i>50:
      count+=1
print("total runs = ", sum)
scored.sort()
print(scored)
print("Highest score =",max(scored))
print(count,"scored more than 50 runs")