Un double écran, deux serveurs X différents
###########################################

:tags: linux, ecran, x, xephyr, devilspie, astuce
:date: 2013-07-10 22:00:00
:blog:
:template: article.html

L'avantage de Linux c'est que l'on peut faire vraiment (ou presque) n'importe quoi. Ma dernière bidouille c’est l’affichage d’un second serveur X sur mon deuxième écran. L’intérêt (pour moi en tout cas) c’est d'avoir les avantages de Gnome-Shell et en parallèle un i3 pour le tilling et surtout pour finaliser la configuration du i3 pour éventuellement migrer complètement.

    .. image:: http://c4software.another-team.com/double.png

Pour faire simple la solution que j'ai utilisé c'est :

* Un lancement classique de Gnome-Shell via GDM.
* Lancement de i3 via Xephyr_
* Suppresion des bordures de la fenêtre de Xephyr avec Devilspie_

*Bien évidement la configuration fait référence à la résolution de mes écrans (1680x1050), Dans mon cas i3 s'affichera sur l'écran de droite qui a une résolution de 1680x1050*

Création du fichier de parametrage pour devilspie
=================================================

Fichier : ~/.devilspie/Xephyr.ds

.. code:: bash

    (if
        (is (window_class) "Xephyr")
        (begin
            (undecorate)
            (geometry "1680x1040+1680+0")
        )
    )

*Vous devez éditer la partie geometry pour l'adapter à votre configuration*

Script de lancement de la totalité
==================================

Fichier : ~/start.sh

.. code:: bash

    #!/bin/bash
    killall devilspie
    devilspie ~/.devilspie/Xephyr.ds &
    startx -- /usr/bin/Xephyr :1 -screen 1680x1050 -host-cursor 2> /dev/null &

Rien de bien révolutionnaire, mais j'ai mis pas mal de temps à trouver une solution stable et pratique pour avoir deux WM/DE en parallèle sur ma machine.

.. _Xephyr: http://www.freedesktop.org/wiki/Software/Xephyr/
.. _Devilspie: https://wiki.gnome.org/DevilsPie