from random import randint
import os as sortie
import netoyeur_d_ecran as chiffon
import le_modul_curses as interface
import bienvenue as recommencer
from numero_de_niveau import mini_barre_score as barre


items = {"Lighter": randint(1,2), "Key": randint(1,2)}

def game():
    fenetre=interface.fenetre(35,120,[2,5])
    couleur_de_texte=interface.init_colors()
    barre(3,fenetre,couleur_de_texte)
    fenetre.addstr(3,4,"🙁 It is STRONGLY RECOMMENDED to play the level without help or guide. Each death should serve as a lesson to you.",interface.color("CYAN",couleur_de_texte))
    fenetre.addstr(6,4,"This game with the end objective of reaching Door 4 in the third Room you should  try to kill you as player the ",interface.color("CYAN",couleur_de_texte))
    fenetre.addstr(9,4,"monster RUSH . Once player enter to the first Room he must search the key to unlock the next door. The rest of ",interface.color("CYAN",couleur_de_texte))
    fenetre.addstr(12,4,"          the game is progressing by entering the following doors where you gonna search the Lighter.          ",interface.color("CYAN",couleur_de_texte))
    fenetre.addstr(16,4,"        🤜 Then, you encounter the monster RUSH (Agent of the Ogre) who appears in the third Room 💀👻👽         ",interface.color("CYAN",couleur_de_texte))
    fenetre.addstr(19,2,"     👉 Please press <Enter> or <Return> to continue or <Echappe> to quit the game or <Space> to restart. 👈      ",interface.color("YELLOW",couleur_de_texte))
    decision =fenetre.getch()
    while decision!=10 and decision!=27 and decision!=32 :
        decision =fenetre.getch()
    if decision == 10 :
        fenetre.addstr(19,2,"                          Welcome to this level, be strong enough good luck 😃                                    ",interface.color("BLUE",couleur_de_texte))
        fenetre.addstr(21,2,"                 You're in the first Room , Rush is an entity that resides in this Hotel🎃.                        ",interface.color("YELLOW",couleur_de_texte))
        fenetre.addstr(23,2,"            It serves as the most frequent threat in the Hotel. First you should find the key🔑.                   ",interface.color("YELLOW",couleur_de_texte))
        fenetre.addstr(27,2,"                                     😍 Please press <Enter> to continue.                                        ",interface.color("MAGENTA",couleur_de_texte))
        fenetre.getch()
        search_key(2)
        return
    elif decision==27 :
        interface.close_curses()
        sortie._exit(1)
    elif decision==32 :
    # C'est la touche pour recommencer le jeu(la touche <espace>)
        recommencer.bienvenue1()
        chiffon.efface_ecran()
        sortie._exit(1)#Pour arreter tous les processus en cours pour qu'après ils ne se réexecutent pas lorsque jeu serait terminé(Juste pour etre sûr).

#les signaux sont mis juste pour faire varier l'affichage à chaque échec d'éssai
def search_key(signal):
    fenetre=interface.fenetre(35,120,[2,5])
    couleur_de_texte=interface.init_colors()
    barre(3,fenetre,couleur_de_texte)
    if items["Key"]== 1:
        fenetre.addstr(15,4,"                                          You opened the Door 😊 Now.                         ",interface.color("CYAN",couleur_de_texte))    
        fenetre.addstr(16,4,"                                    You can now acceess to the next Room 🚶‍♂️.                     ",interface.color("CYAN",couleur_de_texte))
        fenetre.addstr(17,4,"                                 In this Room you have to search the Lighter.                    ",interface.color("CYAN",couleur_de_texte))
        fenetre.addstr(20,4,"                    I know it's difficult but you should try and retry again so good luck 😃      ",interface.color("YELLOW",couleur_de_texte))
        fenetre.addstr(27,4,"                                       Please press <Enter> to continue.                                        ",interface.color("MAGENTA",couleur_de_texte))
        fenetre.getch()
        search_lighter(2)
        return
    elif items["Key"] != 1:
        fenetre.addstr(signal+17,2,"                          Oh NO😪! Press <Enter> to retry, maybe you can find it now🫣.                               ",interface.color("RED",couleur_de_texte))
        decision =fenetre.getch()
        while decision!=10 and decision!=27 and decision!=32 :
            decision =fenetre.getch()
        if decision == 10 :
            items["Key"]=randint(1,2)
            search_key(signal-1)
        elif decision==27 :
            interface.close_curses()
            sortie._exit(1)
        elif decision==32 :
        # C'est la touche pour recommencer le jeu(la touche <espace>)
            recommencer.bienvenue1()
            chiffon.efface_ecran()
            sortie._exit(1)#Pour arreter tous les processus en cours pour qu'après ils ne se réexecutent pas lorsque jeu serait terminé(Juste pour etre sûr).


