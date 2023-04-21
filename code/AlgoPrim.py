#Algorithme de Prim#

from FctBase import *

#Donne les sommets du sous-arbre connexe construit#
 
def SommetsArbre(SousArbre):
    n=len(SousArbre)
    ListeSommets=[]
    for k in range(n):
        for i in range(2):
            nbSommets=len(ListeSommets)
            test=0
            for j in range (nbSommets):
                if ListeSommets[j]==SousArbre[k][i]:
                    test=1
            if test==0:
                ListeSommets.append(SousArbre[k][i])
    return ListeSommets

#Retourne la liste des sommets que ne contient pas la liste mais qui sont présents dans le graph#

def SommetsNonExplores(SommetsExplores,G):
    SommetSNExp=[]
    n=len(SommetsExplores)
    N=len(G)
    for k in range(N):
        Test=0
        for i in range(n):
            if k+1==SommetsExplores[i]:
                Test=1
        if Test==0:
            SommetSNExp.append(k+1)
    return SommetSNExp

#Affiche le liste des distances des chemins entre les points extérieurs et intérieurs au sous-arbre.#

def ListeDistance(SommetsArbre,SommetsExterieurs,G):
    nArbr=len(SommetsArbre)
    nExt=len(SommetsExterieurs)
    ListDist=[]
    for k in range(nArbr):
        for j in range(nExt):
            if G[SommetsArbre[k]-1][SommetsExterieurs[j]-1]!=0:
                ListDist.append([G[SommetsArbre[k]-1][SommetsExterieurs[j]-1],[SommetsArbre[k],SommetsExterieurs[j]]])
    return ListDist

#Couple de distance minimal#

def minDist(L):
    n=len(L)
    minDist=L[0][0]
    indice=0
    for k in range(n):
        if L[k][0]<minDist and L[k][0]!=0:
            minDist=L[k][0]
            indice=k
    return L[indice][1]

#Algorithme principal#

def Prim(G):
    N=len(G)
    SousArbre=[]
    distMin=100000000000000
    sommetMin=0
    for k in range(1,N):
        if distMin>G[0][k] and G[0][k]!=0:
            distMin=G[0][k]
            sommetMin=k+1
    SousArbre.append([1,sommetMin])
    nbSommets=2
    while N>nbSommets:
        CheminExplores=SommetsArbre(SousArbre)
        CheminCourt=minDist(ListeDistance(CheminExplores,SommetsNonExplores(CheminExplores,G),G))
        SousArbre.append(CheminCourt)
        nbSommets=len(SousArbre)+1
    return SousArbre

#Exécution#

P=Prim(G)
print(P)
