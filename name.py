import officer
import le_modul_curses
"""La fonction name est presque faite de la meme facon que nous avons fait avec input() dans le fichier .py le_module_curses """
def name():
    liste = "abcdefghijklmnopqrstuvwxyz0123456789@é&#çàù$£§è"
    nom = ""
    longueur = 0

    while longueur <=15 :

        fenetre= le_modul_curses.fenetre(35,120,[2,5])
        couleur_de_fond = le_modul_curses.init_colors()
        fenetre.addstr(7, 20,"Pseudo :",le_modul_curses.color("YELLOW", couleur_de_fond))
        fenetre.addstr(7, 30, nom,le_modul_curses.color("MAGENTA", couleur_de_fond))
        fenetre.addstr(4, 35,"Ecrivez votre pseudo puis cliquez sur <Espace>",le_modul_curses.color("GREEN", couleur_de_fond))
        fenetre.addstr(1, 35,"             ATTENTION PAS D'ERREUR           ",le_modul_curses.color("RED", couleur_de_fond))
        decision =fenetre.get_wch()
        if (decision == " " and len(nom)>=3) or longueur==15:
            le_modul_curses.close_curses()
            return officer.officer(nom)
        else:
            l = le_modul_curses.recherche(liste,decision.lower())
            if l!="":
                nom = nom + str(decision)
            else:
                longueur-=1
        longueur+=1