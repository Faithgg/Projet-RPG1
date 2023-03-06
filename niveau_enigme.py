import le_modul_curses
from numero_de_niveau import mini_barre_score as barre
def niveau1():
    win= le_modul_curses.fenetre(35,120,[2,5])
    couleur=le_modul_curses.init_colors()
    barre(1,win,couleur)
    win.addstr(4, 25,"Cette première étape du jeu consiste à repondre à l'énigme posée",le_modul_curses.color("GREEN", couleur))
    win.addstr(6, 25,"    par l'arbre de la forêt qui est un grand serre majestieux🌲🦚  ",le_modul_curses.color("GREEN", couleur))
    win.addstr(11, 25,"                              👉 ENIGME 👈                        ",le_modul_curses.color("MAGENTA", couleur))
    win.addstr(13, 25,"     <<   Je tappe ma mère puis je meurs. Qui suis-je 🤔?   >>    ",le_modul_curses.color("YELLOW", couleur))
    reponse,window = le_modul_curses.input(win,1)
    resultat1 = "allumettes"
    resultat2 = "allumette"
    while (reponse.lower() != resultat1) and (reponse.lower() != resultat2):
#C'est une création d'illusion pour faire croire au joueur que c'est la meme fenetre
        win= le_modul_curses.fenetre(35,120,[2,5])
        couleur=le_modul_curses.init_colors()
        barre(1,win,couleur)
        win.addstr(4, 25,"Cette première étape du jeu consiste à repondre à l'énigme posée",le_modul_curses.color("GREEN", couleur))
        win.addstr(6, 25,"    par l'arbre de la forêt qui est un grand serre majestieux🌲🦚  ",le_modul_curses.color("GREEN", couleur))
        win.addstr(11, 25,"                              👉 ENIGME 👈                        ",le_modul_curses.color("MAGENTA", couleur))
        win.addstr(13, 25,"     <<   Je tappe ma mère puis je meurs. Qui suis-je 🤔?   >>    ",le_modul_curses.color("YELLOW", couleur))
        reponse,windows =le_modul_curses.input(win,1)
        window =windows
    window.addstr(28, 25,"              Bravooooo🤩! Bonne aventure à vous 🙃!                ",le_modul_curses.color("YELLOW", couleur))
    window.addstr(29, 25,"                😍Tapez <Entrer> pour continuer😍                   ",le_modul_curses.color("GREEN", couleur))
    window.getch()

    window.erase()
    le_modul_curses.close_curses()
