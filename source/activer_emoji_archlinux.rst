Activer les emoji’s colorés sur Archlinux
#########################################

:tags: Archlinux, emoji, fonts, systeme, os
:category: Archlinux
:date: 2018-01-19 21:00:00
:blog:
:template: article.html

Une note rapide, si comme moi vous voulez activer les emoji’s colorés (comme sur un mobile) sur Archlinux sans vous prendre la tête il suffit d’installer la bonne font et créer le bon fichier de configuration :

.. code-block:: shell

    yaourt -S noto-fonts-emoji
    mkdir -p ~/.config/fontconfig/conf.d/
    vim ~/.config/fontconfig/conf.d/01-emoji.conf


Dans le fichier 01-emoji.conf mettre le contenu suivant :

.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
        <!-- Use Google Emojis -->
        <match target="pattern">
            <test qual="any" name="family"><string>Segoe UI Emoji</string></test>
            <edit name="family" mode="assign" binding="same"><string>Noto Color Emoji</string></edit>
        </match>
    </fontconfig>


Et voilà ! À vous les emoji’s colorés dans votre navigateur (ou autre) 😉.