Sitemap générator : Python webcrawler
#####################################

:tags: Python, web, sitemap
:category: Python
:date: 2012-07-29 18:00:00
:blog:
:template: article.html

[EDIT] Le projet avance maintenant sur Github : ici_

Dans le cadre de mon boulot j'ai eu à mettre en place une sitemap_ pour un site complètement dynamique (les pages sont créée via une administration et via un ensemble de pattern pour la partie dynamique du site) en gros il était très compliqué de générer efficacement une liste de l'ensemble des urls de façon automatique. Le plus simple a été de faire un petit crawler web qui navigue sur le site de façon périodique pour mettre à jour le fichier sitemap.xml.

Et vu que j'adore le python et bien... Vous avez deviné la suite ;). J'avais fait quelques recherches sur le web avant mais j'ai pas trouvé de script simple pour crawler un site web. Enfin si mais il y avait toujours plus de dépendance je voulais en avoir aucune (plus simple pour le déploiement en production). Le script utilise python3 (histoire d'être moderne ;)).

Pour utiliser le script rien de plus simple (en prenant en compte que **python == python3**):

	>>> python main.py --domain http://blog.lesite.us --output sitemap.xml

Si aucun output n'est spécifié le sitemap s'affichera sur la console.

Pour récupérer le script c'est par ici_

.. _ici: https://github.com/c4software/python-sitemap
.. _sitemap: http://www.sitemaps.org/

PS : N'oubliez pas que c'est une première version ;).

*EDIT : J'avais oublié, j'ai ajouté la possibilité d'ignorer certaines extensions lors du "crawl" :*

	>>> python main.py --domain http://blog.lesite.us --output sitemap.xml	--skipext pdf --skipext xml