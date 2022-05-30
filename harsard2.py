from random import *
a=5
ns=1
borne_sup=50
nb=randint(0,borne_sup)
ton_nombre=0
while(1):
    
        c=(input("\n\t entrer votre nom : "))
        print("\n")
        b=int(input("\n\t entrer le nombre essais <=5  : "))
        print("\n")
        print("\n\tA vous de devinez ce nombre en ",b," tantative")
        while (ton_nombre !=nb and ns<= b):
                print(" \n\tessais",ns)
                ton_nombre=int(input( "\n\t votre proposition s.v.p : "))
                if ton_nombre< nb:
                        print("\n\t trop petit")
                        ns+=1
                elif ton_nombre>nb:
                        print("\n\t trop grand")
                        ns+=1
                else:
                       print("\n\t Bravo ! ",c,"vous avez trouvé",nb,"en",ns," essais")
                       ns+=1
                       print("\n")    
        if ns> b and ton_nombre != nb:
                    print("Desolé ",c,"vous avez utilisé tous vos ",b," essais en vin")
                    print(" j'avais choisis ",nb)
                    print("\n\t bonne chance pour la suite ")
            
