# UtilitairesFinalFantasyXIV

## 1. Présentation de l'application

UtilitairesFinalFantasyXIV est une application console permettant la gestion des membres d'une compagnie libre, des recettes et des récoltes du jeu Final Fantasy XIV.

Les fonctionnalités de l'application sont les suivantes :

 - Gestion des membres d'une compagnie libre :
   - Récupération de la liste complète des membres d'une compagnie libre à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des membres d'une compagnie libre dans un fichier au format tabulé,
   - Sélection par l'utilisateur d'une liste de membres d'une compagnie libre (personnalisée ou filtrée par critères),
   - Affichage des caractéristiques, des niveaux par classes et par catégories des membres d'une compagnie libre sélectionnés.

 - Gestion des recettes :
   - Récupération de la liste complète des recettes à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des recettes dans un fichier au format tabulé,
   - Sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères),
   - Calcul et affichage des quantités de matériaux et de cristaux nécessaires afin de réaliser les recettes sélectionnées.

 - Gestion des récoltes :
   - Récupération de la liste complète des récoltes à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des récoltes dans un fichier au format tabulé,
   - Sélection par l'utilisateur d'une liste de récoltes (personnalisée ou filtrée par critères),
   - Affichage des points de récoltes nécessaires afin de réaliser les récoltes sélectionnées.

L'application est réalisée en [Python 2.7.16](https://www.python.org/downloads/release/python-2716/) et nécessite la bibliothèque [BeautifulSoup 4.7.1](https://pypi.org/project/beautifulsoup4/).

## 2. Installation de l'application

### 2.1. Installation de l'interpréteur Python 2.7.16

L'application nécessite l'interpréteur [Python 2.7.16](https://www.python.org/downloads/release/python-2716/). Il convient de récupérer puis d'installer les éléments concernés.

### 2.2 Installation de la bibliothèque BeautifulSoup 4.7.1

L'application nécessite la bibliothèque [BeautifulSoup 4.7.1](https://pypi.org/project/beautifulsoup4/). Il convient de récupérer puis d'installer les éléments concernés.

La bibliothèque BeautifulSoup 4.7.1 peut également s'installer via l'installeur de paquets Python.

Syntaxe d'utilisation :

    python -m pip install bs4

### 2.3. Installation de l'application UtilitairesFinalFantasyXIV

L'application est disponible en [version actuelle](https://github.com/lovehina13/UtilitairesFinalFantasyXIV) ou en [version stable (2.0)](https://github.com/lovehina13/UtilitairesFinalFantasyXIV/releases/tag/v2.0.0). Il convient de récupérer puis d'installer les éléments concernés.

## 3. Utilisation de l'application

### 3.1. Fonctionnalité de récupération des personnages

La fonctionnalité *RecuperationPersonnages* permet de récupérer la liste complète des membres d'une compagnie libre à partir de la base de données d'Éorzéa et de la sauvegarder dans un fichier au format tabulé.

Syntaxe d'utilisation :

    python RecuperationPersonnages.py $numeroCompagnieLibre $fichierPersonnages

Exemple d'utilisation :

    python RecuperationPersonnages.py 9233364398528028107 ListePersonnages.csv

Il convient de modifier le fichier *RecuperationPersonnages.py (ligne 81)* afin d'ajuster le nombre de pages relatives à la compagnie libre considérée.

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

Il convient de modifier le fichier *RecuperationRecettes.py (ligne 61)* afin d'ajuster le nombre de pages relatives aux recettes.

Exemple pour la version 5.00, soit 157 pages :

    nombrePagesRecettes = 157

### 3.4. Fonctionnalité de récupération des matériaux et des cristaux

La fonctionnalité *RecuperationMateriauxCristaux* permet la sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères) et de calculer et d'afficher les quantités de matériaux et de cristaux nécessaires à leur réalisation.

Syntaxe d'utilisation :

    python RecuperationMateriauxCristaux.py $fichierRecettes $fichierMateriauxCristaux

