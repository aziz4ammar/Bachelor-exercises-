def remplir():
    f=open("nombre.txt","w")
    test=False
    while test==False:
        d=False
        while d==False:
            x=int(input("donner un entier >= 0 : "))
            d=x>=0
        f.write(str(x)+"\n")
        e=False
        while e==False:
            rep=input("voulez-vous continuer ? O/N : \n")
            rep=rep.upper()
            e=rep in ["N","O"]
        test=(rep=="N")
    f.close()
def eclater():
    f=open("nombre.txt","r")
    fp=open("pairs.txt","w")
    fimp=open("impairs.txt","w")
    ch=f.readline()
    while (ch!=""):
        if (int(ch)%2==0):
            fp.write(ch)
        else:
            fimp.write(ch)
        ch=f.readline()
    fp.close()
    fimp.close()
    f.close()
def affiche(ch):
    ft=open(ch,"r")
    lig=ft.readline()
    while(lig!=""):
        print(lig[:-1])
        lig=ft.readline()
    ft.close()
#pp
remplir()
eclater()
print("les pairs sont :")
affiche("pairs.txt")
print("les impairs sont :")
affiche("impairs.txt")   
    