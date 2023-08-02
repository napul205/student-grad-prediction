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
    for i in range (int(node)):
        for j in range(int(node)):
            print(i+1,"->",j+1,"=",mat[i][j])
            print()


def dijkstra(source):
    dest=cost[source]
    for i in range(node):
        for j in range(node):
            if dest[j]>cost[i][j]+dest[i]:
                dest[j] = cost[i][j] + dest[i]
    return dest

display(cost)
dist=dijkstra(0)
print("after")
print(dist)