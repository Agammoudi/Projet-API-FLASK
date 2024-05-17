# class Promo:
#     def __init__(self, annee, etudiants):
#         self.annee = annee
#         self.etudiants = etudiants

#     def __str__(self):
#         return f"Promo {self.annee}: {self.etudiants}"

# etudiants_promo = ["Aymen", "Ayoub", "Fatima"]
# promo_2024 = Promo(2024, etudiants_promo)
# print(promo_2024)



class Voiture:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def avancer(self):
        self.x += 1

    def reculer(self):
        self.x -= 1

    def afficher_position(self):
        print(f"Position de la voiture : ({self.x}, {self.y})")


voiture = Voiture(5, 5)
voiture.afficher_position() 
voiture.avancer()
voiture.afficher_position() 
voiture.reculer()
voiture.afficher_position()  
