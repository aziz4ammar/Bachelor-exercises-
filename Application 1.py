import numpy as np
m=dict(num=int,NP=str,sexe=str())
t=np.array([m]*100)
v=np.array([m]*100)
def verif(ch):
    while(ch!="")and(("A"<=ch[0].upper()<="Z")or(ch[0]==" ")):
        ch=ch[1:]
    return ch==""
def remplir (t):
    global n
    n=0
    b=False
    while b==False:
        n+=1
        t[n]=dict(num=int,NP=str,sexe=str())
        t[n]["num"]=int(input("numero : "))
        test=False
        while test==False:
            t[n]["NP"]=input("Nom et prenom : ")
            test=(verif(t[n]["NP"]))
        test=False
        while test==False:
            t[n]["sexe"]=input("sexe : ")
            test=(t[n]["sexe"]in["M","F"])
        test=False
        while test==False:
            rep=input("voulez-vous continuer ?O/N:")
            rep=rep.upper()
            test=rep in["N","O"]
        b=(rep=="N")
def rang(x,n,t):
    ra=1
    for i in range (1,n+1):
        if (t[i]["num"]<x):
            ra+=1
    return ra
def ranger(n,t,v):
    for i in range (1,n+1):
        r=rang(t[i]["num"],n,t)
        v[r]=t[i]
def affiche(n,v):
    for i in range(1,n+1):
        print(v[i]["num"]," ",v[i]["NP"]," ",v[i]["sexe"])
       
remplir(t)
ranger(n,t,v)
affiche(n,v)