Installer le VPN WireGuard sur la Freebox delta
###############################################

:tags: vpn, freebox, wireguard
:category: freebox
:date: 2019-01-05 15:00:00
:blog:
:status: draft
:template: article.html

Depuis maintenant quelques mois (`8 octobre 2019 <https://dev.freebox.fr/blog/?p=5450>`_) il est possible de créer des machines virtuelles sur la Freebox Delta. La puissance de la freebox est « limité » mais ça fonctionne très bien pour des service simple (Jeedom, PiHole, …) c'est sympa ça fonctionne très bien ! Mais il est possible de faire bien plus !

Le freebox dispose d'un serveur VPN integré, mais celui-ci utilise OpenVPN et pas le superbe `WireGuard <https://wireguard.com>`_! Maintenant qu'il est possible simplement d'héberger des machines vituelles nous pouvons monter ça en deux temps trois mouvement. Pour ceux qui n'ont jamais entendu parlé de WireGuard :

- Configuration « simple ».
- Integré dans le noyau Linux (en cours).
- Des clients pour les principaux OS.
- Une faible consommation de ressources.  

La manière la plus simple d'installer WireGuard (pour l'instant) est de passer par Ubuntu Server 19.10 (Eoan), WireGuard server est installable par un simple

.. code:: bash

    $ sudo apt-get install wireguard

Créer la VM sur la Freebox
--------------------------

Pour cette étape rien de bien compliqué, il suffit de suivre la procédure dans l'interface fourni par Free. En terme de ressources moi j'ai mis le « minimum » à savoir :

- 1 CPU.
- 384Mo de RAM.

En dessous c'était trop limite pour que Ubuntu fonctionne correctement.

Installation de WireGuard
-------------------------

Comme je le disais précédement installer WireGuard sur Ubuntu Eoan est aussi simple que d'ajouter VIM (oui, vous devriez l'installer également…), il suffit de :

.. code:: bash

    $ sudo apt-get install wireguard

Configurer WireGuard
--------------------

La configuration de Wireguard n'est pas vraiment compliqué, cependant il faut quand même passer par deux ou trois fichiers. J'ai donc fait un petit script qui simplifie la configuration (et le partage de la configuration avec vos clients mobiles).

Pour le script il est `disponible sur mon compte GitHub <https://github.com/c4software/WireGuard-cli>`_ pour qu'il fonctionne correctement vous pouvez installer également QREncode :

.. code:: bash

    $ sudo apt-get install qrencode

