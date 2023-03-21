import tkinter as tk
import random

# Initialiser la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Jeu du pendu")
label = tk.Label(fenetre, text="Bienvenue dans le jeu du pendu", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget

# Définir la liste de mots pour le jeu
liste_mots = ["correction", "opportuniste", "ascenseur", "evrest", "situation", "saturation", "programmeur","aviateur","musicien"]

# choisir un mots sur internet (a complété)
from bs4 import BeautifulSoup
from urllib.request import urlopen
html= urlopen("http://www.google.com")
bsObj = BeautifulSoup(html) 

# Choisir un mot aléatoire de la liste
mot_a_deviner = random.choice(liste_mots)

# Initialiser les variables du jeu
lettres_trouvees = []
lettres_manquees = []
nb_essais = 9

# Fonction pour afficher le mot caché avec les lettres déjà trouvées

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache


 
import random

liste_de_mot = ['correction', 'opportuniste', 'ascenseur', 'evrest', 'situation', 'saturation', 'programmeur','aviateur','musicien']
solution = random.choice(liste_de_mot)

tentative=8


affichage=""
a = (len(solution))
i = 1
while a >= i:
    affichage += "_"
    i += 1
print(affichage)

#fonctoin qui dit si la lettre est bonne si erreur essai-1 si bon dit que la lettre est bonne faut juste essaiyer de la placer sur l'interface
lettre = []
mauvaises_lettre = []
bonnes_lettres = []
while tentative >= 0 and "_" in affichage:
        proposition = input("entrer une lettre: ")
        x = proposition.isalpha()
        if len(proposition) > 1 and x == False:
            print("erreur, recommencer")
        
        elif len(proposition) <= 1 and x == True:
            
        
            if proposition not in solution:
                mauvaises_lettre += [proposition]
                print("mauvaises lettres: ", mauvaises_lettre)
    
            elif proposition in solution:
                bonnes_lettres +=[proposition]
                print("bonnes lettres: ", bonnes_lettres)
        
            if proposition not in solution:
                tentative -= 1
                print ("tentatives restantes", tentative)
        
            elif proposition in solution:
                affichage += proposition 
    

print(lettre) 
print("le mot est", affichage)
fenetre.mainloop()#lancement de la fenetre
