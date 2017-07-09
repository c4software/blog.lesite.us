Activer la nouvelle page d'accueil de Google
############################################

:tags: google, cookie, astuce
:date: 2013-09-19 22:00:00
:blog:
:template: article.html

Vous l'avez peut être vu sur Internet, Google_ est entrain de tester chez certains un nouveau design pour la homepage de Google.com. Les modifications sont assez nombreuses (oui 3 modifications pour la homepage de Google c'est pas mal :D):

* Nouveau Logo (très IOS7 je trouve).
* Nouveau Menu.
* Et une interface encore plus épuré

	.. image:: http://c4software.another-team.com/google.png

Donc pour tester rien de plus simple:

	>>> Ouvrez votre navigateur et dans la console de celui-ci (exemple F12 sous Chrome) vous tapez ceci :
	>>> document.cookie="PREF=ID=e66a207a51ceefd8:U=936bafc98b2a9121:FF=0:LD=en:NR=10:CR=2:TM=1378808351:LM=1379592992:SG=1:S=OXyq0fqClYB66VuV ; path=/; domain=google.com";window.location.reload();


.. _Google: https://www.google.com/ncr