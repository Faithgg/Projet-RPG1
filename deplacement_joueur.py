import os
import les_donnees
import fights
import curses
import le_modul_curses
import bienvenue as recommencer

def verification_deplacement(lab,infos, pos_col, pos_ligne):
    """
    Indique si le déplacement du personnage est autorisé ou pas.
    lab : Labyrinthe
    pos_ligne : position du personnage sur les lignes
    pos_col : position du personnage sur les colonnes
    Valeurs de retour :
    None : déplacement interdit
    [colonne, ligne] : déplacement autorisé sur la case indiquée
    par la liste
    """
        # Calcul de la taille du labyrinthe
    n_cols = len(lab[0])
    n_lignes = len(lab)
    # Teste si le déplacement conduit le personnage en dehors de l’aire
    # de jeu
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1) :
    #le symbole \ indique que la ligne n’est pas terminée
        return None
    elif lab[pos_ligne][pos_col] == "O" : #######
    # Une position hors labyrinthe indique la victoire ##ici##
        return[-1, -1] 
    elif lab[pos_ligne][pos_col] == "1" or lab[pos_ligne][pos_col] == "2" or lab[pos_ligne][pos_col] == "3" :
# teste si le personnage se déplace sur un trésor
# Découverte d’un trésor
# fonction qui calcule le montant du butin
        les_donnees.decouverte_tresor( infos , lab[pos_ligne][pos_col] )
# On supprime le trésor découvert
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " + lab[pos_ligne][pos_col +1:]
        return [pos_col, pos_ligne]

        #Les groupes d'ennemis sont représentés par % 
    elif lab[pos_ligne][pos_col] == "✘" :
# Rencontre d’un ennemi
        fights.combat(infos)
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " + lab[pos_ligne][pos_col +1:]
        return [pos_col, pos_ligne]
    elif lab[pos_ligne][pos_col] != " " :
        return None
    else :
        return [pos_col, pos_ligne]



def choix_joueur(lab, infos, pos_perso,win):
    """
Demande au joueur de saisir son déplacement
et vérifie s’il est possible.
Si ce n’est pas le cas affiche un message,
sinon modifie la position du perso
dans la liste pos_perso
lab : Labyrinthe
pos_perso : liste contenant la position du personnage
[colonne, ligne]
Pas de valeur de retour
    """


    deplacement = None
    direction = None
#    choix = input("Votre déplacement (Haut/Bas/Droite/Gauche/Quitter) ? ")
#redéfinir la position de la personne

    direction = win.getch()
    if direction == 259 :
        deplacement = verification_deplacement(lab, infos,pos_perso[0], pos_perso[1] -1)
    elif direction == 258  :
        deplacement = verification_deplacement(lab,infos, pos_perso[0], pos_perso[1] +1)
    elif direction == 260  :
        deplacement = verification_deplacement(lab,infos, pos_perso[0] -1, pos_perso[1])
    elif direction == 261:
        deplacement = verification_deplacement(lab,infos, pos_perso[0] +1, pos_perso[1])
    elif direction==32 :
    # C'est la touche pour recommencer le jeu(la touche <espace>)
        recommencer.bienvenue1()
 
# 27 correspond à la touche [Echap]
    if direction == 27 :
        le_modul_curses.close_curses()
        os._exit(1)

    if deplacement != None :
        pos_perso[0] = deplacement[0] # modification du contenu de la liste
        pos_perso[1] = deplacement[1] # positon de la personne
        if pos_perso==[-1,-1]:
            infos["level"]=6

