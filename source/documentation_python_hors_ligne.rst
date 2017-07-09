De la documentation oui! Mais offline...
########################################

:tags: astuce, python, documentation
:date: 2013-05-22 20:09:00
:blog:
:template: article.html

Même si aujourd'hui les périodes hors-ligne sont de moins en moins nombreuses il peut arriver pour une raison X ou Y de ne pas avoir Internet (Train, Camping, ...). Et dans c'est cas là plus de documentation plus rien... Pas très pratique, c'est donc par hasard (et en camping) que je suis tombé sur l'outil pydoc, c'est un peu le man des fonctions python.

Mais ce n'est pas tout si on lui passe le flag -g on ce retrouve avec une petite interface web ET une fonction de recherche dans la documentation installée sur la machine. génial quoi! Donc rien de plus simple

	>>> pydoc -g

ou pour les fans du terminal (par exemple la fonction print)

	>>> pydoc print

Donc plus d'excuse même sans Internet vous pourrez retrouver la doc des fonctions ;).