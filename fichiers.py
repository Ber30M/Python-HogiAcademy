"""Mode d'ouverture : r(lecture seule)
                    : w (écriture avec remplacement)
                    : a (écriture avec ajout en fin de fichier)
                    : x (lecture et écriture)
                    : r+ (lecture/écriture dans un même fichier)
                    
"""
"""from cgi import print_directory


fichier = open("données.txt","r")
print(fichier.read())

fichier.close()"""

with open("données.txt","w") as fichier:
    fichier.write("Bonjour")
    