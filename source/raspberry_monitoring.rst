Monitorer la fréquence et la température d'un Raspberry Pi
##########################################################

:tags: script, raspberry
:date: 2013-02-27 22:55:00
:blog:
:template: article.html

C'est toujours intéressant de pouvoir monitorer ou au moins consulter la fréquence et surtout la température du raspberry Pi. Je ne suis pas parano, mais quand j'ai un système complètement passif j'aime bien consulter la température de fonctionnement pour éviter d'avoir une mauvaise surprise (comme par exemple une carte ou un composant qui part en fumée). Donc le script est vraiment tout simple, mais il remplit son office :

.. code:: bash 

	#!/bin/bash
	GOV=`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor`
	MIN=`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq`
	MAX=`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq`

	echo "$GOV $MIN $MAX" | awk  '{ printf "Governor: %s\nMin Freq: %4dMhz\nMax Freq: %4dMhz\n\n", $1, $2/1000, $3/1000 }'

	C=`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq`
	T=`cat /sys/class/thermal/thermal_zone0/temp`
	echo "`date +%H:%M` $C $T" | awk  '{ printf "%s: %4dMhz, %-.2fC\n",$1, $2/1000,$3/1000 }'

La sortie :

.. code:: bash

	>>> ➜  ~  ./monitor.sh 
	Governor: ondemand
	Min Freq:  700Mhz
	Max Freq:  700Mhz

	22:17:41:  700Mhz, 42.24C
