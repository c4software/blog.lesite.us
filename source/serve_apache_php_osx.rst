Installer PHP sur OSX via Brew.sh
#################################

:tags: osx, Apache, Brew
:date: 2016-05-16 13:00:00
:blog:
:template: article.html

Vu que j'ai récemment « switché » sous osx pour des besoins pro, je suis actuellement en quête de tous les outils que j'utilisais au jour le jour sur ma Archlinux.

La combinaison de base que j'utilise quasi journalièrement c'est Apache et PHP. Pour Apache pas vraiment de problème c'est intégré dans OSX, attention, depuis la dernière version plus de menu pour le démarrer, mais un simple :

Démarrer Apache :

.. code:: bash

    $ sudo apachectl start

Stopper Apache :

.. code:: bash

    $ sudo apachectl stop


suffira à résoudre le problème.

Le point le plus embêtant c'est que de base la version de PHP n'est pas dutout à jour, et ça pour le coup c'est un problème impossible pour moi de coder en PHP sans avoir à minima la dernière version 5.6 (pour la 7 c'est également possible sans soucis). Pour installer PHP rien de plus simple il suffit d'activer quelques repo dans Brew et d'activer le module dans la conf de PHP (pour l'installation de `brew.sh`_ je vous laisse allez voir `le site officiel`_ c'est vraiment tout simple).


.. code:: bash

    $ brew tap homebrew/dupes
    $ brew tap homebrew/versions
    $ brew tap homebrew/homebrew-php
    $ brew install php56

Et voilà PHP 5.6 est installé sur votre machine, cependant pour l'instant votre Apache ne le connait pas... Pour ajouter le support du PHP il vous suffit d'éditer

.. code:: bash

    $ vim /etc/apache2/httpd.conf

et après le dernier LoadModule ajouter :

.. code:: bash

    LoadModule php5_module /usr/local/opt/php56/libexec/apache2/libphp5.so

et maintenant il faut activer le support du PHP pour les extensions de type .php pour ça trouvez la directive :

.. code:: bash

    <FilesMatch "^\.([Hh][Tt]|[Dd][Ss]_[Ss])">
        Require all denied
    </FilesMatch>

et ajouter à la suite :

.. code:: bash

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Pour terminer la configuration il faut juste modifier le Directory Index pour ajouter le index.php comme page pouvant servir de page par default :

.. code:: bash

    <IfModule dir_module>
        DirectoryIndex index.php index.html
    </IfModule>


Une fois terminé, vous pouvez quitter vim et faire un :

.. code:: bash

    $ sudo apachectl restart

Et voilà vous avez PHP sur votre Apache. Pour l'instant c'est pas mal, cependant pour plus de confort je vous conseille de faire les modifications suivantes dans le httpd.conf.


Apache
======

De base l'installation fait référence à un dossier dans le système, c'est pas des plus simple pour dev, moi personnellement je change le dossier pour un dossier htdocs à la racine de mon $HOME, pour cela il faut éditer le fichier /etc/apache2/httpd.conf et rechercher la ligne contenant :

.. code:: bash

    DocumentRoot "/Library/WebServer/Documents"

et la remplacer par :

.. code:: bash

    DocumentRoot "/Users/valentinbrosseau/htdocs"

Un peu plus bas il faut également remplacer le Directory par :

.. code:: bash

    <Directory "/Users/valentinbrosseau/htdocs">

Dans le bloc directory en question il faut également changer l'instruction AllowOverride par :

.. code:: bash

    AllowOverride All

Pour ne pas avoir de soucis de droit il faut changer l'utilisateur et le groupe avec lequel fonctionne apache, pour ça toujours dans le fichier de conf trouver les lignes contenant :

.. code:: bash

    User _www
    Group _www

à remplacer par (dans mon cas, pour vous l'utilisateur sera différent):

.. code:: bash

    User valentinbrosseau
    Group staff

Et voilà après un restart d'apache vous avez une configuration fonctionnelle avec PHP.

Bon dev à vous.

.. _`brew.sh`: http://www.brew.sh/
.. _`le site officiel`: http://www.brew.sh/
