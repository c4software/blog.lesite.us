Installer Gitea (ou Gogs) sur un NAS Synology
#############################################

:tags: unix, git, synology, bidouille
:category: Bidouille
:date: 2018-02-03 20:00:00
:blog:
:status: draft
:template: article.html

On est tous d'accord le versioning c'est hyper important (oui même pour un projet perso). Le plus simple c’est d’utiliser les services dans le cloud type GitHub ou GitLab (ou autre d'ailleurs) mais si on a la chance d'avoir un « serveur » à la maison on peut faire mieux « héberger les sources à domiciles ».

Pour faire ça plusieurs solutions existent, installer un simple service SSH et faire du Git dessus, installer la machine de guerre GitLab à la maison, ou se tourner vers quelques choses de minimaliste j'ai nommé Gitea ( fork de Gogs). C'est donc un équivalent de GitHub (ou GitLab), mais beaucoup plus simple et surtout très léger au niveau des ressources système.

Ici on va s'intéresser à l'installation de Gogs ou Gitea sur un NAS Synology (DSM 6.2). Le système Synology embarque un système de paquet, mais pour une raison que j'ignore impossible de faire fonctionner correctement le paquet Gitea sur mon DS-216+II le paquet s'installe, mais ne se lance pas correctement… J'ai donc pris un peu de temps pour créer et configurer moi-même le service et au final ce n'est pas vraiment compliqué et pour ceux qui ont peurs de la ligne de commande on peut faire sans.

1. Le binaire
-------------

La première étape c’est la récupération du binaire de Gitea qui correspond au processeur de votre NAS, par exemple :

- DS218+II : linux-amd64
- DS217J : linux-arm-7

Le binaires sont tous disponibles sur le `GitHub de Gitea <https://github.com/go-gitea/gitea/releases>`_, télécharger celui qui correspond à votre processeur et garder le sur votre ordinateur.

2. Préparation du NAS
---------------------

Sur le NAS deux options :

- Utiliser un compte existant.
- Créer un nouveau compte.

Vous avez le choix, dans tous les cas je vous conseille juste de ne pas lancer Gitea avec un compte administrateur… Juste au cas ou ! Moi dans mon cas j'ai pris l'exemple d'un compte nommé «gitea »

3. « Installation » et configuration
-------------------------------------

Pour installer Gitea il faut juste lancer le binaire avec le paramètre « Web », c’est donc vraiment très simple ! Le soucis par contre c’est que le programme garde la main (étrange je trouve pour ce genre de service…). Il faut donc un petit script qui se chargera de lancer Gitea et de le mettre en arrière plan.

J’ai donc fait un petit script qui va permettre de lancer (et d’arrêter Gitea), le script est `téléchargeable ici <https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/startup_gitea.sh>`_ un fois téléchargé copiez le dans le même dossier que Gitea sur votre NAS.

Vous devez donc avoir quelques choses comme :

.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/structure.png

Maintenant que tout est sur le NAS, nous allons éditer la configuration du script. Il faut donc remplacer les deux variables en haut du fichier par les valeurs correspondants à votre configuration. Dans mon cas :

.. code-block:: shell 

    GITEA_ROOT="/var/services/homes/gitea/gitea/"
    GITEA_USER="gitea"

️️⚠️ Vous pouvez avoir le chemin dans les propriétés de l’un des deux fichiers.

Voilà! Le script est maintenant prêt à être utilisé.

4. Démarrage et Arrêt automatique
----------------------------------

Maintenant que tout est prêt, nous allons mettre en place les deux « tâches » dans le « Planificateur de tâches » du NAS :

⚠️ Le script de démarrage doit être lancé en root.

.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/creation.png
.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/creation2.png
.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/creation3.png

5. Démarrer manuellement le service
-----------------------------------

Maintenant que tout est prêt nous pouvons lancer le service, une fois lancé vous allez pouvoir configurer votre instance Gitea en allant sur :

http://ip.de.votre.nas:3000

À partir de maintenant vous êtes dans Gitea, personnellement je l’ai configuré en mode SQLite pour tester le service c’est bien. 

6. La suite…
-------------

Voilà votre service Git est fonctionnel. Cependant, de base vous n’allez pas pouvoir cloner en SSH facilement. Dans un prochain article je vais détailler l’activation du serveur SSH intégré.

Cette article fait parti d’une série de trois articles :

- `Activer le serveur SSH Intégré <#>`_
- `Retrouver la mise en veille des disques avec Gitea en service <#>`_