# UtilitairesFinalFantasyXIV

## 1. Présentation de l'application

UtilitairesFinalFantasyXIV est une application console permettant la gestion des membres d'une compagnie libre et des recettes du jeu Final Fantasy XIV.

Les fonctionnalités de l'application sont les suivantes :

 - Gestion des membres d'une compagnie libre :
   - Récupération de la liste complète des membres d'une compagnie libre à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des membres d'une compagnie libre dans un fichier au format tabulé,
   - Sélection par l'utilisateur d'une liste de membres d'une compagnie libre (personnalisée ou filtrée par critères),
   - Affichage des caractéristiques, des niveaux par classes et par catégories des membres d'une compagnie libre.

 - Gestion des recettes :
   - Récupération de la liste complète des recettes à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des recettes dans un fichier au format tabulé,
   - Sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères),
   - Calcul des quantités de matériaux et de cristaux nécessaires afin de réaliser les recettes sélectionnées.

L'application est réalisée en Python 2.7.13 et nécessite la bibliothèque BeautifulSoup 4.5.3.

## 2. Installation des prérequis de l'application

### 2.1. Installation de l'interpréteur Python 2.7.13

L'application nécessite l'interpréteur [Python 2.7.13](https://www.python.org/downloads/release/python-2713/). Il convient de récupérer puis d'installer les éléments concernés.

### 2.2 Installation de la bibliothèque BeautifulSoup 4.5.3

L'application nécessite la bibliothèque [BeautifulSoup 4.5.3](https://pypi.org/project/beautifulsoup4/4.5.3/#files). Il convient de récupérer puis d'installer les éléments concernés.

La bibliothèque BeautifulSoup 4.5.3 peut également s'installer via l'installeur de paquets Python.

Syntaxe d'utilisation :

    python -m pip install bs4

## 3. Utilisation de l'application

### 3.1. Fonctionnalité de récupération des personnages

La fonctionnalité *RecuperationPersonnages* permet de récupérer la liste complète des membres d'une compagnie libre à partir de la base de données d'Éorzéa et de la sauvegarder dans un fichier au format tabulé.

Syntaxe d'utilisation :

    python RecuperationPersonnages.py $numeroCompagnieLibre $fichierPersonnages

Exemple d'utilisation :

    python RecuperationPersonnages.py 9233364398528028107 ListePersonnages.csv

Il convient de modifier le fichier *RecuperationPersonnages.py (ligne 79)* afin d'ajuster le nombre de pages relatives à la compagnie libre considérée.

Exemple pour une compagnie libre avec 80 membres, soit 2 pages :

    nombrePagesPersonnages = 2

### 3.2. Fonctionnalité de récupération des profils

La fonctionnalité *RecuperationProfils* permet la sélection par l'utilisateur d'une liste de membres d'une compagnie libre (personnalisée ou filtrée par critères) et d'afficher leurs caractéristiques et leurs niveaux par classes et par catégories.

Syntaxe d'utilisation :

    python RecuperationProfils.py $fichierPersonnages $fichierProfils

Exemple d'utilisation :

    python RecuperationProfils.py ListePersonnages.csv ListeProfils.csv

Il convient de modifier le fichier *RecuperationProfils.py (ligne 48)* afin de spécifier les personnages à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets.
Les sauts de lignes sont possibles entre les éléments.

Exemple pour certains membres de la compagnie libre *Pampa's Brotherhood* :

    noms = ["Virbyker Tinkle",
            "Cerillyanne Tinkle",
            "Yuna' Hikari"]
    personnages = listePersonnages.recupererPersonnages(noms=noms)

Il convient de modifier le fichier *RecuperationProfils.py (ligne 48)* afin de spécifier les critères supplémentaires à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets.
Les sauts de lignes sont possibles entre les éléments d'un même critère.

Exemple pour les femmes Hyures et Miqo'tes :

    races = ["Hyure", "Miqo'te"]
    sexes = ["Femme"]
    personnages = listePersonnages.recupererPersonnages(races=races, sexes=sexes)

Les critères disponibles sont les suivants : *noms*, *titres*, *serveurs*, *races*, *ethnies*, *sexes*, *datesNaissance*, *divinites*, *citesDepart*, *grandesCompagnies* et *compagniesLibres* (le critère *classes* sera disponible prochainement).

### 3.3. Fonctionnalité de récupération des recettes

La fonctionnalité *RecuperationRecettes* permet de récupérer la liste complète des recettes à partir de la base de données d'Éorzéa et de la sauvegarder dans un fichier au format tabulé.

Syntaxe d'utilisation :

    python RecuperationRecettes.py $fichierRecettes

Exemple d'utilisation :

    python RecuperationRecettes.py ListeRecettes.csv

Il convient de modifier le fichier *RecuperationRecettes.py (ligne 63)* afin d'ajuster le nombre de pages relatives aux recettes.

Exemple pour la version 4.50, soit 141 pages :

    nombrePagesRecettes = 141

### 3.4. Fonctionnalité de récupération des matériaux et des cristaux

La fonctionnalité *RecuperationMateriauxCristaux* permet la sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères) et de calculer les quantités de matériaux et de cristaux nécessaires à leur réalisation.

Syntaxe d'utilisation :

    python RecuperationMateriauxCristaux.py $fichierRecettes $fichierMateriauxCristaux

Exemple d'utilisation :

    python RecuperationMateriauxCristaux.py ListeRecettes.csv ListeMateriauxCristaux.csv

Il convient de modifier le fichier *RecuperationMateriauxCristaux.py (ligne 56)* afin de spécifier les recettes à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets.
Les sauts de lignes sont possibles entre les éléments.

Exemple pour les équipements d'artisans de niveau 50 :

    noms = ["Calot de patricien",
            "Boléro de patricien",
            "Gants de patricien",
            "Bas-de-corps de patricien",
            "Guêtres de patricien"]
    recettes = listeRecettes.recupererRecettes(noms=noms)

Il convient de modifier le fichier *RecuperationMateriauxCristaux.py (ligne 56)* afin de spécifier les critères supplémentaires à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets (sauf les nombres).
Les sauts de lignes sont possibles entre les éléments d'un même critère.

Exemple pour les recettes de tanneur et de couturier entre les niveaux 1 et 10 :

    classes = ["Tanneur", "Couturier"]
    niveaux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    recettes = listeRecettes.recupererRecettes(classes=classes, niveaux=niveaux)

Les critères disponibles sont les suivants : *noms*, *classes*, *niveaux*, *categories*, *quantites*, *difficultes*, *solidites* et *qualites* (les critères *materiaux* et *cristaux* seront disponibles prochainement).

## 4. Informations

L'application est en version 1.5 au 8 janvier 2019 et réalisée par [Alexis Foerster](mailto:alexis.foerster@gmail.com), joueur du personnage [Yuna Hikari](https://fr.finalfantasyxiv.com/lodestone/character/8095216/).
