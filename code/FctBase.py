import random

#Représentation du graph sous forme matricielle#

G=[
    [0,1,4,0,1],
    [1,0,0,2,1],
    [4,0,0,1,2],
    [0,2,1,0,1],
    [1,1,2,1,0]
]
# Test unitaire 1#

#G=[[0,1,0,0,0],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,1],[0,0,0,1,0]]

# Test unitaire 2#

#G=[[0,1,0,0,2],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,1],[2,0,0,1,0]]

#Génération graphe aleatoire de taille n#

def graphAlea(n):
    A=[]
    for k in range (n):
        A.append([])
        for i in range(n):
            A[k].append(random.randint(0,10))
    for k in range (n):
        A[k][k]=0
    return A
