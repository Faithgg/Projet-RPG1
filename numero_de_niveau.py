
import le_modul_curses
def barre_score(infos,win,coul) :
    """
Barre et mini_barre de score affichant les données du jeu
"""
    win.addstr(1, 9,"Vie :", le_modul_curses.color("CYAN", coul))
    if infos["pv"] < 5 :
        win.addstr(1, 16,str(infos["pv"])+ " 💛", le_modul_curses.color("RED", coul))
    else :
        win.addstr(1, 16,str(infos["pv"]) + " 💝", le_modul_curses.color("GREEN", coul))
    win.addstr(1, 33,"Points :", le_modul_curses.color("BLUE", coul))
    win.addstr(1, 43,str(infos["po"])+ " 💶", le_modul_curses.color("GREEN", coul))
    win.addstr(1, 55,"Niveau :", le_modul_curses.color("CYAN", coul))
    win.addstr(1, 65,str(infos["level"]), le_modul_curses.color("MAGENTA", coul))
    win.addstr(1, 80,"Joueur :", le_modul_curses.color("RED", coul))
    win.addstr(1, 90,infos["name"] + " 🃏", le_modul_curses.color("YELLOW", coul))


def mini_barre_score(niveau,win,couleur):
    win.addstr(1, 2,"Niveau :", le_modul_curses.color("YELLOW", couleur))
    win.addstr(1, 12,str(niveau), le_modul_curses.color("BLACK", couleur))
