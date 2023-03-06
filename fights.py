from random import randint
def combat(infos) :
    """
Détermine le nombre de points de vie perdus lors d’un combat
infos : données de jeu (niveaux, nombre de pièces d’or et points de vie)
"""
    ennemi = randint(1, 4) # Nombre d'ennemi rencontrés
    if ennemi == 1 :
        infos["pv"] = infos["pv"] - randint(1, 5)
    elif ennemi >= 2 :
        infos["pv"] = infos["pv"] - randint(3, 10) 