
# recolter une valeur porte monnaie
# creer un produit qui aura pour valeur 50
# afficher la nouvelle valeur du porte monnaie, après son achat

import fractions


porteMonnaie = input("Combien avez-vous d'argent dans votre porte monnaie")
porteMonnaie = int(porteMonnaie)
lePain = 500
print ("le pain coute ",lePain," francs, merci d'acherter")
porteMonnaie -= lePain
print("Il vous reste ", porteMonnaie," dans votre porte monnaie")
