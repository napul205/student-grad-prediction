def schedule(jobs):
    schedulejobs=[]
    for i in range(len(jobs)):
        schedulejobs.append(0)
    maxprofit=0
    for i in range(len(jobs)):
        for j in range(jobs[i][1]-1,-1,-1):
            if schedulejobs[j]==0:
                schedulejobs[j]=jobs[i][0]
                maxprofit+=jobs[i][2]
                break
    print(maxprofit)
    for i in range(len(arr)):
        if schedulejobs[i] != 0:
            print("job", schedulejobs[i])

if __name__ == '__main__':
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print("Following is maximum profit sequence of jobs")

    schedule(arr)


