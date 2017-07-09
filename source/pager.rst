Paginer les résultats avec MySQL Cli
#####################################

:tags: Mysql, astuce
:date: 2012-11-30 19:59:00
:blog:
:template: article.html

Je n'ai jamais vraiment trouvé très pratique l'utilisation du client Mysql (Control-C qui quitte le programme, la non-pagination des résultats, etc). Mais aujourd'hui j'ai trouvé sur le net une super astuce qui permet (entre autre) la pagination des résultats. Cette astuce c'est la variable **pager**.

Pour l'utilisation rien de plus simple, il suffit de se connecter à un serveur MySql avec le client shell et de taper :

	>>> mysql> pager more
	PAGER set to 'more'

Et à partir de ce moment, si le nombre d'enregistrements dépasse le nombre affichable sur l'écran MySql utilisera la commande système more pour limiter le nombre d'éléments à afficher exemple :

	>>> 	+-----+------------+---------+---------+-----+-------+-------+----------------+----------+
		| id  | date       | produit | famille | qte | HT    | motif | pour           | secteur  |
		+-----+------------+---------+---------+-----+-------+-------+----------------+----------+
		| 337 | 16-10-2012 |      89 |       9 |  15 |  0.28 | 2     |                | fulgent  |
		| 336 | 16-10-2012 |     242 |       9 |   2 |  6.95 | 2     |                | fulgent  |
		| 335 | 15-10-2012 |     241 |      12 |   3 |  2.56 | 2     |                | herbiers |
		--Plus--

Mais la puissance du truc ne s'arrête pas là, si par exemple vous voulez sortir le résultat dans vim, rien de plus simple

	>>> mysql> pager vim -

ou alors faire un grep 

	>>> mysql> pager grep --color -v 89

etc. etc. etc... C'était la bonne astuce de la soirée :).