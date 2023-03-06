import curses


def fenetre(lignes, cols, position):
    """
Initialisation des paramètres graphiques
lignes : nombre de lignes (en caractères)
cols : nombre de colonnes (en caractères)
de la fenêtre graphique 
On retourne la fenetre crée
"""
    curses.initscr()
    curses.beep()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    window = curses.newwin(lignes, cols, position[0], position[1])
    window.border(0)
    window.keypad(1)
    return window


def close_curses() :
    """
Restauration des paramètres graphiques
"""
# Appel des fonctions inverses que celles invoquées dans la fonction fenetre en haut
    curses.echo()
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()

def recherche(liste, element):
    for composants in liste :
        if composants == element :    
            return element
    return ""
#En besoin de fonction pour recueillir certaines informations chez le jouer et les afficher automatiquement, on s'est basé sur les 
#fonctions de curses et de quelques logiques pour mettre en place ceci
def input(fenetre,id) :#Pour le nom, c'est juste en rappel de input qu'on utilisait tant en console simple
    liste = "abcdefghijklmnopqrstuvwxyz0123456789@é&#çàù$£§è"
    if id ==2 :
        liste = "1234567890"#Pour un de ses appels, on a eu besoin que de recueillir des chiffres pour les transformer en int()
        #on a donc du créer des id en paramètre et on a varrié les appels avec l'idée.
    nom = ""
    longueur = 0

    while longueur <=15 :#on a limité les entrés à 15 caractères. C'est largement surfisant pour nous pour recueillir la 
    #vraie réponse
        couleur_de_fond = init_colors()
        if id ==1 or id==2:
            fenetre.addstr(19, 20,"Résultat:",color("RED", couleur_de_fond))
            fenetre.addstr(19, 30, nom,color("BLUE", couleur_de_fond))
        elif id==3:
            fenetre.addstr(25, 20,"Résultat:",color("RED", couleur_de_fond))
            fenetre.addstr(25, 30, nom,color("BLUE", couleur_de_fond))

        fenetre.addstr(17, 35,"Ecrivez le résultat puis cliquez sur <Espace>",color("GREEN", couleur_de_fond))
        fenetre.addstr(1, 35,"             ATTENTION PAS D'ERREUR           ",color("RED", couleur_de_fond))
        decision =fenetre.get_wch()
        if (decision == " " and len(nom)>=1) or longueur==15:
            close_curses()
            return nom,fenetre
        else:
            l = recherche(liste,decision.lower())#on a créé une petite fonction de recherche en haut pour rechercher le caractère appuyé 
            if l!="":#par le joueur puis le valider.
                nom = nom + str(decision)#A chaque fois que le caractère inséré par le joueur est validé, on le rajoute à l'information 
                #à recueillir et on l'affiche automatiquement pour qu'il voit.
            else:
                longueur-=1
        longueur+=1

def init_colors() :
    """
    Initialisation des couleurs
    Valeur de retour :
    liste contenant le nom des couleurs et on index la couleur avec un code couleur tel que index = code couleur
    """
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    return["RED", "GREEN", "BLUE","YELLOW","CYAN","BLACK","MAGENTA"]

    #On a juste créé quelques animations ici pour mettre de la danse à l'écran 

def animation(type):
    i=0
    if type == 1:
        while i<100000:
            print("╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩")
            print("╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦ ╩ ╦")
            i+=1
    if type == 2:
        while i<100000:
            print("╚> <╝╚> <╝╚> <╝╚> <╝╚> <╝╚>")
            print("<╝ ╚><╝ ╚><╝ ╚><╝ ╚><╝ ╚><╝")
            i+=1
    if type == 3:
        while i<100000:
            print("1011010010101100010110101010110101")
            print("1001010110100101010011001101010110")
            i+=1
    if type == "lose":
        while i<100000:
            print("PERDU🥵")
            print("😭YOU LOSE😢")
            i+=1
    if type == "level2":
        while i<100000:
            print("💥Niveau 2")
            print("Level 2🔥")
            i+=1
    if type == "level1":
        while i<100000:
            print("🌝Niveau 1🫶🏻")
            print("😻Level 1🙎‍♂️")
            i+=1
    if type == "level3":
        while i<100000:
            print("Niveau 3🤭")
            print("👏Level 3")
            i+=1
    if type == "level4":
        while i<100000:
            print("🫣Niveau 4")
            print("Level 4😇")
            i+=1
    if type == "level5":
        while i<100000:
            print("Niveau 5🤩")
            print("🤓Level 5")
            i+=1
    if type == "fin":
        while i<200000:
            print("Bravo😍")
            print("The End")
            print("Fin")
            i+=1


def color(code, l_color):
    """
    Sélectionne une couleur
    code est le nom de la couleur que nous voulons rendre
    l_color : liste des couleurs
    Valeur de retour : code de couleur curses
    """
    return curses.color_pair(l_color.index(code) +1)

#En besoin, on a créé une fonction ralentisseur, un genre équivalent de asyncion.sleep() pour modérer l'évolution du jeu.

def ralentisseur(n):
    curses.napms(int((1000*n)//1))