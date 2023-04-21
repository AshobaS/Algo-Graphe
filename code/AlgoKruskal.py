#Algorithme de Kruskal#

from FctBase import *

#Classement du poids des arrêtes du graph#

def ClassementArretes(G):
    listeDistance=[]
    N=len(G)
    for i in range(N):
        for j in range(N):
            if G[i][j]!=0 and i<j:
                listeDistance.append([G[i][j],[i+1,j+1]])
    n=len(listeDistance)
    ListeClassee=[]
    while n>0:
        minD=listeDistance[0][0]
        indice=0
        for k in range (1,n):
            if minD>listeDistance[k][0]:
                minD=listeDistance[k][0]
                indice=k
        ListeClassee.append(listeDistance[indice])
        del listeDistance[indice]
        n=len(listeDistance)
    return ListeClassee

#Donne le nombre de sommets distincts dans un sous-arbre plus une arrête#

def NombreSommet(SousArbre,Arrete):
    n=len(SousArbre)
    ListeSommets=[Arrete[0],Arrete[1]]
    for i in range (n):
        test0=0
        test1=0
        l=len(ListeSommets)
        for k in range(l):
            if ListeSommets[k]==SousArbre[i][0]:
                test0=1
            if ListeSommets[k]==SousArbre[i][1]:
                test1=1
        if test0==0:
            ListeSommets.append(SousArbre[i][0])
        if test1==0:
            ListeSommets.append(SousArbre[i][1])
    return len(ListeSommets)

def ListeDesSommets(SousArbre):
    n=len(SousArbre)
    ListeSommets=[SousArbre[0][0],SousArbre[0][1]]
    for i in range (n-1):
        test0=0
        test1=0
        l=len(ListeSommets)
        for k in range(l):
            if ListeSommets[k]==SousArbre[i][0]:
                test0=1
            if ListeSommets[k]==SousArbre[i][1]:
                test1=1
        if test0==0:
            ListeSommets.append(SousArbre[i][0])
        if test1==0:
            ListeSommets.append(SousArbre[i][1])
    return ListeSommets


#Vérification des cycles#

def VerifCycle(SousArbre,Arrete):
    Arbre=SousArbre.append(Arrete)
    L=ListeDesSommets(Arbre)
    n=len(L)
    for k in range(n):
        test=0
        SommetsVisites=[k+1]
        ListeArretes=Arbre
        while test!=1:
            nbChemin=len(ListeArretes)
            nbSommets=len(SommetsVisites)
            for i in range (nbChemin):
                for j in range (nbSommets):
                    if ListeArretes[i][0]==SommetsVisites[j]:
                        SommetsVisites.append(ListeArretes[i][1])
                        del(ListeArretes[i])
                    if ListeArretes[i][1]==SommetsVisites[j]:
                        SommetsVisites.append(ListeArretes[i][0])
                        del(ListeArretes[i])
                    else:
                        test=1
        if DoublonsSommets(SommetsVisites)==True:
            return True
    return False
            
def DoublonsSommets(ListeSommets):
    n=len(ListeSommets)
    for k in range (n):
        Sommet=ListeSommets[k]
        for i in range (k+1,n):
            if ListeSommets[i]==Sommet:
                return True
    return False

#Algorithme principal#

def Kruskal(G):
    C=ClassementArretes(G)
    SousArbre=[]
    SousArbre.append(C[0])
    del(C[0])
    nbArretes=len(C)
    for k in range (nbArretes):
        TestCycl=VerifCycle(SousArbre,C[0])
        if TestCycl==False:
            SousArbre.append(C[0])
    return SousArbre

#Exécution#

C=ClassementArretes(G)
print(C)
SousArbre=[[1,2],[2,3],[4,5]]
Arrete=[1,3]
Test=VerifCycle(SousArbre,Arrete)
print(Test)
