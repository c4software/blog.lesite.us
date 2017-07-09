MacOS: Désactiver les .DS_Store sur le réseau
#############################################

:tags: Réseau, ds_store, osx, partage
:date: 2017-07-09 22:09:00
:blog:
:template: article.html

Rien de plus chiant sous MacOs que les fichiers « .DS_Store » à défaut de pouvoir les retirer complètement il est possible de désactiver l’écriture des fichiers sur les disques réseaux :

.. code:: bash

  sudo defaults write /Library/Preferences/com.apple.desktopservices DSDontWriteNetworkStores -string true


Pour la disparition complète des fichier il faudra attendre APFS et High Sierra (Enfin il me semble…)