def search_lighter(signal):
    fenetre=interface.fenetre(35,120,[2,5])
    couleur_de_texte=interface.init_colors()
    barre(3,fenetre,couleur_de_texte)
    if items["Lighter"] == 1:
        fenetre.addstr(15,4,"                                That cool you did it now light it on 🫡                     ",interface.color("CYAN",couleur_de_texte))    
        fenetre.addstr(17,10,"You entered inside the room where RUSH😱 appears wish you good luck to the fighting 🫣",interface.color("YELLOW",couleur_de_texte))    
        fenetre.addstr(27,4,"                                   Please press <Enter> to continue.                    ",interface.color("MAGENTA",couleur_de_texte))
        fenetre.getch()
        monster(2)
        return
    elif items["Lighter"] != 1:
        fenetre.addstr(signal+17,2,"                          Oh NO😪! Press <Enter> to retry, maybe you can find it now🫣.                               ",interface.color("RED",couleur_de_texte))
        decision =fenetre.getch()
        while decision!=10 and decision!=27 and decision!=32 :
            decision =fenetre.getch()
        if decision == 10 :
            items["Lighter"]=randint(1,2)
            
            search_lighter(signal-1)
        elif decision==27 :
            interface.close_curses()
            sortie._exit(1)
        elif decision==32 :
        # C'est la touche pour recommencer le jeu(la touche <espace>)
            recommencer.bienvenue1()
            chiffon.efface_ecran()
            sortie._exit(1)#Pour arreter tous les processus en cours pour qu'après ils ne se réexecutent pas lorsque jeu serait terminé(Juste pour etre sûr).



def monster(signal):
    fenetre=interface.fenetre(35,120,[2,5])
    couleur_de_texte=interface.init_colors()
    barre(3,fenetre,couleur_de_texte)
    power = randint(0,1)
    if power == 1:
        fenetre.addstr(15,4,"                😍Fine you win! Now you have to open the next where is the General Ogre       ",interface.color("GREEN",couleur_de_texte))    
        fenetre.addstr(27,4,"                                       Please press <Enter> to continue.       ",interface.color("MAGENTA",couleur_de_texte))
        fenetre.getch()
        return
    elif power != 1:
        fenetre.addstr(signal+15,4,"                             🤧You didn't kill the monster to who you call RUSH...                  ",interface.color("BLUE",couleur_de_texte))    
        fenetre.addstr(signal+16,4,"              You must run away from it! However, it may appear in front of you at any time.       ",interface.color("BLUE",couleur_de_texte))
        fenetre.addstr(signal+17,4,"                                    So fight again untill you kill him 🥲.                         ",interface.color("BLUE",couleur_de_texte))
        fenetre.addstr(signal+27,4,"                                       Please press <Enter> to continue.                                        ",interface.color("MAGENTA",couleur_de_texte))
        fenetre.addstr(signal+17,2,"  ",interface.color("RED",couleur_de_texte))
        decision =fenetre.getch()
        while decision!=10 and decision!=27 and decision!=32 :
            decision =fenetre.getch()
        if decision == 10 :
            monster(signal-1)
            return
        elif decision==27 :
            interface.close_curses()
            sortie._exit(1)
        elif decision==32 :
        # C'est la touche pour recommencer le jeu(la touche <espace>)
            recommencer.bienvenue1()
            chiffon.efface_ecran()
            sortie._exit(1)#Pour arreter tous les processus en cours pour qu'après ils ne se réexecutent pas lorsque jeu serait terminé(Juste pour etre sûr).





