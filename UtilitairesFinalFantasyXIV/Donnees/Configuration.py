# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Donnees/Configuration.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition de la configuration de l'application
# ==================================================================================================

import copy
from UtilitairesFinalFantasyXIV.Donnees.Personnage import Personnage
from UtilitairesFinalFantasyXIV.Donnees.Recette import Recette
from UtilitairesFinalFantasyXIV.Donnees.Recolte import Recolte
from UtilitairesFinalFantasyXIV.Structure.Configuration import Configuration


class ConfigurationPagePersonnages:

    # Paramètres
    activer = str("activer")
    compagnieLibre = str("compagnieLibre")
    nombrePages = str("nombrePages")
    fichierSortie = str("fichierSortie")

    # Valeurs par défaut
    defaut = {activer: False, compagnieLibre: str("9233364398528028107"), nombrePages: 1,
              fichierSortie: str("Personnages.csv")}


class ConfigurationPageRecettes:

    # Paramètres
    activer = str("activer")
    nombrePages = str("nombrePages")
    fichierSortie = str("fichierSortie")

    # Valeurs par défaut
    defaut = {activer: False, nombrePages: 185, fichierSortie: str("Recettes.csv")}


class ConfigurationPageRecoltes:

    # Paramètres
    activer = str("activer")
    nombrePages = str("nombrePages")
    fichierSortie = str("fichierSortie")

    # Valeurs par défaut
    defaut = {activer: False, nombrePages: 18, fichierSortie: str("Recoltes.csv")}


class ConfigurationGestionPersonnages:

    # Paramètres
    activer = str("activer")
    fichierEntree = str("fichierEntree")
    fichierSortie = str("fichierSortie")
    filtres = str("filtres")
    trier = str("trier")
    formatUtilisateur = str("formatUtilisateur")

    # Valeurs par défaut
    filtresDefaut = {item: list() for item, _ in Personnage().__dict__.items()}
    defaut = {activer: False, fichierEntree: str("Personnages.csv"),
              fichierSortie: str("Personnages.txt"), filtres: filtresDefaut, trier: True,
              formatUtilisateur: True}


class ConfigurationGestionRecettes:

    # Paramètres
    activer = str("activer")
    fichierEntree = str("fichierEntree")
    fichierSortie = str("fichierSortie")
    filtres = str("filtres")
    trier = str("trier")
    formatUtilisateur = str("formatUtilisateur")

    # Valeurs par défaut
    filtresDefaut = {item: list() for item, _ in Recette().__dict__.items()}
    defaut = {activer: False, fichierEntree: str("Recettes.csv"),
              fichierSortie: str("Recettes.txt"), filtres: filtresDefaut, trier: True,
              formatUtilisateur: True}


class ConfigurationGestionRecoltes:

    # Paramètres
    activer = str("activer")
    fichierEntree = str("fichierEntree")
    fichierSortie = str("fichierSortie")
    filtres = str("filtres")
    trier = str("trier")
    formatUtilisateur = str("formatUtilisateur")

    # Valeurs par défaut
    filtresDefaut = {item: list() for item, _ in Recolte().__dict__.items()}
    defaut = {activer: False, fichierEntree: str("Recoltes.csv"),
              fichierSortie: str("Recoltes.txt"), filtres: filtresDefaut, trier: True,
              formatUtilisateur: True}


class ConfigurationGestionInventaire:

    # Paramètres
    activer = str("activer")
    fichierRecettesEntree = str("fichierRecettesEntree")
    fichierRecoltesEntree = str("fichierRecoltesEntree")
    fichierSortie = str("fichierSortie")
    filtres = str("filtres")

    # Valeurs par défaut
    filtresDefaut = {item: list() for item, _ in Recette().__dict__.items()}
    defaut = {activer: True, fichierRecettesEntree: str("Recettes.csv"),
              fichierRecoltesEntree: str("Recoltes.csv"), fichierSortie: str("Inventaire.txt"),
              filtres: filtresDefaut}


class ConfigurationPrincipale(Configuration):

    def __init__(self, elements=None, fichier=str()):
        super().__init__(elements, fichier)
        self.elements = copy.deepcopy(ConfigurationPrincipale.defaut)

    # Paramètres
    fichierEntree = str("Configuration.json")
    pagePersonnages = str("pagePersonnages")
    pageRecettes = str("pageRecettes")
    pageRecoltes = str("pageRecoltes")
    gestionPersonnages = str("gestionPersonnages")
    gestionRecettes = str("gestionRecettes")
    gestionRecoltes = str("gestionRecoltes")
    gestionInventaire = str("gestionInventaire")

    # Valeurs par défaut
    defaut = {pagePersonnages: ConfigurationPagePersonnages.defaut,
              pageRecettes: ConfigurationPageRecettes.defaut,
              pageRecoltes: ConfigurationPageRecoltes.defaut,
              gestionPersonnages: ConfigurationGestionPersonnages.defaut,
              gestionRecettes: ConfigurationGestionRecettes.defaut,
              gestionRecoltes: ConfigurationGestionRecoltes.defaut,
              gestionInventaire: ConfigurationGestionInventaire.defaut}
