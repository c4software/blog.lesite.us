SSL : Gitlab + LetsEncrypt (acme.sh) = <3
#########################################

:tags: Gitlab, ssl, LetsEncrypt, acme.sh
:date: 2018-01-26 23:00:00
:blog:
:template: article.html

GitLab c'est bien, mais Gitlab en SSL c'est mieux ! Un petit article rapide pour vous montrer la simplicité de mise en place des certificats SSL gratuit fourni par LetsEncrypt.

La première étape acme.sh
-------------------------

Le plus simple sous Linux pour générer des certificats LetsEncrypt c'est le client en bash Acme.sh :

.. code-block:: shell

    curl https://get.acme.sh | sh

Ou via le sources :

.. code-block:: shell

    git clone https://github.com/Neilpang/acme.sh.git
    cd ./acme.sh
    ./acme.sh --install

😎 Pas besoin d’être root.

Configurer GitLab
-----------------

Maintenant que nous avons notre client « Acme LetsEncrypt », il faut configurer GitLab pour qu'il accepte la connexion entrante venant de LetsEncrypt et qui va valider que vous êtes le propriétaire du nom de domaine. Pour ça il va falloir modifier la configuration « par défaut » de GitLab.

Il faut éditer le fichier /etc/gitlab/gitlab.rb pour ajouter la configuration suivante :

.. code-block:: ruby

    nginx['custom_gitlab_server_config'] = "location ^~ /.well-known { root /var/www/letsencrypt; }"
    mattermost_nginx['custom_gitlab_mattermost_server_config'] = "location ^~ /.well-known { root /var/www/letsencrypt; }"

⚠️ Dans mon cas je vais valider également un certificat pour le Mattermost inclus dans GitLab.

Maintenant que la configuration est modifiée il faut la faire prendre en compte par GitLab :

.. code-block:: shell

    $ gitlab-ctl reconfigure

On va également créer un dossier qui va recevoir le fichier .key et .crt.

.. code-block:: shell

    $ mkdir -p /etc/gitlab/ssl/

Demander un certificat
----------------------

Pas grand-chose à faire, il suffit juste de taper la bonne commande :

.. code-block:: shell

    $ acme.sh --issue -d gitlab.votre_domaine.fr -d mattermost.votre_domaine.fr -w /var/www/letsencrypt --keypath /etc/gitlab/ssl/cert.key --certpath /etc/gitlab/ssl/cert.crt


Et voilà, normalement les fichiers sont disponibles dans le dossier /etc/gitlab/ssl/

Activer le SSL dans GitLab
--------------------------

Maintenant que le certificat a été généré il faut activer réellement le SSL dans GitLab, pour ça retournons dans le fichier /etc/gitlab/gitlab.rb et ajouter la configuration suivante :

.. code-block:: ruby

    # Permet d’indiquer l’emplacement des certificats SSL
    mattermost_nginx['ssl_certificate'] = "/etc/gitlab/ssl/cert.crt"
    mattermost_nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/cert.key"
    nginx['ssl_certificate'] = "/etc/gitlab/ssl/cert.crt"
    nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/cert.key"

    # Permet la redirection du HTTP vers le HTTPS
    nginx['redirect_http_to_https'] = true
    mattermost_nginx['redirect_http_to_https'] = true

Changer la configuration de vos URL dans le /etc/gitlab/gitlab.rb pour ajouter un **s** après http :

- https://mattermost.votre_domaine.fr/ 
- https://gitlab.votre_domaine.fr/


Finalisont en appliquant la configuration :

.. code-block:: shell

    $ gitlab-ctl reconfigure


Et voilà votre GitLab est maintenant configuré en SSL.

Renouvellement
--------------

Les certificats LetsEncrypt ont une durée de validité de 90 jours, mais ils peuvent être renouvelés à l'infinies, avec acme.sh pas de soucis un cron a automatiquement été mis en place lors de l'installation du client acme. Normalement tous les 60 jours vos certificats seront automatiquement renouvelés. Dans mon cas :

.. code-block:: shell

    $ crontab -l
    52 0 * * * "/root/.acme.sh"/acme.sh --cron --home "/root/.acme.sh" > /dev/null

