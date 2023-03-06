from random import randint
def decouverte_tresor(infos, categorie) :
    """
Incrémente le nombre de pièces d’or du joueur en fonction du trésor
categorie : type de trésor
- 1 : entre 1 et 5 po
- 2 : entre 5 et 10 po
- 3 : entre 0 et 25 po
infos : données de jeu (niveaux, nombre de pièces d’or et points de vie)
"""
    if categorie == "1" :
        infos["po"] = infos["po"] + randint(1, 5)
    elif categorie == "2" :
        infos["po"] = infos["po"] + randint(5, 10)
    else :#équivalent de la catégorie 3
        infos["po"] = infos["po"] + randint(0, 25)