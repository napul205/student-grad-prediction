jobs=[
[1,1,20],
[2,1,21],
[3,2,20],
[4,3,30]
]
schedulejobs=[]
for i in range(len(jobs)):
    schedulejobs.append(0)
def schedule():
    maxprofit=0
    for i in range(len(jobs)):
        for j in range(jobs[i][1]-1,-1,-1):
            if schedulejobs[j]==0:
                schedulejobs[j]=jobs[i][0]
                maxprofit+=jobs[i][2]
                break

    return maxprofit
jobs=sorted(jobs, key=lambda l:l[2], reverse=True)
profit=schedule()
print(profit)
for i in range(len(jobs)):
    if schedulejobs[i]!=0:
        print("job",schedulejobs[i])
