Adb sur TCP/IP (Adb au travers du wifi)
#######################################

:tags: android, cyanogen, wifi, adb
:category: android
:date: 2012-06-12 00:00:00
:blog:
:template: article.html

Si comme moi, vous utilisez une rom Cyanogen, vous avez "la chance" de pouvoir paramétrer votre téléphone pour accepter les connexions de type "ADB" au travers du réseau Wifi. Pour cela rien de plus simple :

Paramètres >> Options pour les développeurs >> ADB sur TCP/IP

Pour accéder à votre téléphone (en ligne de commande) depuis votre ordinateur rien de plus simple

	>>> adb connect <ip_du_telephone>
	connected to <ip_du_telephone>:5555
	>>> adb shell
	shell@android:/ $ 