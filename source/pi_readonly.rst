Sauver une carte SD! Utiliser votre Pi en lecture seule
#######################################################

:tags: RaspberryPi, carde sd, readonly, tweak
:category: RaspberryPi
:date: 2018-01-23 22:00:00
:blog:
:template: article.html

Avec mes Pi j'ai un soucis récurrent c'est l'usure des cartes SD… J'ai tenté pleins de choses (réduire les logs, changer le swap, etc…) mais sans jamais de grand succès au final la carte SD se corrompt et rebelotte…

J'ai donc décidé de changer carrément de méthode, à partir de maintenant pour les projets ou je n'ai pas besoin d'écrire sur la carte SD, et bien je monte carrément le système en lecture seule. Pour ça il suffit de changer un peu le « /etc/fstab » :

.. code-block:: configuration

    proc            /proc           proc    defaults          0       0
    /dev/mmcblk0p1  /boot           vfat    defaults          0       2
    /dev/mmcblk0p2  /               ext4    ro                0       1
    # Valeur par defaut : /dev/mmcblk0p2  /               ext4    defaults,noatime  0       1

    tmpfs           /tmp            tmpfs   defaults,noatime,mode=1777      0       0
    tmpfs           /var/log        tmpfs   defaults,noatime,mode=0755      0       0
    tmpfs           /var/lib/systemd tmpfs   defaults,noatime,mode=0755      0       0

À partir de maintenant si vous redémarrez le Pi votre système sera en lecture seule.

Donc c'est un bon début… Mais parfois c'est pratique de pouvoir modifier son système (mise à jour par exemple), j'ai donc trouvé un petit script qui permet de passer de lecture seule à lecture/écriture hyper simplement :

.. code-block:: shell

    #!/bin/bash

    case "${1}" in
            rw)
                    sudo mount -o remount,rw /
                    echo "Filesystem mounted in READ-WRITE mode"
                    ;;
            ro)
                    sudo mount -o remount,ro /
                    echo "Filesystem mounted in READ-ONLY mode"
                    ;;
            *)
                    if [ -n "$(mount | grep mmcblk0p2 | grep -o 'rw')" ]
                    then
                            echo "Filesystem is mounted in READ-WRITE mode"
                    else
                            echo "Filesystem is mounted in READ-ONLY mode"
                    fi
                    echo "Usage ${0} [rw|ro]"
                    ;;
    esac


Pour l’utiliser c’est simple :

- Repasser en lecture/écriture : ./mountfs.sh rw 
- Repasser en lecture seule : ./mountfs.sh ro

En espérant que ça aide certains d’entre vous … 