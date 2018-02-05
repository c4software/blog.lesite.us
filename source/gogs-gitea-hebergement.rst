Installer Gitea (ou Gogs) sur un NAS Synology
#############################################

:tags: unix, git, synology, bidouille
:category: Bidouille
:date: 2018-02-03 20:00:00
:blog:
:template: article.html

On est tous d’accord le versionning c’est hyper important (oui même pour un projet perso). On peu utiliser GitHub ou GitLab (ou autre d’ailleur) mais si on à la chance d’avoir un « serveur » à la maison on peu faire mieux, héberger les sources à domiciles.

Pour rappel Gitea (Gogs) c’est un équivalent de GitHub (ou GitLab), mais beaucoup plus simple et surtout très légé au niveau des ressources système.

Ici on va s’intéresser à l’installation de Gogs ou Gitea sur un NAS Synology (DSM 6). Le système synology embarque un système de paquet, mais pour une raison que j’ignore impossible de faire fonctionner correctement le paquet Gitea sur mon DS-216+II, le paquet s’install mais ne se lance pas correctement… J’ai donc pris un peu de temps pour configurer moi même le services et au final c’est pas très compliqué, et pour ceux qui ont peurs de la ligne de commande on peu faire sans.

Le binaire
----------

La première étape c’est la récupération du binaire de Gitea qui correspond au processeur de votre NAS, par exemple :

- DS218+II : linux-amd64
- DS217J : linux-arm-7

Le binaires sont tous disponibles sur le `GitHub de Gitea <https://github.com/go-gitea/gitea/releases>`_, télécharger celui qui correspond à votre processeur et garder le sur votre ordinateur.

1. Préparation du NAS
---------------------

Sur le NAS deux options :

- Utiliser un compte existant.
- Créer un nouveau compte.

La vous avez le choix, dans tous les cas je vous conseils juste de ne pas lancer Gitea avec un compte administrateur… Juste au cas ou !

2. « Installation » et configuration
-------------------------------------

Pour installer Gitea il faut juste lancer le binaire avec le paramètre « Web », c’est donc vraiment très simple ! Le soucis par contre c’est que le programme garde la main (étrange je trouve pour ce genre de service…). Il faut donc un petit script qui se chargera de lancer Gitea et de le mettre en arrière plan.

J’ai donc fait un petit script qui va permettre de lancer (et d’arrêter Gitea), le script est `téléchargeable ici <https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/startup_gitea.sh>`_ un fois télécharger copier le dans le même dossier que Gitea sur votre NAS.

Vous devez donc avoir quelques choses comme :

.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/structure.png

Maintenant que tout est sur le NAS, nous allons éditer la configuration du script. Il faut donc remplacer les 2 variables en haut du fichier par les valeurs correspondants à votre configuration. Dans mon cas :

.. code-block:: shell 

    GITEA_ROOT="/var/services/homes/gitea/gitea/"
    GITEA_USER="gitea"


Voilà. Votre script est prêt à être utilisé.

3. Démarrage et Arrêt automatique
----------------------------------

Maintenant que tout est prêt, nous allons mettre en place les deux « tâches » dans le « Planificateur de tâches » du NAS :

⚠️ Le script de démarrage doit être lancé en root.

.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/creation.png
.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/creation2.png
.. image:: https://raw.githubusercontent.com/c4software/dotfiles/master/gitea/images/creation3.png
