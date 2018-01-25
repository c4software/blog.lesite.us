SSH Agent Forwarding : Garder votre identité de serveurs en serveurs
####################################################################

:tags: Linux, SSH, Agent, Key
:category: Linux
:date: 2018-01-25 21:00:00
:blog:
:template: article.html


Une note rapide pour vous partager une « découverte » récente, jusqu'à pas si longtemps j'avais le réflexe de générer une clef depuis le serveur de « rebond ». Je ne m'étais jamais posé la question, mais avec l'usage de plus en plus important que je fais avec ma Yubikey j'ai un peu étudié la question et il est possible de « propager » son identité grâce au SSH Agent Forwarding.

Pour l’activer c’est simple, il suffit d’ajouter dans votre fichie ~/.ssh/config la directive suivante :

.. code-block:: shell

    vim ~/.ssh/config
    ForwardAgent yes

Et voilà ! Vous pouvez vérifier que ça fonctionne en tappant ssh-add -L sur le serveur distant vous devriez voir votre clef publique.