Trackball Logitech Trackman Marble PS/2 : Ajouter la roulette et le clic central
################################################################################

:tags: Linux, Trackball, Xorg
:date: 2016-05-16 12:00:00
:blog:
:template: article.html

J'ai récemment fait l'acquisition d'une (un ?) trackball Logitech Trackman Marble, c'est un vieux
modèle au vu de la fiche Wikipedia il date de 1996, mais pour 2€ c'est vraiment une bonne affaire...  Enfin l'inconvénient d'avoir une souris aussi âgée c'est qu'elle ne possède pas de roulette, mais trois boutons
comme sur cette image :

.. image:: https://dl.dropboxusercontent.com/u/309501/Blog/Trackman/souris.jpg

Mais le gros avantage de Linux c'est que tout est configurable, donc aucun problème un petit fichier de configuration et ça roule.

Pour ajouter le support de la roulette et du clic central il vous suffit de créer le fichier
10-evdev.conf dans le bon dossier et c'est parti (pour Archlinux en tout cas, mais dans les autres distributions ça doit être sensiblement là même chose)

.. code:: bash

    $ cat /X11/xorg.conf.d/10-evdev.conf
    Section "InputClass"
        Identifier  "Logitech Trackball
        MatchProduct "PS/2 Logitech TrackMan"
        Option "EmulateWheel" "true"
        Option "EmulateWheelButton" "2"
        Option "Emulate3Buttons" "true"
    EndSection

Un petit reboot (où en redémarrant X11 à vous de voir) et vous pourrez scroller en laissant le bouton central enfoncé et en tournant la jolie boule rouge de votre trackball.
