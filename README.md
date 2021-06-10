# 👴 Créez GrandPy Bot, le papy-robot 🤖
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
<img alt="Flask" src="https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/>
--------------------------------------------

## Introduction ##

Cette application permet à un utilisateur de trouver l'adresse d'un lieu, et d'avoir une petite histoire liée
à celui-ci.
L'utilisation de Flask permet d'avoir une interface graphique minimale, l'utilisation de JQuery permet d'avoir un site
web dynamique.

Pour récuperer, afficher un lieu nous passons par l'API de GoogleMaps. L'API de Wikipedia est utilisé afin de fournir
une petite fonctionnalitée suplémentaire, pour chaques recherches une histoire est raconté en rapport avec le lieu. 

--------------------------------------------

## Installation & lancement ##

Télécharger et décompresser le repository puis créer un VENV. Installer ensuite le requirements.

    pip install -r requirements.txt

L'application utilisant l'API de Google maps, une key est nécessaire. Voici les étapes afin d'en obtenir une : 
    https://www.e-monsite.com/pages/tutoriels/configuration-avancee-du-site/obtenir-une-cle-google-maps-api.html

Pour lancer l'application :

    python run.py

--------------------------------------------

## Applications   ##

- ### botapp : 
    
    - views : Le module principal de l'application, permet la gestion de la route index et les différentes fonctions.
    - parser : Parse la question de l'utilisateur pour fournir un lieu.
    - api_gmaps : Permet de récupérer l'adresse, la latitude et la longitude du lieu recherché par l'utlisateur 
      grace au retour du parseur.
    - api_wiki : Retourne une petite histoire en rapport avec le lieu grâce au retour du parser et/ou les données retournées
    de Gmaps.
    - constantes : Les différents messages nécessaires pour GrandPy. Une liste de stop_words utilisé par le parser.  

--------------------------------------------

## Tests  ##

Des simples tests sont réalisés grâce à pytest, sur : Parser, GmpasApi et WikiApi. Utilisation de mocks pour imiter
le comportement des modules googlemaps et wikipedia.

Pour lancer les tests : 
    
    pytest 


--------------------------------------------

## Version  ##

- v 1.0 : Première version stable de l'application. 