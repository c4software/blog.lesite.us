Synology, veilles de disques et Gitea
#####################################

:tags: nas, gitea, disque, veille
:category: Bidouille
:date: 2018-02-09 20:00:00
:blog:
:template: article.html


Cet article est le dernier d’une série de 3 articles détaillant `l’installation <installer-gitea-ou-gogs-sur-un-nas-synology.html>`_ / `la configuration <activer-le-serveur-ssh-integre-a-gitea.html>`_ / `l’optimisation de Gitea sur un Nas Synology <synology-veilles-de-disques-et-gitea.html>`_.

Les Nas Synology sont relativement très silencieux quand les disques sont arrêtés, j'aime l'idée d'avoir un Nas qui fonctionne en permanence, mais je ne veux pas que les disques fonctionnent en permanence (la conso, le bruit etc). Sur les systèmes Synology il est parfois difficile de garder le système en veille, c'est un vrai problème… chaque paquet en plus peut provoquer des soucis de mise en veille.

La configuration par défaut de Gitea empêche la mise en veille, j'ai cherché un moment pourquoi… Et la réponse est relativement simple c'est les logs ! Le démon Gitea ouvre les fichiers sur disques et les gardes ouverts en permanence ce qui bloque la mise en veille des disques. Pour remédier à cela il faut éditer le « custom/conf/app.ini » pour ajouter **dans** la section [log] la configuration suivante :

.. code-block:: ini 

    [log]
    MODE      = console
    LEVEL     = Error

Redémarrer Gitea, vos disques devraient maintenant passer en veille, attention tout de même après cette modification vous n’avez plus de logs sur disque.

Cet article fait parti d’une série de trois articles :

- `Héberger Gitea sur un Nas Synology <installer-gitea-ou-gogs-sur-un-nas-synology.html>`_
- `Activer le serveur SSH Intégré <activer-le-serveur-ssh-integre-a-gitea.html>`_
- `Retrouver la mise en veille des disques avec Gitea en service <synology-veilles-de-disques-et-gitea.html>`_