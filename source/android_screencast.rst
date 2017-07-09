Android et les screencasts vidéo
################################

:tags: Android, Screencast
:date: 2013-12-10 21:40:00
:blog:
:template: article.html

Vous l'avez peut-être vu passer sur Internet (ici_ ou là_) la Cyanogen Mod permet maintenant de faire des screencast (en beta pour le moment) c'est une super nouvelle démocratiser et surtout simplifier la prise de vue d'un téléphone est une super nouvelle surtout dans le monde de l'entreprise. Étant moi-même développeur j'ai remarqué que rien ne vaut une démonstration réel d'un site web. À défaut de pouvoir en faire simplement avec tout le monde, j'ai commencé à faire des vidéos (screencast) principalement depuis le mon PC, et pour simuler un mobile un petit tour dans les dev-tools de Chrome et hop. 

Mais ce temps est révolu! Mais pas besoin d'une ROM Cyanogen ou de rooter votre mobile pour en profiter. Depuis Android 4.4 il est possible de faire un screencast de son mobile sans outils supplémentair (ok à part un câble USB - Quoi que -). Pour ça rien de plus simple il suffit de brancher son mobile à son PC et de lancer la commande :

.. code:: bash

	➜ ~ adb shell screenrecord /sdcard/exemple.mp4 

La commande ne retourne aucune info ? C'est normal, l'enregistrement est parti. Pour l'arreter aucun soucis il suffit de faire « Ctrl+c ». Pour le rendu ça donne quelques chose de trés propre :

.. raw:: html

	<br /><iframe width="560" height="315" src="http://www.youtube.com/embed/F_F7o86Pa0o" frameborder="0" allowfullscreen></iframe><br /><br />

PS: Il est aussi possible de lancer l'enregistrement depuis un terminal emulator directement depuis le mobile.

.. _ici: http://www.frandroid.com/applications/183580_screencast-beta-play-store-android
.. _là: https://plus.google.com/110558071969009568835/posts/72Tc9e3ZFMA