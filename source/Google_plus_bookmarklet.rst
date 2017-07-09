Google Plus bookmarklet
#######################

:tags: web, google+, bookmarklet
:date: 2012-07-29 20:00:00
:category: web
:blog:
:template: article.html

.. role:: raw-html(raw)
   :format: html

Je l'avais partagé il y a quelques temps sur les réseaux sociaux, mais jamais sur mon blog donc... Google+ j'aime bien, par contre ce que j'aime moins c'est que peu de site ont intégrés le bouton de partage. Donc pour palier à ça j'ai écrit rapidement un petit bookmarklet qui permet de partager n'importe quelle page sur Google+.

Pour ajouter le bookmarklet rien de plus simple, il suffit de glisser le lien ci-dessous dans votre barre de favoris :

	:raw-html:`<a href="javascript:javascript:var b=document.body;z=document.createElement('script');void(z.src='https://apis.google.com/js/plusone.js');void(b.appendChild(z));elem=document.createElement('div');elem2=document.createElement('div');void(elem2.setAttribute('style','position: fixed; background-image: initial; background-attachment: initial; background-origin: initial; background-clip: initial; background-color: rgb(255, 255, 255);border-top:2px solid red;border-left:2px solid green;border-right:2px solid blue;border-bottom:2px solid yellow;padding:5px; top: 8px; right: 8px; z-index: 2147483647; background-position: initial initial; background-repeat: initial initial; '));void(elem.setAttribute('class','g-plusone'));void(elem2.appendChild(elem));void(b.appendChild(elem2));void(gapi.plusone.go());">Google Plus +1</a>`

Et voilà le tour est joué, vous pouvez maintenant faire des +1 partout :).

PS: Pour twitter cela existe aussi (ce n'est pas de moi mais ça fonctionne bien) :

	:raw-html:`<a href="javascript:(function(){window.twttr=window.twttr||{};var D=550,A=450,C=screen.height,B=screen.width,H=Math.round((B/2)-(D/2)),G=0,F=document,E;if(C>A){G=Math.round((C/2)-(A/2))}window.twttr.shareWin=window.open('http://twitter.com/share','','left='+H+',top='+G+',width='+D+',height='+A+',personalbar=0,toolbar=0,scrollbars=1,resizable=1');E=F.createElement('script');E.src='http://platform.twitter.com/bookmarklets/share.js?v=1';F.getElementsByTagName('head')[0].appendChild(E)}());">Partager sur Twitter</a>`