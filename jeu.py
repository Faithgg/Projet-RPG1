import le_modul_curses
import niveau_3
import numero_de_niveau
import afficheur_environnement_de_jeu
import deplacement_joueur
import os
import niveau_equation as niveau_2
import netoyeur_d_ecran
import boutique
import lancer_combat
import niveau_enigme
#cette liste contient notre labyrinthe
labyrinthe =[
"+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+",
"|    1  3   | 2   ✘ | ✘ | 1 3   |  1   2    | 3   | |3  3 |  ✘        ✘ | ✘ | |  2  | |",
"| --+---+-- + | +---+ + | | | | | --+ --+-+-+ | --| | +---+ --+ | | +-- +-+ | +---+ | |",
"| ✘ | ✘ |   3 | | | ✘ | | | | | | 3 | 2 | | | |   ✘   | |     | | | | 1   | 3  1  | | |",
"|---+ --+ +-- +-+ | +-| |-+-+ |-| --| | | | +-+ +-----+ +-- +---+ | +-+-+ |-- +-+ | | |",
"| 1 |1    |1 1 ✘    |1| |   3 | |  1| |  3      | ✘  ✘  3   | 1   | ✘ | | |   | ✘ | ✘ |",
"|-+ +-- + |---- +---+ +-| | |-+ | | |-----+ |-+ | | | ----- | --+ |---+ +-+-+ | +-+ +-|",
"| |   1 | |   1 |2   ✘  | |  2  | | |  2  | | ✘   | |  3| 3 |  ✘| | | ✘     | | | 1 | |",
"| | +---|-| + --+ +-- + | +-+ --+-|-+-- +-+-|-----+-|---+---+ --| | +-+---- |-| | --+ |",
"|✘|✘| | | | |  ✘  |   | | 3 |  ✘  |  ✘  |   |  1  ✘ | 3   1     | ✘   | 1   | |    3  |",
"| | | | | | |-+ +-+ | | +-- +-+ +-+ +-- +-+ | ------+ +-- --+-- |-+ --|-- + | |-- --+-|",
"| |3|  1  | | | |   | |   3   | |✘  |  2  | |    2    |  1  | ✘ | |   | ✘ | | | ✘   | |",
"| |-+-- --+ | |-+ | +-|---- +-|-|-- |-- | | +---+-- +-+-- --| --+ +-- | --+ | | | +-+ |",
"| |     2  ✘  | ✘ |   | ✘   | | | ✘ | ✘ | |  1  | ✘ |   3   | ✘   ✘ | | | ✘  ✘  | |   |",
"| | --+-------+ --| +-|-+ | | | |---+---| | | --+ +-|---+ +-+ +-- --+-|-+ | --+ | | | |",
"|   2 |  2  3   ✘ | | |✘| | ✘   |   2   | | |  ✘  | |   | |   |  3    |   | ✘ | | | | |",
"| | | | +---+-| | |-| | | +-+---+-+ +-+ | | | +-- | +-+1| | | |-+ +-| | | |---|-| |-+ |",
"| | | | |  3|   | | | ✘ |   |  2  | | |     | |   |   |   | | | | |     | |✘  | | |✘  |",
"| |-+-+ + --+-+-| | | | |-+ | ----+-+ | | +-|-|-- | +-|-+ |-+-| +-+ --+-+ |-- | | | | |",
"| | ✘      ✘  | | |   | | |  3 ✘  1     | | | | 3   | | | |   |   1   | ✘ | ✘ |  1  | |",
"|-+---- +-- | | | | --+-| | --+ --+ | | |-+ | +-+ | | | +-+ --+-- --+-|---| --| | | |-|",
"|   ✘   |1  | |   |  3  | | ✘ |   | | | |   |   | | |   ✘     |     | |   |   | | | | |",
"|-+ | +-+-- +-+---| --+-+ |-+-+-- | +-+-| | +-- |-+-|-- | --+ | +-+-+ +-- | --| +-|-| |",
"| | | |       ✘       |     | 2   |     | |  3  |   |   | 1 |   | |     ✘  1  |   | | |",
"| | +-| | --+-- --+-- |-- | | ----| ----+-+ +---+ | +-- |-- |-- | | | | +---- | --+ | |",
"|   1 | |   | 1   | 1 |   |   3   |  ✘ 3  ✘ | ✘ 1 |  ✘  |   | 2 |  ✘| | | 1  3    3   O",
"+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+"

    ]


def jeu(infos, perso,objet, pos_perso,win,coul):
    """
    Boucle principale du jeu. Affiche le labyrinthe dans ses différents
    états après les déplacements du joueur.
    level : Labyrinthe
    n_level : numéro du niveau courant
    perso : caractère représentant le personnage
    pos_perso : liste contenant la position du personnage
    [colonne, ligne]
    """
    le_modul_curses.close_curses()
    #Appel de chaque fichier_niveau en du numéro de niveau envoyé par le fichier officer
    while infos ["level"]<=5 :
        win = le_modul_curses.fenetre(35, 120, (2, 5))
        numero_de_niveau.barre_score(infos,win,coul)

        if infos["pv"] <= 0 :
            if (infos["po"]*3/4) >= 5 :
                win.addstr(16, 30,"🧑‍🏫 Vous avez assez de pièces pour vous soigner 👨‍🏫")
                win.addstr(18, 30,"👩‍💻 Pour vous soigner utilisez la touche <Entrer> 🧑‍💻")
                decision = win.getch()
                le_modul_curses.animation(1)
                if decision == 10 :
                    le_modul_curses.close_curses()
                    boutique.acheter_vie(infos)
                else :
                    le_modul_curses.animation("lose")
                    le_modul_curses.close_curses()
                    netoyeur_d_ecran.efface_ecran()
                    os._exit(1)

            else:
                le_modul_curses.animation("lose")
                le_modul_curses.close_curses()
                netoyeur_d_ecran.efface_ecran()
                os._exit(1)
        if infos["level"] == 1:
            le_modul_curses.animation("level1")
            le_modul_curses.close_curses()
            niveau_enigme.niveau1()
            break
        if infos["level"] == 2:
            le_modul_curses.animation("level2")
            le_modul_curses.close_curses()
            niveau_2.niveau2()

            break
        if infos["level"] == 3:
            le_modul_curses.animation("level3")
            le_modul_curses.close_curses()
            niveau_3.game()
            break

        if infos["level"]==5 :
            afficheur_environnement_de_jeu.affiche_labyrinthe(labyrinthe, perso,objet, pos_perso,win,coul)
            deplacement_joueur.choix_joueur(labyrinthe,infos, pos_perso,win)
        if pos_perso == [-1, -1] : 
            win.erase()
            le_modul_curses.close_curses()
            break
        if infos["level"] == 4:
            lancer_combat.combat_ogre(infos,1,0)
            le_modul_curses.close_curses()
            break
