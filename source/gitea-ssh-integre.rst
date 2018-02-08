Activer le serveur SSH intégré à Gitea
######################################

:tags: unix, git, gitea, bidouille, ssh
:category: Bidouille
:date: 2018-02-03 20:00:00
:blog:
:status: draft
:template: article.html

Le gros avantage des solution tout intégrée telle que Gitea (Gogs, ou GitLab, …) c’est la simplicité de mise en place. Un outil à lancer et hop ! C’est parti. 

Dans cet article, je vais détailler l’activation du serveur SSH intégré à Gitea, une fois actifs c’est Gitéa qui s’occupera de toutes les problématiques lié aux SSH pour pousser votre code sur votre serveur (échanges de clefs, port, etc).

L’ensemble de la configuration est dans le fichier « custom/conf/app.ini », de base il contient quelques éléments de la configuration mais pas l’ensemble (c’est d’ailleurs bien dommage…). Il suffit d’ajouter dans la section [server] la configuration suivante :

.. code-block:: ini 
    [server]
    [...]
    START_SSH_SERVER = true
    SSH_LISTEN_PORT  = 2222
    BUILTIN_SSH_SERVER_USER = "git"
    [...]

Redémarrer Gitea et normalement votre serveur écoute maintenant les nouvelles connexion sur le port 2222. Pour l’utiliser il faut bien évidement faire un échange de clefs SSH dans la configuration de votre compte sur l’interface Web de Gitea.
