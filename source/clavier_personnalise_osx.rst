El Capitan : Personnaliser la disposition de clavier du « Login screen »
########################################################################

:tags: OSX, Clavier, Bépo, ElCapitan, bidouille
:date: 2016-07-11 23:00:00
:blog:
:template: article.html

Vu que maintenant je saisie au clavier exclusivement en bépo, je souhaite que celui-ci soit disponible dans l'intégralité de mon système.

Sous OSX cette intégration est presque parfaite, il est possible de mettre (sans bidouiller) une disposition de clavier complètement personnalisé dans le système. Cependant, pour une raison qui m'échappe, au niveau du « login screen » il est impossible de choisir une disposition de clavier autre que celle fourni de base par le système, mais par chance une parade existe :

Après avoir choisi sur votre utilisateur la disposition voulue il suffit de passer les commandes suivantes dans un terminal :

.. code:: bash

	sudo cp ~/Library/Preferences/com.apple.HIToolbox.plist /Library/Preferences/
	sudo chmod 644 /Library/Preferences/com.apple.HIToolbox.plist

Après un redémarrage ça devrait être OK!
