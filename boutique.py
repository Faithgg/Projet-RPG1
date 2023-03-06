import le_modul_curses

def acheter_vie(infos) :
    win = le_modul_curses.fenetre(35, 120, (2, 5))
    couleur= le_modul_curses.init_colors()
    vie_ajoutee = int((infos["po"]*3/4)//5)
    infos["pv"] = vie_ajoutee
    infos["po"] = int((infos["po"]*3/4) % 5 + (infos["po"]*1/4))
    win.addstr(15, 40,"💹 Vu votre caisse, vous avez chargé " + str(vie_ajoutee) + " vies.",le_modul_curses.color("CYAN",couleur))
    win.addstr(17, 40,"🥳 Faites <Entrer> pour continuer le jeu🫣 " ,le_modul_curses.color("GREEN",couleur))
    decision = win.getch()
    while decision != 10 :
        decision = win.getch()
