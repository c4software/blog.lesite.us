Installer Archilnux sur un Dell XPS 2017 (Remplacer Ubuntu)
###########################################################

:tags: Archlinux, Dell, XPS
:category: Archlinux
:date: 2018-01-21 21:00:00
:blog:
:template: article.html

J’ai récemment eu une nouvelle machine (changement professionnel) cette machine est un [DELL XPS 9360 (de 2017) fourni avec Ubuntu](http://www.dell.com/en-us/shop/dell-laptops/xps-13-laptop/spd/xps-13-9360-laptop). C’est vraiment une superbe machine un 13 pouces dans un gabarit d’un 11… Bref génial !

La machine est livrée avec Ubuntu 16.04 LTS, ça fonctionne… mais je ne suis vraiment pas fan d’Ubuntu (exemple Out Of The Box unity plante régulièrement sans raison…) ! Donc migration sous Archlinux rien de bien particulié pour l’installation, c’est une machine avec de l’UEFI j’ai donc décidé de faire un petit article récap pour lister les différentes étapes clef de l’installation :

- [Téléchargement de l’ISO](https://www.archlinux.org/download/).
- Dans l’UEFI de la machine désactiver le secureboot (F12 au démarrage).
- Choisir la clef USB sur laquelle l’ISO à été « copié ».


Je vous conseil une fois booté de lancer le service SSH pour faire l’installation depuis une autre machine (ça permet de copier les commandes) :

.. code-block:: shell

    # Clavier
    loadkeys fr-bepo

    # Pour autoriser la connexion le compte Root doit avoir un mot de passe.
    $ passwd
    $ systemctl start sshd.service

    # Connexion au Wifi
    wifi-menu

    # Avoir votre IP
    $ ip addr


Pour la suite vous pouvez continuer depuis une autre machine

.. code-block:: shell

    $ ssh root@ip.de.votre.machine