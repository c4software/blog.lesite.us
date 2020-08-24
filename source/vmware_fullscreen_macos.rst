VMWare fusion et la gestion du plein-écran / fullscreen
#######################################################

:tags: vm, MacOS, fullscreen, dock
:category: macos
:date: 2020-08-24 12:00:00
:blog:
:template: article.html

Un petit article rapide après des années de silence pour vous donner une astuce bien pratique. Cela fait maintenant quelques années, que j'utilise VMWare Fusion sous Mac pour gérer mes machines virtuelles, il fonctionne bien pas de problème. 

Par contre, j'ai un souci le Dock ! En fullscreen celui-ci est « toujours affiché », enfin il est visible au survol. C'est pénible… Et très contreproductif surtout quand on essai de travailler dans la VM… 

Je viens de découvrir que ça se change facilement via la commande suivante :

.. code:: bash

    $ sudo lsappinfo setinfo -app com.vmware.fusion UIPresentationMode=kLSUIPresentationModeContentHiddenValue

Attention par contre, c'est temporaire le comportement revient « par défaut » quand vous quittez le mode plein écran…