Linux et les dispositions de clavier personnalisées
###################################################

:tags: Linux, Clavier, Gnome-Shell
:category: Linux
:date: 2018-01-28 23:00:00
:blog:
:template: article.html

Salut,

Sous MacOs il est très simple de personnaliser une disposition clavier, il suffit en gros de déplacer un XML au bon endroit dans le système (root ou pas d'ailleurs) et votre disposition est disponible… Sous Linux c'est une autre pair de manche… Par défaut toutes les dispositions sont dans des fichiers « xkb » qui sont au niveau du système, donc ce sont des fichiers qui sont écrasés à chaque mise a jours.
Il n'est donc pas forcément simple de maintenir une disposition personnalisées dans un système qui se met a jours régulièrement (il existe des techniques à base de la commande « chatr », mais je ne suis pas fan de cette technique). Il est possible par contre de charger une disposition depuis un dossier (votre $HOME par exemple).

Sur ma distribution j'utilise Gnome-Shell, j'ai donc fait une « petite » extension qui se permet de charger une disposition personnalisées provenant du $HOME et surtout l'extension permet de restaurer la disposition après le déverrouillage du système (sinon de base votre disposition système est remise en place).

.. image:: https://github.com/c4software/xkbswitcher/raw/master/screen.png

Pour l'instant je ne l'ai pas publiée, elle est uniquement disponible sur mon compte GitHub. Je m'en sers maintenant depuis quelques temps sans soucis. Si vous aussi vous la voulez c'est `à télécharger ici <https://github.com/c4software/xkbswitcher/>`_.

Pour déclarer une disposition personnalisées il faut juste :

.. code-block:: shell 

    $ mkdir -p ~/.xkb/symbols/
    $ cp bepoDev.xkb ~/.xkb/symbols/

À partir de maintenant vous allez pouvoir l’utiliser dans votre système. Avec l’extension ou directement avec la commande :

.. code-block:: shell

    $ setxkbmap -I ~/.xkb bepoDev -print | xkbcomp -I$HOME/.xkb - $DISPLAY

Bonne bidouille !