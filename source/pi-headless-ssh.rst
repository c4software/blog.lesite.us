Raspberry PI Zero W: SSH et Wifi headless.
##########################################

:tags: Pi, SSH, Wifi, Boot
:date: 2017-07-09 12:00:00
:blog:
:template: article.html

[Edit] Ajout du country dans le « wpa_supplicant.conf »

J'ai acquis depuis quelques semaines un Raspberry Pi Zero W (la toute toute petite carte équipée du Wifi de la fondation Rasberry), la petite particularité de celle-ci c'est qu'elle n'est pas équipée d'un port HDMI habituel mais d'un mini HDMI dans mon cas ce n'est pas vraiment un soucis, car le Pi Zero va me servir comme « Mini serveur de relevés de températures ». Par contre le soucis c'est qu'il faut pouvoir activer l'accès SSH et le Wifi dès le premier boot et sans écran ni port ethernet.

Heureusement tout est déjà prévu (mais pas forcément bien documenté à mon goût). Donc comme d’habitude :

- Télécharger la Rasbian Lite.
- « Flasher » la sur votre carte SD.

Activation du SSH :
-------------------

Dans la partition « boot » (sous Windows la seule que vous voyez), sous linux celle en FAT32 il suffit d’ajouter un fichier vide SSH

.. code:: bash

  $ touch SSH

Activation de Wifi :
--------------------

Toujours dans la partition « boot» il faut créer le fichier « wpa_supplicant.conf » avec le contenu suivant :

.. code::

  country=fr
  update_config=1
  ctrl_interface=/var/run/wpa_supplicant

  network={
    ssid="YOUR_SSID"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
  }

Et voilà vous pouvez maintenant éjecter votre carte SD et la brancher dans votre PI. Celui-ci devrait-être connecté dès le premier boot à votre réseau Wifi et autoriser l’accès SSH.
