import le_modul_curses
import jeu
import netoyeur_d_ecran as chiffon
import os as sortie
#Après tous les niveaux, on a réservé cette récompense au jours qui terminerait tout. 
recompense= [
" +_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+ ",
"[]  _-_                                    []",
"[] |---|  MERCI POUR NOUS AVOIR SAUVÉ!     []",
"[]  -_-                              .Mia♥ []",
" +_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+ "
]

def officer(name_du_joueur) :

    infos = {
        "po" : 0,#point ou pieces d'or
        "pv" : 100,#point de vie
        "level" : None,#Le numéro du niveau
        "name" : name_du_joueur # Le nom du joueur
    }

    perso = "☻"#définition du caractère qui représente notre personne

    n_levels = 6 # Variable contenant le nombre total de niveaux

    for n_level in range(1, n_levels +1) :
        win = le_modul_curses.fenetre(35, 120, (2, 5))
        # Initialisation des couleurs
        coul = le_modul_curses.init_colors()
        # Attente de l’appui sur une touche
        pos_perso = [1,1]
        infos["level"] = n_level
        objet = "€"
        jeu.jeu(infos, perso, objet, pos_perso,win,coul)

        if n_level == 6 :
            win = le_modul_curses.fenetre(35, 120, (2, 5))
            # Initialisation des couleurs
            coul = le_modul_curses.init_colors()
            i=1
            for ligne in recompense:
                win.addstr(i+15,36,ligne,le_modul_curses.color("BLACK",coul))
                i+=1
            win.getch()
            le_modul_curses.animation("fin")
            chiffon.efface_ecran()
            sortie._exit(1)
            
