Quelques règles pour le web mobile
##################################

:tags: Mobile, UX, Chrome, Google
:date: 2013-11-22 23:30:00
:blog:
:template: article.html

.. _`Google Chrome Dev Summit`: http://developer.chrome.com/devsummit/schedule
.. _`PageSpeed Insights for UX`: https://developers.google.com/speed/


Dans une récente conférence qui c'est déroulé lors du `Google Chrome Dev Summit`_ à Mountain View, +Paul Kinlan a présenté les règles de base (selon Google) pour une application web mobile de qualité, voilà un petit résumé de ce qui s'est dit :

Dans un premier temps les erreurs
---------------------------------

* Le mobile est en plein essor et les gens s'orientent vers des expériences mobiles.
* 53% des 1000 sites de Alexa n'ont pas de version mobile. Ce sont juste des versions réduite (De-zoomer). 25% de ces sites ne tiennent mêmes pas sur l'écran.
* 83% des sites ont une navigation difficile aux doigts, 60% ont des problèmes de lisibilité. 10% ont utilisé des plugins qui ne fonctionnent pas sur un mobile (Flash, Java, Silverlight).


Une des solutions? `PageSpeed Insights for UX`_
-----------------------------------------------

Google propose un outil (PageSpeed Insights for UX) qui permet de :

* Vérifier la bonne configuration de vos viewport
* Vérifier que le texte est lisible
* Que les éléments clickable sont suffisamment grand.

Et après le test l'outil vous propose des pistes d'améliorations :

* Indique quels éléments agrandir pour simplifier le clique au doigt.
* Quelle taille de police utiliser pour que votre site soit lisible.
* Quels viewport utiliser.

L'outil vous permet :

* D'avoir un aperçu du rendu de votre site sur un terminal mobile.
* Affiche comment les utilisateurs peuvent interagir dans votre application.

Quelques règles à appliquer
---------------------------

* Toujours utiliser des viewport pour créer une vraie experience mobile.
* Toujours définir une règle « device-width » pour être certain du rendu quel que soit le périphérique. 
* Le navigateur essayera toujours de compenser pour que le site soit lisible, agrandissement des polices, l'utilisation des viewport vous permettra de reprendre le contrôle de l'affichage.
* TOUJOURS adapter le contenu de votre site pour qui l'utilisateur n'est pas à scroller dans des multiples directions (en utilisant les viewports donc).
* Définisser via le « Media Queries » comment doit se comporter votre site en fonction de la taille d'écran.
* Quel que soit la beauté de votre police, 12pt, 1em, 16px, est la taille minimum pour que votre texte soit lisible.
* Un bon contraste ainsi qu'un « line-height » bien calculer améliorera grandement la lisibilité.
* Limiter au maximum l'utilisation des Web Fonts (sur un mobile), si vous devez vraiment les utiliser, utiliser les pour les titres.
* Un élément clickable doit faire 7mm de large et inclure 2mm de padding.
* L'utilisation des labels, permet d'avoir 2x plus d'éléments clickables pour accéder à l'élément voulu.
* L'utilisation des nouveaux types d'input HTML (number, email, etc…), vous permets d'adapter de clavier de l'utilisateur en fonction de la donnée saisie.
* Essayer au maximum de proposer de l'auto-complétion (autoComplete api) pour réduire le nombre de caractère à taper pour l'utilisateur.
* Quand vous renseignez un viewport le double tap pour zoomer n'est plus disponible (width=device-width, initial-scale=1, maximum-scale=1)

