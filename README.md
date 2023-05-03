Le dossier composant ce fichier README est le dossier principal qui héberge les différentes fonctions de notre RPG.
Veuillez le lire jusqu'à la fin pour comprendre comment ça marche.  

_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- Le contexte du Jeu -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
Mia est une jeune fille de 15 ans qui a s'est fait capturer par une ogre . La disparition de Mia éveil le village tout entier sur la menace qu'est cette Ogre
c'est alors que vous, en role du Cherif du village décide de se mettre à la poursuite de l'ogre .
En allant sa poursuite il rencontra beaucoup de difficultés sur sa route ce qui transformât sa poursuite en aventure pour retrouver les enfants disparus.")

---------------------------------------------------> Comment lancer le rpg? <---------------------------------------------------------

Importer d'abord tout le dossier comme espace de travail sur VS-code
Ouvrez le fichier .py intitulé lancer_le_jeu.py 
Ouvrir son terminal VS-code et s'assurer d'obtenir un terminal de plus de 43 lignes de hauteur et de 150 colonnes.
Autrement vérifiez d'avoir grandement ouvert le terminal et que les options de zoom ne sont pas à l'intant activées sur 
votre ordinateur(juste une précaution pour l'ouverture de la fenetre de jeu)
Interpreter le fichier lancer_le_jeu.py .(F5)
Suivez les consignes de chaque début de niveau et essayez de relever les défis jusquà la fin du jeu.

------------------------------------------------------> fonctionnalités <---------------------------------------------------------
Comme fonctionnalités, nous n'avons vraiment pas utilisé un logiciel d'interface graphique python mais nous avons amélioré la console avec
le module curses distribué avec python, ce qui vous réduit la tache d'importer tout un autre logiciel et de notre coté rend notre projet
plus fluide (avec ses fonctions pour changer de couleurs, avec ses systèmes de fenetres etc...).

Nous avons ajouté une petite boutique qui utilise le 3/4 de votre solde en argent pour vous recharger de vie en cas de manque, si c'est sec des deux cotés,
vous perdrez évidemment.

Les différentes tourches sur lesquelles taper à chaque moment,et vis-à-vis des enjeux,ces tourches doivent etre 
respectés pour continuer le jeu. Dans d'autre cas, l'enjeu de reprendre ou de perdre le jeu n'est vraiment pas de taille, donc soit on 
redirrige vers la bonne destination, soit on donne des chances de retaper. Ayant élaboré le menu de la page d'accueille et autres, il est 
nécessaire de savoir que durant tout le jeu, la touche Echape/Esc sert à quitter le jeu et la touche Espace sert redémarrer le jeu (sauf en cas de d'insertion du nom où elle sert à valider le pseudo)

Notre fonction d'insertion du nom au début est basé sur des retours touches sur curses,plusieurs tourches comme la suppression de caractère retournent
des fonctions, un type entre griffe non string ce qui laisse le fait qu'après insertion d'un caractère, plus de retour en arrière et qu'il faudra 
valider le nom avec le caractère espace (" ").

ATTENTION!
A noter que les tests et le jeu ont été fait sur un Mac, donc sur un Linux ou Windows nous ne savons
pas trop le comportement de ses touches mais vu la documentation du module curses, les nombres retournés pour les tourches sont basés sur
le code ASCI donc ça devrait aller sur tous les systèmes d'exploitation vu que c'est une convention universelle.


-----------------------------------------------------Les différents niveaux du jeu-------------------------------------------------------
Niveau 1: Ce niveau consiste à trouver la réponse à l'énigme posée par l'arbre de la foret qui est un grant serre majestieux. 
En temps que sauveur du village, les esprits doivent tester votre capacité d'assurer cette mission qui vous est imposée.

Niveau 2: Ce niveau consiste à trouver réponse à une équation posée par les nains de la foret. 
Cette solution dans l'idée du jeu est l'année où a lieu le premier enlèvement d'enfants par l'orgre dans ce village. 
Non seulement ça, c'est son équivalence en hexadécimal qui est le code d'identification du pistolet du chérif à utiliser 
pour activer ce pistolet et l'utiliser pour se défendre contre l'orgre. Pour gagner le niveau, vous devez donc trouver ce code pour
débloquer le niveau qui suit.

Niveau 3: Ce consiste à rechercher des clés de chambre et de la lumière à l'aide du perroquet mystique jusqu'à se dirriger vers
la résidence de l'orgre pour le combatre dans le 4ème niveau.

Niveau 4: Ce niveau est un niveau de combat qui consiste à affronter un orgre au moyen des coups de poing.
A chaque coup donné, l'orgre également réplique. On a fallu utiliser un randint pour compter les coups de points donnés car
avec un système non aléatoire il aurait toujours le même gagnant puisque le coup ne varie alors que ce qui rend un jeu jouable est la perte.
Le joueur ne gagnerait un certain nombre de points dans ctte partie qu'en donnnant un coup plus fort à l'orgre que lui n'en lui donne. C'est
juste pour le féliciter du fait qu'il a été pu réduire la puissance de l'orgre avec ses coups.


Niveau 5: Ce niveau est un labyrinthe et consiste au joueur à sortir du labyrinthe en vie. En passant,
il a la possibilité de prendre des points représentés par "€" et de surtout éviter les ennemis "✘" en couleurs rouges.
Les points/argents dans cette partie lui serviront de pièces pour payer à la boutique des vies en cas de manque de vie. C'est une façon 
de faire pour lui permettre d'utiliser ses pièces pour se réanimer. Autant pour un joueur de ne pas négliger ces pièces car c'est un labyrinthe
peu complexe. La sortie de ce labyrinthe est là où se trouve les enfants à récupérer.
