# UtilitairesFinalFantasyXIV

## 1. Présentation de l'application

UtilitairesFinalFantasyXIV est une application console permettant la gestion des membres d'une compagnie libre, des recettes, des récoltes et de l'inventaire du jeu Final Fantasy XIV.

Les fonctionnalités de l'application sont les suivantes :

 - Gestion des membres d'une compagnie libre :
   - Récupération de la liste complète des membres d'une compagnie libre à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des membres d'une compagnie libre dans un fichier au format utilisateur ou tabulé,
   - Sélection par l'utilisateur d'une liste de membres d'une compagnie libre (personnalisée ou filtrée par critères),
   - Affichage des caractéristiques, des niveaux par classes et par catégories des membres d'une compagnie libre sélectionnés.

 - Gestion des recettes :
   - Récupération de la liste complète des recettes à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des recettes dans un fichier au format utilisateur ou tabulé,
   - Sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères),
   - Affichage des caractéristiques des recettes sélectionnées.

 - Gestion des récoltes :
   - Récupération de la liste complète des récoltes à partir de la base de données d'Éorzéa,
   - Sauvegarde de la liste complète des récoltes dans un fichier au format utilisateur ou tabulé,
   - Sélection par l'utilisateur d'une liste de récoltes (personnalisée ou filtrée par critères),
   - Affichage des caractéristiques des récoltes sélectionnées.

 - Gestion de l'inventaire :
   - Sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères),
   - Calcul et affichage des quantités de matériaux/cristaux et des points de récoltes nécessaires afin de réaliser les recettes sélectionnées.

L'application est réalisée en [Python 3.7.3](https://www.python.org/downloads/release/python-373/) et nécessite la bibliothèque [BeautifulSoup 4.7.1](https://pypi.org/project/beautifulsoup4/).

## 2. Installation de l'application

### 2.1. Installation de l'interpréteur Python 3.7.3

L'application nécessite l'interpréteur [Python 3.7.3](https://www.python.org/downloads/release/python-373/). Il convient de récupérer puis d'installer les éléments concernés.

### 2.2 Installation de la bibliothèque BeautifulSoup 4.7.1

L'application nécessite la bibliothèque [BeautifulSoup 4.7.1](https://pypi.org/project/beautifulsoup4/). Il convient de récupérer puis d'installer les éléments concernés.

La bibliothèque BeautifulSoup 4.7.1 peut également s'installer via l'installeur de paquets Python.

Syntaxe d'utilisation :

```shell
    python -m pip install bs4
```

### 2.3. Installation de l'application UtilitairesFinalFantasyXIV

L'application est disponible en [version actuelle](https://github.com/lovehina13/UtilitairesFinalFantasyXIV) ou en [version stable (3.0)](https://github.com/lovehina13/UtilitairesFinalFantasyXIV/releases/tag/v3.0.0). Il convient de récupérer puis d'installer les éléments concernés.

L'application s'installe en tant que paquetage Python 3.7.3.

Syntaxe d'utilisation :

```shell
    python setup.py install
```

## 3. Utilisation de l'application

### 3.1. Fichier de configuration

L'application s'exécute avec un fichier de configuration au format JSON préalablement renseigné par l'utilisateur.

Syntaxe d'utilisation :

```shell
    python -m UtilitairesFinalFantasyXIV Configuration.json
```

Un fichier de configuration au format JSON par défaut est créé si aucun n'est spécifié.

### 3.2. Fonctionnalité de récupération des personnages

La fonctionnalité *PagePersonnage* permet de récupérer la liste complète des membres d'une compagnie libre à partir de la base de données d'Éorzéa et de la sauvegarder dans un fichier au format tabulé.

Exemple de configuration :

```json
    "pagePersonnages": {
        "activer": true,
        "compagnieLibre": "9233364398528028107",
        "nombrePages": 1,
        "fichierSortie": "Personnages.csv"
    },
```

Il convient de modifier la configuration afin d'ajuster notamment la compagnie libre considérée ainsi que son nombre de pages.

### 3.3. Fonctionnalité de récupération des recettes

La fonctionnalité *PageRecettes* permet de récupérer la liste complète des recettes à partir de la base de données d'Éorzéa et de la sauvegarder dans un fichier au format tabulé.

Exemple de configuration :

```json
    "pageRecettes": {
        "activer": true,
        "nombrePages": 185,
        "fichierSortie": "Recettes.csv"
    },
```

Il convient de modifier la configuration afin d'ajuster notamment le nombre de pages relatives aux recettes, soit 185 pour la version 5.50.

### 3.4. Fonctionnalité de récupération des récoltes

La fonctionnalité *PageRecoltes* permet de récupérer la liste complète des récoltes à partir de la base de données d'Éorzéa et de la sauvegarder dans un fichier au format tabulé.

Exemple de configuration :

```json
    "pageRecoltes": {
        "activer": true,
        "nombrePages": 18,
        "fichierSortie": "Recoltes.csv"
    },
```

Il convient de modifier la configuration afin d'ajuster notamment le nombre de pages relatives aux récoltes, soit 18 pour la version 5.50.

### 3.5. Fonctionnalité de gestion des personnages

La fonctionnalité *GestionPersonnages* permet la sélection par l'utilisateur d'une liste de membres d'une compagnie libre (personnalisée ou filtrée par critères) et d'afficher puis sauvegarder leurs caractéristiques et leurs niveaux par classes et par catégories.

Exemple de configuration :

```json
    "gestionPersonnages": {
        "activer": true,
        "fichierEntree": "Personnages.csv",
        "fichierSortie": "Personnages.txt",
        "filtres": {},
        "trier": true,
        "formatUtilisateur": true
    },
```

Il convient de modifier la configuration afin de spécifier notamment les personnages à considérer.

Exemple pour certains membres de la compagnie libre *Pampa's Brotherhood* :

```json
        "filtres": {
            "nom": ["Virbyker Tinkle",
                    "Cerillyanne Tinkle",
                    "Yuna' Hikari"],
```

Exemple pour les femmes Hyures et Miqo'tes :

```json
        "filtres": {
            "race": ["Hyure", "Miqo'te"],
            "sexe": ["Femme"],
```

Les critères disponibles sont les suivants : *nom*, *titre*, *serveur*, *race*, *ethnie*, *sexe*, *dateNaissance*, *divinite*, *citeDepart*, *grandeCompagnie*, *rang* et *compagnieLibre* (le critère *classes* sera disponible prochainement).

### 3.6. Fonctionnalité de gestion des recettes

La fonctionnalité *GestionRecettes* permet la sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères) et d'afficher puis sauvegarder leurs caractéristiques.

