import niveau_combat
import le_modul_curses
import numero_de_niveau
import netoyeur_d_ecran as cleaner
from os import _exit as sortie
def combat_ogre(infos,Indicateur_de_récursion,Indicateur_de_récursion2) :
    # Créer un ogre et un héros

    ogre = {'health': 100}
    hero = {'health': infos["pv"]}#l'hero, c'est sans doute le joueur
    win= le_modul_curses.fenetre(35,120,[2,5])
    couleur=le_modul_curses.init_colors()
    win.addstr(2, 1,"Prêt pour commencer ?",le_modul_curses.color("GREEN", couleur))

    le_modul_curses.animation("level4")
    win.erase()
    le_modul_curses.close_curses()
    # Faire combattre l'ogre et le héro
    window,i=niveau_combat.fight(hero, ogre,Indicateur_de_récursion,Indicateur_de_récursion2,infos)


    numero_de_niveau.barre_score(infos,window,couleur)
    # Afficher le gagnant

    if niveau_combat.is_alive(ogre):
        window.addstr(i+2, 50,"Vous avez perdu!😔",le_modul_curses.color("RED", couleur))
        window.get_wch()
        le_modul_curses.animation("lose")
        le_modul_curses.close_curses()
        cleaner.efface_ecran()
        sortie(1)
    else:
        #Juste un petite confirmation, une condition forte au cas où quoi.
        if niveau_combat.is_alive(hero):
            infos["pv"]=25
            window.addstr(i+4, 22,"                               Vous avez Gagné😍!                           ",le_modul_curses.color("GREEN", couleur))
            window.addstr(i+14, 22,"                    👉Veuillez <Entrer> pour continuer👈                     ",le_modul_curses.color("MAGENTA", couleur))
            window.addstr(i+8, 22,"   Le plan qui suit est celui de la forêt où l'orgre a caché les enfants 👩‍👧‍👦.",le_modul_curses.color("CYAN", couleur))
            window.addstr(i+10, 22,"Prenez le maximum d'argent💰 que vous aurez et évitez les disciples de l'ogre🫥",le_modul_curses.color("BLUE", couleur))
            window.addstr(i+12, 22,"            🥳Retrouvez la sortie pour récupérer les enfants.               ",le_modul_curses.color("CYAN", couleur))
            window.get_wch()
            le_modul_curses.animation("level5")
            window.erase()

