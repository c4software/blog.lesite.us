Utiser une Yubikey comme smartcard et Agent-SSH avec Archilnux
##############################################################

:tags: Archlinux, yubikey, systeme, os
:category: Archlinux
:date: 2018-01-20 21:00:00
:blog:
:template: article.html

J'ai récemment réinstallé un Archlinux (sur un Dell XPS 2017, le 9360) j'utilise depuis quelques mois une Yubikey comme Smartcard (et comme Agent-SSH). C'est bien pratique et cela évite d'avoir les clefs PGP et SSH physiquement sur la machine.

J'utilisai ma clé sur un Mac et sur Android, mais je ne l'avais pas branché sur une machine Archlinux… Donc ce qui nous intéresse la configuration. Pour que ça fonctionne il faut installer les paquets suivants :

.. code-block:: shell

    yaourt -S gnupg libu2f-host pcsc-tools ccid libusb-compat

Puis démarrer le service :

.. code-block:: shell

    systemctl enable pcscd.service
    systemctl start pcscd.service


Et pour la configuration, c’est comme sur les autres systèmes :

.. code-block:: configuration

    enable-ssh-support
    default-cache-ttl 1800
    max-cache-ttl 21600
    pinentry-program /usr/bin/pinentry

Et voilà, normalement c’est bon! Votre Yubikey est utilisable. 