Activer les commentaires Google+ sur votre blog
###############################################

:tags: astuce, google+, blogger, iframe
:date: 2013-04-21 18:31:00
:blog:
:template: article.html

Visiblement Google est en train de tester l'intégration des commentaires Google+ dans autre chose que Google+, en début de semaine Google a annoncé que leur outil de blogging utiliserai maintenant Google+ comme support pour les commentaires. Et visiblement le système est plutot open car sans trop se casser la tête il est possible de l'intégrer sur son blog perso. 

Certains ont déjà migré sur ce nouveau service de commentaires, pour ma part je suis plutôt réservé même si le service semble vraiment sympa, je me méfie de Google qui peut sans prévenir couper le tout... (Bha oui rien a été vraiment annoncé). Mais bon vu que vous êtes joueur (et moi aussi) voilà le code source à mettre dans vos pages web pour que celle-ci soit Google+ commentairisé ;).

.. code:: html

	<iframe id="gcomments" width="70%" height="600" src="" frameborder="0" scrolling="auto" marginheight="0" marginwidth="0" ></iframe>
	<script type='text/javascript'>
 		document.getElementById("gcomments").src="https://plusone.google.com/_/widget/render/comments?bsv&href="+document.URL+"&first_party_property=BLOGGER&view_type=FILTERED_POSTMOD";
	</script>

Rien de plus, et oui c'est vraiment super simple... Reste à voir combien de temps ça va fonctionner...

**Hop petite mise à jour, il est possible aussi de passer via une version, avec un peu plus de javascript (plus complexe) mais qui est peut-être un peu plus pérenne (En tout cas qui est je pense beaucoup plus propre):**

.. code:: html

	<script type="text/javascript" src="https://apis.google.com/js/plusone.js" gapi_processed="true"></script>
	<div id="plusonecomments"></div>
	<script type='text/javascript'>
 		var id = 'plusonecomments'; 
 		var divWidth = document.getElementById(id).offsetWidth; 
 		var width = !!divWidth ? Math.min(divWidth, 1351) : 600; 
 		var url = document.URL; 
 		var moderationUrl = ""; 
 		var moderationMode = "FILTERED_POSTMOD"; 
 		gapi.comments.render(id, { 'href': url, 'first_party_property': 'BLOGGER', 'legacy_comment_moderation_url': moderationUrl, 'view_type': moderationMode, 'width': width });
	</script>

[Source_]

.. raw:: html

	<script type="text/javascript" src="https://apis.google.com/js/plusone.js" gapi_processed="true"></script>
	<div id="plusonecomments"></div>
	<script type='text/javascript'>
 		var id = 'plusonecomments'; 
 		var divWidth = document.getElementById(id).offsetWidth; 
 		var width = !!divWidth ? Math.min(divWidth, 1351) : 600; 
 		var url = document.URL; 
 		var moderationUrl = ""; 
 		var moderationMode = "FILTERED_POSTMOD"; 
 		gapi.comments.render(id, { 'href': url, 'first_party_property': 'BLOGGER', 'legacy_comment_moderation_url': moderationUrl, 'view_type': moderationMode, 'width': width });
	</script>

.. _Source: http://www.geekeries.fr/google-plus-comments/	