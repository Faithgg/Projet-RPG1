import le_modul_curses
from random import randint
import os
import numero_de_niveau
import bienvenue as recommencer

# Fonction qui retourne si un personnage est en vie ou non
def is_alive(character):
  if character['health'] > 0 :
    return True
  else :
    return False


# Fonction qui simule un tour de combat entre deux personnages
def fight(character1, character2,indicateur_de_récursion,Indicateur_de_récursion2,infos):
  window = le_modul_curses.fenetre(35,120,[2,5])
  couleur=le_modul_curses.init_colors()
  #numero_de_niveau.barre_score(infos,window,couleur)
  if indicateur_de_récursion !=1 :
    
    window.addstr(2, 27,"Combat nul <sans gagnant!>.Veuillez rejouer en continuant.",le_modul_curses.color("BLACK", couleur))

  window.addstr(3, 20,"🥱Vous allez jouer cette partie avec vos tourches <Tab> et <Entrer>😏",le_modul_curses.color("BLUE", couleur))
  window.addstr(5, 20,"   🫣 Appuyez sur <Tab> pour reculer et <Entrer> pour Attaquer.  😉",le_modul_curses.color("CYAN", couleur))
  i=7
  while is_alive(character1) and is_alive(character2):
    if infos["pv"]>0 and character2["health"]> 0:
      if len(str(infos["pv"])) == 2 :
        if Indicateur_de_récursion2 == 0 :
          window.get_wch()
          Indicateur_de_récursion2 =1
          window.erase()
          le_modul_curses.close_curses()
          fight(character1, character2,indicateur_de_récursion,Indicateur_de_récursion2,infos)
          break
        #J'ai mis ces break après l'appelation des fonctions car j'ai constaté qu'après après appel comme pour tout autre fonction
        #l'ancienne boucle continue sa tournue, ce qui dans ce cas-ci compromet les calculs d'où je l'achève automatiquement.
      if len(str(infos["pv"])) ==1 :
        if Indicateur_de_récursion2 == 1 :
          Indicateur_de_récursion2 =2
          window.erase()
          le_modul_curses.close_curses()
          fight(character1, character2,indicateur_de_récursion,Indicateur_de_récursion2,infos)
          break
  
      numero_de_niveau.barre_score(infos,window,couleur)
      decision=window.getch()
      # Afficher le début du tour de combat
      if decision== 9:
        #A chaque recule, l'orgre lui inflige un petit coup 🤓
        coup = randint(1,4)
        infos["pv"] = infos["pv"] - coup
        window.addstr(i, 10,"L'orgre vous inflige " + str(coup) +" dégâts.",le_modul_curses.color("YELLOW", couleur))
        window.addstr(i, 80,"VOUS: " + str(infos["pv"])+ " ♥",le_modul_curses.color("RED", couleur))
      elif decision == 10 :
      #A chaque attarque il file un gros/petit coup à l'orgre
        coups = randint(7,15)
        character2['health'] = character2['health'] - coups
        window.addstr(i, 10,"Vous attaquez l'orgre avec " + str(coups)+ " coups",le_modul_curses.color("GREEN", couleur))
        window.addstr(i, 80,"Ogre: " + str(character2['health']) + " ♥",le_modul_curses.color("MAGENTA", couleur))
        passage1=1
        #A chaque attarque différent de la dernière qui le tue,l'orgre l'attarque aussi.
        if is_alive(character2):
          coup = randint(7,15)
          infos["pv"] = infos["pv"] - coup
          window.addstr(i+1, 10,"L'orgre replique avec " + str(coup)+ " coups",le_modul_curses.color("MAGENTA", couleur))
          window.addstr(i+1, 80,"VOUS: " + str(infos["pv"]) + " ♥",le_modul_curses.color("GREEN", couleur))
          passage1 =2
          i+=1
        if passage1==1 :
          window.addstr(i+2, 30,"Tapez <Entrer> pour continuer",le_modul_curses.color("YELLOW", couleur))
          window.get_wch()
          break
        if coups > coup :
          infos["po"]+= 5

        #Respectons toujopurs notre règle d'échappe pour fermer la partie
      elif decision==27 :
        le_modul_curses.close_curses()
        os._exit(1)
      elif decision==32 :
        # C'est la touche pour recommencer le jeu(la touche <espace>)
        recommencer.bienvenue1()
        os._exit(1)#Pour arreter tous les processus en cours pour qu'après ils ne se réexecutent pas lorsque jeu serait terminé(Juste pour etre sûr).
    else:
      break
    i+=1
  return window,i #Je retourne un tuple pour permettre à l'afficheur de rspecter le numéro de la dernière ligne qui porte un texte
  #afin qu'il y ait pas de perte d'information ou de superposition de phrase sur une meme ligne puisqu'on a retourné la meme fenetre.
    
