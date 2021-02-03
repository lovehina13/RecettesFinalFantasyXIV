# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Traitements/Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition des traitements relatifs aux recettes
# ==================================================================================================

import os
from UtilitairesFinalFantasyXIV.Collections.Recette import CollectionRecettes
from UtilitairesFinalFantasyXIV.Pages.Recette import PageRecette, PageRecettes
from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPageRecette(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        self.afficher("Traitement de la recette %d sur %d" % (self.compteur, self.nombre))
        open(self.fichier, "a", encoding="utf-8").write(PageRecette(self.donnee).executer().texte() + "\n")


class TraitementPageRecettes(Traitement):

    def __init__(self, nombre=int(), fichier=str()):
        super().__init__(None)
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        if os.path.exists(self.fichier):
            os.remove(self.fichier)
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de recettes %d sur %d" % (item + 1, self.nombre))
            pages += PageRecettes(str("%d" % (item + 1))).executer().lister()
        for item, page in enumerate(pages):
            TraitementPageRecette(page.nom, item + 1, len(pages), self.fichier).executer()
        # Note: Calcul des degrés des recettes
        collection = CollectionRecettes(None, self.fichier)
        collection.charger()
        unicite = collection.unicite()
        for _, element in collection.elements.items():
            element.degre = element.calculerDegre(unicite)
        collection.sauver()


class TraitementCollectionRecettes(Traitement):

    def __init__(self, fichier=str()):
        super().__init__(None)
        self.fichier = fichier
        self.collection = None

    def executer(self):
        self.collection = CollectionRecettes(None, self.fichier)
        self.collection.charger()


class TraitementGestionRecettes(TraitementCollectionRecettes):

    def __init__(self, fichierIn=str(), fichierOut=str(), filtres=None, tri=False,
                 utilisateur=False):
        super().__init__(fichierIn)
        self.fichierOut = fichierOut
        self.collectionOut = None
        self.filtres = filtres if isinstance(filtres, Filtres) else Filtres()
        self.tri = tri
        self.utilisateur = utilisateur

    def executer(self):
        super().executer()
        self.collectionOut = CollectionRecettes(None, self.fichierOut)
        items = self.collection.lister(self.filtres)
        if self.tri:
            items = sorted(items, key=lambda item: (item.nom, item.classe))
        for item in items:
            self.collectionOut.ajouter(item)
            self.afficher(item.texte() if not self.utilisateur else item.texteUtilisateur())
        if not self.utilisateur:
            self.collectionOut.sauver()
        else:
            self.collectionOut.sauverUtilisateur()
