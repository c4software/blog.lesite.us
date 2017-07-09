Google Chrome, console.table()
##############################

:tags: Chrome, debug, javascript
:date: 2013-11-17 10:50:00
:blog:
:template: article.html

[Edit] Visiblement la console de Firefox fait la même chose! Bonne nouvelle :)

C'est indéniable la console de debug de Google Chrome est vraiment génial, je pense vraiment que celle-ci est loin devant la concurrence, même si celle de Firefox fait des progrès et rattrape petit à petit son « retard ». Une des super fonctionalitée c'est l'objet « console » celui-ci est effectivement disponible sur tous les navigateurs, mais vous ne connaissez peut-être pas ja methode « table »

La methode table est en faite une façon hyper simple de représenter dans votre console de debug un objet Javascript. Rien ne vaut une bonne demo :

.. code:: bash 

	var demo = [
	    { prenom: "Valentin", nom: "Brosseau" },
	    { prenom: "John", nom: "Doe" },
	    { prenom: "Angelina", nom: "Jolie" }
	];

	console.table(demo)

Et ça vous donne :

.. image:: ./static/console_chrome.png

C'est pas magique, mais en tout cas c'est super utile!