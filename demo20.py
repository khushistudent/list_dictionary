# programed By : Khushi
# Roll No. 36
#List Assignment number :20
#20	"A cricket player scored runs in 6 matches.
#Example: [45, 60, 10, 80, 55, 90]
#Find:
#
#Total runs
#
#Highest score"
scored_runs=[45, 68, 20, 82, 55, 90]
sum=0
for i in scored_runs:
    sum+=i
scored_runs.sort()
#print(scored_runs)
print("Highest score = ",scored_runs[-1])
print("Total runs = ",sum)
