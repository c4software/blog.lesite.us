Modification importante du rc.conf sous Archlinux
#################################################

:tags: Archlinux, rc.conf, systemd
:category: Archlinux
:date: 2012-08-12 12:35:00
:blog:
:template: article.html

**[EDIT]** La partie Network a aussi été déplacée dans /etc/conf.d/netcfg

Il y a en ce moment des gros changements dans la distribution Archlinux (abandons de Grub, migration vers systemd, modification de glibc, etc.). Et ce n'est pas fini l'autre grosse modification c'est celle concernant le **rc.conf**. On passe donc d'un fichier unique à 6 fichiers différents (voir plus)...

- **/etc/hostname** (Nom de la machine sur le réseau)
- **/etc/modules-load.d/*** (Contient les modules à charger -Bonne nouvelle on peut découper en plusieurs fichier-)
- **/etc/modprobe.d/blacklist.conf** (Contient les modules blacklister)
- **/etc/locale.conf** (Langue pour le système)
- **/etc/vconsole.conf** (Langue du clavier)
- **/etc/timezone** (Fuseau horaire)
- **/etc/conf.d/netcfg** (Configuration des interfaces réseau)

Et pour le rc.conf il est réduit à ça plus simple expression :

	>>> [valentin@valentinpc output]$ cat /etc/rc.conf
	#
	# /etc/rc.conf - configuration file for initscripts
	#
	# Most of rc.conf has been replaced by various other configuration
	# files. See archlinux(7) for details.
	#
	# For more details on rc.conf see rc.conf(5).
	#
	DAEMONS=(syslog-ng dbus @networkmanager @crond acpid cpufreq)
	# Storage
	#
	# USEDMRAID="no"
	# USELVM="no"

Chez moi la nouvelle configuration donne :

	>>> [valentin@valentinpc src]$ cat /etc/hostname 
	valentinpc

	>>> [valentin@valentinpc src]$ cat /etc/modules-load.d/modules 
	fuse
	acpi_cpufreq

	>>> [valentin@valentinpc src]$ cat /etc/locale.conf
	LOCALE=fr_FR.UTF-8
	LC_COLLATE=C

	>>> [valentin@valentinpc src]$ cat /etc/vconsole.conf 
	KEYMAP="fr-pc"
	FONT="lat9w-16"
	FONT_MAP="8859-1_to_uni"

	>>> [valentin@valentinpc src]$ cat /etc/timezone 
	Europe/Paris

	>>> [valentin@valentinpc src]$ cat /etc/conf.d/netcfg
	# interface=
	# address=
	# netmask=
	# gateway=


Donc rien de bien compliquer en soit, mais je sens que les prochaines installations de Archlinux seront vraiment, mais alors vraiment moins fun... (surtout avec dans le même temps l'abandon d'Aif :()

Merci à `+Frederic Bezies`_ pour son super article :).

Un petit tableau récapitulatif est disponible dans le Wiki anglais : ICI_

.. _+Frederic Bezies: http://frederic.bezies.free.fr/blog/?p=8017
.. _ICI: https://wiki.archlinux.org/index.php/Beginners%27_Guide#Configure_the_system