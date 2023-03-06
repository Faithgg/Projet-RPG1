import netoyeur_d_ecran
import os
import name
import developpeur
import le_modul_curses

def bienvenue1() :
    bienvenuee =[
"                                    . ----- .              ",
"                                   / >     < \             ",
"                                  |     °     |              ",
"                                   \   ---   /               ",
"                         😍            _____          😍         ",
"                         |            _(_)_           |      ",
"                         |          /       \         |      ",
"                         |         //|  ♥️  |\\\\        |           ",
"                         |           |_____|          |       ",
"                         |           |-----|          |     ",
"                         |           | | | |          |       ",
"                         |           |_| |_|          |         ",
"                         |           (_) (_)          |         ",
"                          \                          /           ",
"                           +------------------------+            ",
"                           |÷----------------------÷|           ",
"                           ||      Bienvenue       ||           ",
"                           |÷----------------------÷|           ",
"                           +------------------------+            ",
"                          /         💻HETIC💻         \           ",
"                         /     #NO TECH NO FUTURE     \           ",
"              +----------                              ----------+ ",
"              |      😇 La vie c'est comme un jeu vidéo 😇        | ",     
"              |En faisant ce que ton créateur te dit, tu gagneras |  ",
"              |                     Aliou AOUDI ✍️                | ",
"              +--------------------------------------------------+ "
]
    fenetre= le_modul_curses.fenetre(35,120,[2,5])
    j =1
    for lines in bienvenuee :
        Couleur_de_teste = le_modul_curses.init_colors()
        fenetre.addstr(j+1, 20,lines,le_modul_curses.color("YELLOW", Couleur_de_teste))#création de la fenetre de jeu
        j+=1
#Juste des chaines de caractères affichées sur la fenetre crée
    fenetre.addstr(j +2, 10,"⓵ - Tapez <Entrer> pour commencer le jeu  ",le_modul_curses.color("GREEN", Couleur_de_teste))
    fenetre.addstr(j +3, 10,"⓶ - Tapez <Tab> pour des informations sur le développeur",le_modul_curses.color("BLUE", Couleur_de_teste))
    fenetre.addstr(j +4, 10,"③ - Tapez <Echape> pour quitter le Jeu",le_modul_curses.color("RED", Couleur_de_teste))
#Quelques raisonnements pour continuer le jeu en fonction de la touche tappée par le joueur.
    decision =fenetre.getch()

    if decision == 10 :
        fenetre.erase()
        le_modul_curses.close_curses()
        Couleur_de_teste = le_modul_curses.init_colors()
        fenetre= le_modul_curses.fenetre(35,120,[2,5])

        fenetre.addstr(4, 20,"👧Mia est une jeune fille de 15 ans qui s'est faite capturer par une ogre.",le_modul_curses.color("CYAN", Couleur_de_teste))
        fenetre.addstr(6, 20,"La disparition de Mia éveille le village 🏘️ tout entier sur la menace qu'est",le_modul_curses.color("CYAN", Couleur_de_teste))
        fenetre.addstr(8, 20,"cette Ogre. C'est alors que vous, dans le role du Cherif👲 du village décidez",le_modul_curses.color("CYAN", Couleur_de_teste))
        fenetre.addstr(10, 20,"de se mettre à la poursuite de l'ogre et récupérer les enfants 👩‍👧‍👦.",le_modul_curses.color("CYAN", Couleur_de_teste))
        fenetre.addstr(15, 20,"En allant à sa poursuite, il rencontra beaucoup de difficultés sur la route 🛣️.",le_modul_curses.color("BLUE", Couleur_de_teste))
        fenetre.addstr(17, 20,"Ce qui transformât sa poursuite en aventure pour retrouver les enfants disparus.",le_modul_curses.color("BLUE", Couleur_de_teste))
        fenetre.addstr(20, 20,"🫳Durant tout le jeu, tapez <Echape> pour quitter et <Espace> pour recommencer",le_modul_curses.color("YELLOW", Couleur_de_teste))
        fenetre.addstr(25, 48,"😍Touchez pour continuer😍",le_modul_curses.color("GREEN", Couleur_de_teste))
        decision =fenetre.getch()
        name.name()
    elif decision== 9 :
        fenetre.erase()
        le_modul_curses.close_curses()
        developpeur.informations()
    elif decision == 27 :
        fenetre.erase()
        netoyeur_d_ecran.efface_ecran()
        le_modul_curses.close_curses()
        os._exit(1)
    else:
        fenetre.erase()
        le_modul_curses.close_curses()
        bienvenue1()
        os._exit(1)