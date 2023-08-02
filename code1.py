node=6
inf=999
cost=[
[0,50,45,10,inf,inf],
[inf,0,10,15,inf,inf],
[inf,inf,0,inf,30,inf],
[20,inf,inf,0,15,inf],
[inf,20,35,inf,0,inf],
[inf,inf,inf,inf,3,0]
]

def display(mat):
    for i in range(node):
        for j in range(node):
            print(i+1,"->",j+1,"=",mat[i][j])


def floydwar():
    for i in range(node):
        for j in range(node):
            for k in range(node):
                if cost[j][k]>cost[j][i]+cost[i][k]:
                    cost[j][k] = cost[j][i] + cost[i][k]
display(cost)
floydwar()
print("After new :")
display(cost)



