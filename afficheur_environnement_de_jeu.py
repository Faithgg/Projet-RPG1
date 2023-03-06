import le_modul_curses
def affiche_labyrinthe(lab, perso,objet, pos_perso,win, coul):
    """
    Affichage d’un labyrinthe
    lab : Variable contenant le labyrinthe
    perso : caractère représentant le personnage
    pos_perso : liste contenant la position du personnage
    [ligne, colonne]
    Pas de valeur de retour
    """
    n_ligne = 0
    j = 3
    for ligne in lab:
        for k in range(1,4):
            # remplace les chiffres représentant des trésors
            ligne = ligne.replace(str(k), objet)
        if n_ligne == pos_perso[1]:
            i=15
            for element in ligne[0:pos_perso[0]] :
                if str(element) =="€":
                    win.addstr(j +1, i,element,le_modul_curses.color("BLUE",coul))
                elif str(element) =="✘":
                    win.addstr(j +1, i,element,le_modul_curses.color("RED",coul))
                elif str(element) =="O":
                    win.addstr(j +1, i,element,le_modul_curses.color("GREEN",coul))
                else :
                    win.addstr(j +1, i,element,le_modul_curses.color("YELLOW",coul))

                i+=1
    #slicing
            # Coloration du personnage
            win.addstr(j +1, i, perso, le_modul_curses.color("MAGENTA", coul))
            i+=1
            for element in ligne[pos_perso[0]+1:] :
                if str(element) =="€":
                    win.addstr(j +1, i,element,le_modul_curses.color("BLUE",coul))
                elif str(element) =="✘":
                    win.addstr(j +1, i,element,le_modul_curses.color("RED",coul))
                elif str(element) =="O":
                    win.addstr(j +1, i,element,le_modul_curses.color("GREEN",coul))
                else :
                    win.addstr(j +1, i,element,le_modul_curses.color("YELLOW",coul))
                i+=1


        else :
            i=15
            for element in ligne :
                if str(element) =="€":
                    win.addstr(j +1, i,element,le_modul_curses.color("BLUE",coul))
                elif str(element) =="✘":
                    win.addstr(j +1, i,element,le_modul_curses.color("RED",coul))
                elif str(element) =="O":
                    win.addstr(j +1, i,element,le_modul_curses.color("GREEN",coul))
                else :
                    win.addstr(j +1, i,element,le_modul_curses.color("YELLOW",coul))

                i+=1
        n_ligne = n_ligne +1
        j+=1

