Syncer, boostez vos transfert
#############################

:tags: outil, github, go
:date: 2015-09-20 12:00:00
:blog:
:template: article.html

En voilà une bonne idée !

De plus en plus d'outils utilisent des techniques de synchro partielles pour sauvegarder vos fichiers (Dropbox, BitTorentSync, etc…) mais il était pourt l'instant plutôt dificile d'utiliser ce genre de technique avec vos propres transferts de fichiers.

C'est maintenant fini ! À vous aussi les joies de la copie rapide ! Syncer_ est un outil écrit en Go qui fonctionne sur le même principe que BitTorrent Sync (enfin je crois). Pour faire simple au lieu de simplement copier vos fichiers l'outils lors de la première copie calcul un hash de chaque block des fichiers que vous souhaitez copier.

Via :

.. code:: bash

  % ./syncer -src /dev/ada0 -dst /dev/da0 -state state.bin
  [%%%%%%]
  # all blocks were transferred to da0

Puis lors de la prochaine copie, au lieu de copier l'intégralité des fichiers le même processus sera utilisé, mais ce coup-ci au lieux de tout copier (et c'est là que c'est vraiment cool) uniquement les blocks modifiés seront copiés vers la destination :

.. code:: bash

  % ./syncer -src /dev/ada0 -dst /dev/da0 -state state.bin
  [....%.]
  # only one block was transferred to da0

C'est aussi simple que ça! Personelement je trouve le truc vraiment génial ! Ça ouvre vraiment de bonne perspective surtout vu les débits plutôt misérable que l'on peu avoir en ADSL montant…

L'outil est open source et est écrit en Go, pour le `télécharger c'est par ici`_

.. _Syncer: https://github.com/stargrave/syncer
.. _télécharger c'est par ici: https://github.com/stargrave/syncer
