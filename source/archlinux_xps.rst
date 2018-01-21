Installer Archilnux sur un Dell XPS 2017 (Remplacer Ubuntu)
###########################################################

:tags: Archlinux, Dell, XPS
:category: Archlinux
:date: 2018-01-21 21:00:00
:blog:
:template: article.html

J'ai récemment eu une nouvelle machine (changement professionnel) cette machine est un [DELL XPS 9360 (de 2017) fourni avec Ubuntu](http://www.dell.com/en-us/shop/dell-laptops/xps-13-laptop/spd/xps-13-9360-laptop). C'est vraiment une superbe machine un 13 pouces dans un gabarit d'un 11… Bref génial !

La machine est livrée avec Ubuntu 16.04 LTS, ça fonctionne… mais je ne suis vraiment pas fan d'Ubuntu (exemple Out Of The Box unity plante régulièrement sans raison…) ! Donc migration sous Archlinux. Rien de bien particuliés pour l'installation, c'est une machine avec de l'UEFI j'ai donc décidé de faire un petit article récap pour lister les différentes étapes clef de l'installation :

- [Téléchargement de l’ISO](https://www.archlinux.org/download/).
- Dans l’UEFI de la machine désactiver le secureboot (F12 au démarrage).
- Choisir la clef USB sur laquelle l’ISO a été « copié ».

⚠️ Archlinux n’est pas un OS pour débutant, si vous avez un doute… Passer votre tour.

Je vous conseille une fois booté de lancer le service SSH pour faire l'installation depuis une autre machine (ça permet de copier les commandes) :

.. code-block:: shell

    # Clavier
    loadkeys fr-bepo

    # Pour autoriser la connexion le compte Root doit avoir un mot de passe.
    $ passwd
    $ systemctl start sshd.service

    # Connexion au Wifi
    wifi-menu

    # Avoir votre IP
    $ ip addr


Pour la suite vous pouvez continuer depuis une autre machine

.. code-block:: shell

    $ ssh root@ip.de.votre.machine


Pour éviter de perdre la partition de recovery fourni par DELL j’ai décidé de ne pas toucher au partitionnement « de base », je part du principe que ça sera le cas vous aussi.

La base
-------

.. code-block:: shell

    # Clavier
    loadkeys fr-bepo

    # Reglage de l’heure
    timedatectl set-ntp true

    # Éffacement des partitions
    # Boot
    $ mkfs.fat -F32 /dev/nvme0n1p1

    # Système
    $ mkfs.ext4 /dev/nvme0n1p3

    # Montage des partitions
    $ mount /dev/nvme0n1p3 /mnt 
    $ mount /dev/nvme0n1p1 /mnt/boot

    # Installation du système de base et d’autres paquets nécéssaire en CLI
    $ pacstrap /mnt base base-devel dialog zsh git sudo vim dialog wpa_supplicant iw

    # Création du fstab
    $ genfstab -L /mnt >> /mnt/etc/fstab

    # Changer la partition ext4 pour passer de relatime to noatime (Ça réduit l’usure du SSD)
    $ vim /mint/etc/fstab

    # Activation du chroot
    $ arch-chroot /mnt

    # Reglage du temps
    $ ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime
    $ hwclock --systohc

    # Réglage des locales
    $ vi /etc/locale.gen	# Décommenter par exemple "en_US.UTF-8", "fr_FR.UTF-8"
    $ locale-gen

    # Locale par défaut
    $ echo 'LANG=fr_FR.UTF-8' > /etc/locale.conf

    # Disposition clavier par defaut
    $ echo 'KEYMAP=fr-bepo' > /etc/vconsole.conf

    # Nom de la machine
    echo 'vbrosseau-laptop' > /etc/hostname

    # Définition des hosts de base
    $ echo '127.0.0.1   localhost.localdomain	localhost' > /etc/hosts
    $ echo '::1 	localhost.localdomain	localhost' >> /etc/hosts
    $ echo '127.0.1.1   vbrosseau-laptop.localdomain	vbrosseau-laptop' >> /etc/hosts

    # Définition du mot de passe root de votre machine
    $ passwd

    # Création de votre utilisateur
    $ useradd -m -g users -G wheel -s /bin/zsh vbrosseau
    $ passwd vbrosseau
    $ echo 'vbrosseau ALL=(ALL) ALL' > /etc/sudoers.d/vbrosseau

    # Activation du modules ext4 (requis pour le boot)
    $ vim /etc/mkinitcpio.conf
    # Ajouter "ext4" dans MODULES

    # Génération de l’image initrd
    $ mkinitcpio -p linux

    # Installation des de la gestion des updates d’Intel
    $ pacman -S intel-ucode 

    # Boot de la machine (c’est la partie la plus sensible)
    $ bootctl --path=/boot install

    # Création des entrées dans le bootloader (bootctl)
    $ vim /boot/loader/entries/arch.conf

    title   Arch Linux
    linux   /vmlinuz-linux
    initrd	/intel-ucode.img
    initrd  /initramfs-linux.img
    options root=/dev/nvme0n1p3 rw

    # Mettre Archlinux comme boot par defaut
    $ vim /boot/loader/loader.conf

    default		arch

Voilà l’installation de base est faite. Avant de rédémarrer installons la suite (La partie graphique et dans mon cas Gnome-Shell)

La partie Graphique, Audio et Gnome-Shell
-----------------------------------------

.. code-block:: shell

    # L’audio
    $ pacman -S gst-plugins-{base,good,bad,ugly} gst-libav

    # Xorg
    $ pacman -S xorg-{server,xinit} xf86-input-libinput xdg-user-dirs

    # Le pilote graphique
    $ pacman -S xf86-video-intel

    # Les fonts
    $ pacman -S ttf-{bitstream-vera,liberation,freefont,dejavu}

    # Installation de Gnome-Shell
    $ pacman -S gnome gnome-extra system-config-printer unoconv pavucontrol pulseaudio pulseaudio-alsa
    $ systemctl enable gdm

    # Extra 
    $ pacman -S libreoffice-still-fr firefox-i18n-fr chromium

AUR ou Arch User Repository
---------------------------

Ajouter à la fin du /etc/pacman.conf le Repository « Archlinux FR »

.. code-block:: shell

    # Ajouter à la fin
    $ vim /etc/pacman.conf

    [archlinuxfr]
    SigLevel = Never
    Server = http://repo.archlinux.fr/$arch

    # Installation de Yaourt
    $ pacman -Syy
    $ pacman -S yaourt

Voilà, maintenant que tout est installé

.. code-block:: shell

    # On quitte 
    $ exit

    # On reboot
    $ reboot


Votre ordinateur devrais reboot sous Archlinux.