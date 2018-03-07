Configurer simplement Cordova sous MacOS
########################################

:tags: Cordova, osx, android, sdk, tricks
:date: 2018-03-07 21:47:00
:blog:
:template: article.html

Salut ! Changement de boulôt changement d’ordinateur, donc reconfiguration des logiciels. Pour Cordova c’est plutôt « simple » il faut :

- NodeJS
- Le SDK Android
- Le JDK (Java Dev Kit)
- Gradle 

Pour NodeJS et Gradle pas de choix le plus simple c’est de passer par Brew.sh :

.. code:: bash

  brew install nodejs
  brew install gradle  --ignore-dependencies
  npm install -g cordova

Pourquoi --ignore-dependencies ? C’est simplement que l’on va utiliser le JDK fourni dans le SDK d’Android 😁.

Maintenant que la base est prête il vous suffit d’installer `le SDK d’Android (celui avec Android Studio)  <https://developer.android.com/studio/index.html>`_. Une fois installé (et lancé une première fois), éditer votre .zshrc (ou .bashrc) pour ajouter :

.. code:: bash

    export ANDROID_HOME=$HOME/Library/Android/sdk/
    export JAVA_HOME="/Applications/Android Studio.app/Contents/jre/JDK/Contents/Home/"
    export PATH=${PATH}:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools


Et voilà, vous avez maintenant dans votre terminal les outils (et le sdk) Android. Vous pouvez utiliser Cordova comme habituellement.

Bon dev à tous 