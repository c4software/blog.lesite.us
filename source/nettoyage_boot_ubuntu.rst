[Ubuntu] Nettoyer le /boot
##########################

:tags: Ubuntu, nettoyage, boot
:date: 2012-11-30 19:42:00
:blog:
:template: article.html

J'ai depuis quelques temps un grand mystère (récurrent) sur ma Ubuntu Server... Le MANQUE DE PLACE sur la partition /boot. C'est l'installation par défaut de Online_ certes.... Mais ce que je ne comprend pas c'est pourquoi le **apt-get upgrade**; j'ai chercher plein de solutions différentes, mais au bout d'un moment je me retrouve toujours avec le /boot plein.

Donc, après quelques recherches je suis tombé sur THE commande, une petite boucle sympatique qui supprime tous les Kernels qui ne sont plus utiles sur la machine :

	>>> dpkg --get-selections|grep 'linux-image*'|awk '{print $1}'|egrep -v "linux-image-$(uname -r)|linux-image-generic" |while read n;do apt-get -y remove $n;done

Pour l'utiliser rien de plus simple il suffit de se mettre en root et de la lancer. :).

Source_

.. _Online: http://www.online.net
.. _Source: http://ubuntuforums.org/showthread.php?t=1435818#5