Exemple de configuration :

```json
    "gestionRecettes": {
        "activer": true,
        "fichierEntree": "Recettes.csv",
        "fichierSortie": "Recettes.txt",
        "filtres": {},
        "trier": true,
        "formatUtilisateur": true
    },
```

Il convient de modifier la configuration afin de spécifier notamment les recettes à considérer.

Exemple pour les équipements d'artisans de niveau 50 :

```json
        "filtres": {
            "nom": ["Calot de patricien",
                    "Boléro de patricien",
                    "Gants de patricien",
                    "Bas-de-corps de patricien",
                    "Guêtres de patricien"],
```

Exemple pour les recettes de tanneur et de couturier entre les niveaux 1 et 10 :

```json
        "filtres": {
            "classe": ["Tanneur", "Couturier"],
            "niveau": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
```

Les critères disponibles sont les suivants : *nom*, *classe*, *niveau*, *livre*, *categorie*, *totalFabrique*, *difficulte*, *solidite*, *qualiteMaximum*, *qualite* et *degre* (les critères *materiaux*, *cristaux* et *conditions* seront disponibles prochainement).

### 3.7. Fonctionnalité de gestion des récoltes

La fonctionnalité *GestionRecoltes* permet la sélection par l'utilisateur d'une liste de récoltes (personnalisée ou filtrée par critères) et d'afficher puis sauvegarder leurs caractéristiques.

Exemple de configuration :

```json
    "gestionRecoltes": {
        "activer": true,
        "fichierEntree": "Recoltes.csv",
        "fichierSortie": "Recoltes.txt",
        "filtres": {},
        "trier": true,
        "formatUtilisateur": true
    },
```

Il convient de modifier la configuration afin de spécifier notamment les récoltes à considérer.

Exemple pour les cristaux :

```json
        "filtres": {
            "nom": ["Cristal de feu",
                    "Cristal de glace",
                    "Cristal de vent",
                    "Cristal de terre",
                    "Cristal de foudre",
                    "Cristal d'eau"],
```

Exemple pour les récoltes de mineur et de botaniste entre les niveaux 1 et 10 :

```json
        "filtres": {
            "classe": ["Mineur", "Botaniste"],
            "niveau": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
```

Les critères disponibles sont les suivants : *nom*, *classe*, *sousClasse*, *niveau* et *categorie* (le critère *pointsRecolte* sera disponible prochainement).

### 3.8. Fonctionnalité de gestion de l'inventaire

La fonctionnalité *GestionInventaire* permet la sélection par l'utilisateur d'une liste de recettes (personnalisée ou filtrée par critères) et de calculer, d'afficher puis sauvegarder les quantités de matériaux/cristaux et des points de récoltes nécessaires à leur réalisation.

Exemple de configuration :

```json
    "gestionInventaire": {
        "activer": true,
        "fichierRecettesEntree": "Recettes.csv",
        "fichierRecoltesEntree": "Recoltes.csv",
        "fichierSortie": "Inventaire.txt",
        "filtres": {}
    }
```

Il convient de modifier la configuration afin de spécifier notamment les recettes à considérer.

Exemple pour les équipements d'artisans de niveau 50 :

```json
        "filtres": {
            "nom": ["Calot de patricien",
                    "Boléro de patricien",
                    "Gants de patricien",
                    "Bas-de-corps de patricien",
                    "Guêtres de patricien"],
```

Exemple pour les recettes de tanneur et de couturier entre les niveaux 1 et 10 :

```json
        "filtres": {
            "classe": ["Tanneur", "Couturier"],
            "niveau": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
```

Les critères disponibles sont les suivants : *nom*, *classe*, *niveau*, *livre*, *categorie*, *totalFabrique*, *difficulte*, *solidite*, *qualiteMaximum*, *qualite* et *degre* (les critères *materiaux*, *cristaux* et *conditions* seront disponibles prochainement).

## 4. Informations

L'application est en version 3.0 au 3 février 2021 et réalisée par [Alexis Foerster](mailto:alexis.foerster@gmail.com), joueur du personnage [Yuna Hikari](https://fr.finalfantasyxiv.com/lodestone/character/8095216/).
