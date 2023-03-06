import sys
import os

def efface_ecran() :
    """
    Efface l’écran de votre console peu importe le système d'exploitation que vous utiliserez pour tester notre projet.
    """
    if sys.platform.startswith("win") :
    # Si système Windows
        os.system("cls")
    else :
    # Si système Linux ou OS X
        os.system("clear")

