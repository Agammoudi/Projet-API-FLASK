import random
# equipe = "Real Madrid"
# type_sport = "football"
# nombre_joueurs = 11
# numero_joueur_5 = "Bellingham"

# print("Nom de l'équipe :", equipe)
# print("Nom du joueur portant le numéro 5 :", numero_joueur_5)


# list=[1,2,3,4,5,6,7]
# for nombre in  list :
#     print(nombre)

# def addition():
#     valuer1 = random.randint(0,100)
#     valuer2 = random.randint(0,100)
#     somme = valuer1 + valuer2
#     return somme

# resultat = addition()
# print(resultat)

# def addition():
#     valuer1 = random.choice(range(101)) 
#     valuer2 = random.choice(range(101))  
#     somme = valuer1 + valuer2
#     return somme

# resultat = addition()
# print(resultat)
def aleatoire(boolen,liste,min,max) :
    if boolen == True :
        res = random.choice(liste)
        return res
    else:
        res = random.randint(min,max)
        return res


liste=[1,20,30]
resultat = aleatoire(False,liste,1,8)

print(resultat)