Exemple d'utilisation :

    python RecuperationMateriauxCristaux.py ListeRecettes.csv ListeMateriauxCristaux.csv

Il convient de modifier le fichier *RecuperationMateriauxCristaux.py (ligne 69)* afin de spécifier les recettes à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets.
Les sauts de lignes sont possibles entre les éléments.

Exemple pour les équipements d'artisans de niveau 50 :

    noms = ["Calot de patricien",
            "Boléro de patricien",
            "Gants de patricien",
            "Bas-de-corps de patricien",
            "Guêtres de patricien"]
    recettes = listeRecettes.recupererRecettes(noms=noms)

Il convient de modifier le fichier *RecuperationMateriauxCristaux.py (ligne 69)* afin de spécifier les critères supplémentaires à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets (sauf les nombres).
Les sauts de lignes sont possibles entre les éléments d'un même critère.

Exemple pour les recettes de tanneur et de couturier entre les niveaux 1 et 10 :

    classes = ["Tanneur", "Couturier"]
    niveaux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    recettes = listeRecettes.recupererRecettes(classes=classes, niveaux=niveaux)

Les critères disponibles sont les suivants : *noms*, *classes*, *niveaux*, *categories*, *quantites*, *difficultes*, *solidites* et *qualites* (les critères *materiaux* et *cristaux* seront disponibles prochainement).

### 3.5. Fonctionnalité de récupération des récoltes

La fonctionnalité *RecuperationRecoltes* permet de récupérer la liste complète des récoltes à partir de la base de données d'Éorzéa et de la sauvegarder dans un fichier au format tabulé.

Syntaxe d'utilisation :

    python RecuperationRecoltes.py $fichierRecoltes

Exemple d'utilisation :

    python RecuperationRecoltes.py ListeRecoltes.csv

Il convient de modifier le fichier *RecuperationRecoltes.py (ligne 55)* afin d'ajuster le nombre de pages relatives aux récoltes.

Exemple pour la version 5.00, soit 14 pages :

    nombrePagesRecoltes = 14

### 3.6. Fonctionnalité de récupération des points de récolte

La fonctionnalité *RecuperationPointsRecolte* permet la sélection par l'utilisateur d'une liste de récoltes (personnalisée ou filtrée par critères) et d'afficher les points de récolte nécessaires à leur réalisation.

Syntaxe d'utilisation :

    python RecuperationPointsRecolte.py $fichierRecoltes $fichierPointsRecolte

Exemple d'utilisation :

    python RecuperationPointsRecolte.py ListeRecoltes.csv ListePointsRecolte.csv

Il convient de modifier le fichier *RecuperationPointsRecolte.py (ligne 36)* afin de spécifier les récoltes à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets.
Les sauts de lignes sont possibles entre les éléments.

Exemple pour les cristaux :

    noms = ["Cristal de feu",
            "Cristal de glace",
            "Cristal de vent",
            "Cristal de terre",
            "Cristal de foudre",
            "Cristal d'eau"]
    recoltes = listeRecoltes.recupererRecoltes(noms=noms)

Il convient de modifier le fichier *RecuperationPointsRecolte.py (ligne 36)* afin de spécifier les critères supplémentaires à considérer.
Les éléments doivent être entre crochets, séparés par des virgules et entre guillemets (sauf les nombres).
Les sauts de lignes sont possibles entre les éléments d'un même critère.

Exemple pour les récoltes de mineur et de botaniste entre les niveaux 1 et 10 :

    classes = ["Mineur", "Botaniste"]
    niveaux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    recoltes = listeRecoltes.recupererRecoltes(classes=classes, niveaux=niveaux)

Les critères disponibles sont les suivants : *noms*, *classes*, *sousClasses*, *niveaux* et *categories* (le critère *pointsRecolte* sera disponible prochainement).

## 4. Informations

L'application est en version 2.0 au 3 juillet 2019 et réalisée par [Alexis Foerster](mailto:alexis.foerster@gmail.com), joueur du personnage [Yuna Hikari](https://fr.finalfantasyxiv.com/lodestone/character/8095216/).
