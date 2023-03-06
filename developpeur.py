import name
import os
import netoyeur_d_ecran
import le_modul_curses
def informations():
    win = le_modul_curses.fenetre(35, 120, (2, 5))
    couleur=le_modul_curses.init_colors()
    info =[
    "            +-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_  ",
    "            |                                                            |  ",
    "            |                             1️⃣                             |  ",
    "            |                 👨‍🎓 AGBAHE Manuel Govinda                |  ",
    "            |              Il a géré les niveaux 1 et 2 👨‍⚕️             |  ",
    "            |                                                            |  ",
    "            |                             2️⃣                             |  ",
    "            |                🧑‍🎓 EKLOU-DOVI BLESSING-GRACE              |  ",
    "            | Elle a géré la cohérence entre les fonctions et le menu 🗓️  |  ",
    "            |                                                            |  ",
    "            |                             3️⃣                             |  ",
    "            |                    🧑‍🎓 ISSIAKENE Hanane                   |  ",
    "            |  Elle a géré le niveau3 et le test des fonctionnalités 📽️   |  ",
    "            |                                                            |  ",
    "            |                             4️⃣                             |  ",
    "            |                  👨‍🎓 GLIN-DAYI Faithgot                  |  ",
    "            | Il a géré la cohérence entre les niveaux et le niveau5     |  ",
    "            |                                                            |  ",
    "            |                             5️⃣                             |  ",
    "            |                     🧑‍🎓 KHALIL Lamiaa                     |  ",
    "            |                 Elle a géré le niveaux 4 🤺                |  ",
    "             -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+ ",
    ]
    j=2
    for lines in info:
        win.addstr(j +1, 17,lines,le_modul_curses.color("GREEN",couleur))
        j+=1

    win.addstr(30, 40,"Faites «Entrer» ↩️ pour commencer le jeu🎮",le_modul_curses.color("MAGENTA",couleur))
    decision = win.getch()
    while decision != 10 :
        if decision==27 :
            netoyeur_d_ecran.efface_ecran()
            os._exit(1)
        decision = win.getch()
    le_modul_curses.animation(2)
    le_modul_curses.close_curses()
    name.name()
