import le_modul_curses
from numero_de_niveau import mini_barre_score as barre
#Juste de la logique
def niveau2():
    win= le_modul_curses.fenetre(35,120,[2,5])
    couleur=le_modul_curses.init_colors()
    barre(2,win,couleur)
    win.addstr(4, 25,"😎 Pour vous tester, les nains de la forêt vous ont préparé une   ",le_modul_curses.color("GREEN", couleur))
    win.addstr(6, 25,"équation à résoudre. La solution est l'année (Ap J-C) où a lieu         ",le_modul_curses.color("GREEN", couleur))
    win.addstr(8, 25,"le premier enlèvement d'enfant par l'orgre dans ce village.     ",le_modul_curses.color("GREEN", couleur))
    win.addstr(11, 25,"                           👉 EQUATION 👈                      ",le_modul_curses.color("MAGENTA", couleur))
    win.addstr(13, 25,"<< (|x|)¹  = |-1979| où |y| est la valeure absolue de y. TROUVEZ x 🤓!>>",le_modul_curses.color("YELLOW", couleur))
    reponse,window = le_modul_curses.input(win,2)
    resultat = 1979
    while int(reponse) != resultat:
#C'est une création d'illusion pour faire croire au joueur que c'est la meme fenetre
        win= le_modul_curses.fenetre(35,120,[2,5])
        couleur=le_modul_curses.init_colors()
        barre(2,win,couleur)
        win.addstr(4, 25,"😎 Pour vous tester, les nains de la forêt vous ont préparé une   ",le_modul_curses.color("GREEN", couleur))
        win.addstr(6, 25,"équation à résoudre. La solution est l'année (Ap J-C) où a lieu         ",le_modul_curses.color("GREEN", couleur))
        win.addstr(8, 25,"le premier enlèvement d'enfant par l'orgre dans ce village.     ",le_modul_curses.color("GREEN", couleur))
        win.addstr(11, 25,"                           👉 EQUATION 👈                      ",le_modul_curses.color("MAGENTA", couleur))
        win.addstr(13, 25,"<< (|x|)¹  = |-1979| où |y| est la valeure absolue de y. TROUVEZ x 🤓!>>",le_modul_curses.color("YELLOW", couleur))
        reponse,window =le_modul_curses.input(win,2)

    win= le_modul_curses.fenetre(35,120,[2,5])
    couleur=le_modul_curses.init_colors()
    barre(2,win,couleur)
    win.addstr(4, 25,"😎 Pour vous tester, les nains de la forêt vous ont préparé une   ",le_modul_curses.color("GREEN", couleur))
    win.addstr(6, 25,"équation à résoudre. La solution est l'année (Ap J-C) où a lieu         ",le_modul_curses.color("GREEN", couleur))
    win.addstr(8, 25,"le premier enlèvement d'enfant par l'orgre dans ce village.     ",le_modul_curses.color("GREEN", couleur))
    win.addstr(11, 25,"                           👉 EQUATION 👈                      ",le_modul_curses.color("MAGENTA", couleur))
    win.addstr(13, 25,"<< (|x|)¹  = |-1979| où |y| est la valeur absolue de y. TROUVEZ x 🤓!>>",le_modul_curses.color("YELLOW", couleur))
    win.addstr(21, 25,"                                😍Bravoooo😍!                          ",le_modul_curses.color("MAGENTA", couleur))
    win.addstr(23, 25,"Entrez ensuite son équivalent en hexadécimal pour activer votre armement🥲",le_modul_curses.color("YELLOW", couleur))
    reponse,window = le_modul_curses.input(win,3)
    resultat = "7BB"
    while reponse != resultat:
#Pareil
        win= le_modul_curses.fenetre(35,120,[2,5])
        couleur=le_modul_curses.init_colors()
        barre(2,win,couleur)
        win.addstr(4, 25,"😎 Pour vous tester, les nains de la forêt vous ont préparé une   ",le_modul_curses.color("GREEN", couleur))
        win.addstr(6, 25,"équation à résoudre. La solution est l'année (Ap J-C) où a lieu         ",le_modul_curses.color("GREEN", couleur))
        win.addstr(8, 25,"le premier enlèvement d'enfant par l'orgre dans ce village.     ",le_modul_curses.color("GREEN", couleur))
        win.addstr(11, 25,"                           👉 EQUATION 👈                      ",le_modul_curses.color("MAGENTA", couleur))
        win.addstr(13, 25,"<< (|x|)¹  = |-1979| où |y| est la valeur absolue de y. TROUVEZ x 🤓!>>",le_modul_curses.color("YELLOW", couleur))
        win.addstr(21, 25,"                                😍Bravoooo😍!                          ",le_modul_curses.color("MAGENTA", couleur))
        win.addstr(23, 25,"Entrez ensuite son équivalent en hexadécimal pour activer votre armement🥲",le_modul_curses.color("YELLOW", couleur))
        reponse,windows =le_modul_curses.input(win,3)
    window.addstr(28, 25,"                      😻Bravoooo! Bonne suite🥷!                       ",le_modul_curses.color("YELLOW", couleur))
    window.addstr(29, 10,"Les esprits du village vous envoient l'oiseau 🦉 mystique pour vous conduire dans la suite.",le_modul_curses.color("YELLOW", couleur))
    window.addstr(30, 10,"Il vous guidera dans la cabane où habite l'ogre et sa troupe afin que vous puissiez combattre 🤺.",le_modul_curses.color("YELLOW", couleur))
    window.addstr(31, 25," En outre, il ne peut s'exprimer qu'en 🔥Anglais  pour vous orienter jusqu'à l'Ogre.",le_modul_curses.color("YELLOW", couleur))
    window.addstr(33, 25,"                👨‍🚀 Tapez <Entrer> pour continuer 👨‍🚀                   ",le_modul_curses.color("GREEN", couleur))
    window.getch()
    window.erase()
    le_modul_curses.close_curses()
