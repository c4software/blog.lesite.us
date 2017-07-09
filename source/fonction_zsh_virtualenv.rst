Zsh : Une fonction pour démarrer vos virtualenv
#################################################

:tags: zsh, virtualenv
:date: 2013-03-15 23:10:00
:blog:
:template: article.html

Quand  je fais du python j'utilise énormément de virtualenv (je pense que je ne suis pas le seul). Les virtualenv's c'est vraiment génial (oui oui vraiment) ça évite de polluer son système avec plein de dépendances diverses qui sont au final utile que dans un seul projet. Le seul "petit" soucis avec les virtualenv c'est qu'il faut utiliser la commande source pour les démarrer exemple :

.. code:: bash

	➜ ~ source python/mon_super_virtualenv/bin/activate

Ce n'est pas vraiment long, mais quand on multiplie par quatre ou cinq virtualenv par jour c'est plutôt pénible (même si avec l'historique des commandes -ctrl+r- c'est assez rapide). L'idée de départ c'est de simplifier l'activation du virtualenv avec une petite fonction sympathique dans mon **.zshrc**:

.. code:: bash

	function workon() {
		source ~/python/$1/bin/activate
	}


Après pour l'utilisation rien de plus simple :

.. code:: bash
	
	➜ ~ workon mon_super_virtualenv
	(mon_super_virtualenv)➜ ~ 

[Edit] Et pour ceux qui souhaitent encore plus, FreakyNadley_ m'a remonté l'existence de virtualenvwrapper_ :)

.. _FreakyNadley: https://twitter.com/FreakyNadley
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/