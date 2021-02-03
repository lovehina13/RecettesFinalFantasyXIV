# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Traitements/Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition des traitements relatifs aux personnages
# ==================================================================================================

import os
from UtilitairesFinalFantasyXIV.Collections.Personnage import CollectionPersonnages
from UtilitairesFinalFantasyXIV.Pages.Personnage import PagePersonnage, PagePersonnages
from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPagePersonnage(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        self.afficher("Traitement du personnage %d sur %d" % (self.compteur, self.nombre))
        open(self.fichier, "a", encoding="utf-8").write(PagePersonnage(self.donnee).executer().texte() + "\n")


class TraitementPagePersonnages(Traitement):

    def __init__(self, donnee=str(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        if os.path.exists(self.fichier):
            os.remove(self.fichier)
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de personnages %d sur %d" % (item + 1, self.nombre))
            pages += PagePersonnages(str("%s:%d" % (self.donnee, item + 1))).executer().lister()
        for item, page in enumerate(pages):
            TraitementPagePersonnage(page.nom, item + 1, len(pages), self.fichier).executer()


class TraitementCollectionPersonnages(Traitement):

    def __init__(self, fichier=str()):
        super().__init__(None)
        self.fichier = fichier
        self.collection = None

    def executer(self):
        self.collection = CollectionPersonnages(None, self.fichier)
        self.collection.charger()


class TraitementGestionPersonnages(TraitementCollectionPersonnages):

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
        self.collectionOut = CollectionPersonnages(None, self.fichierOut)
        items = self.collection.lister(self.filtres)
        if self.tri:
            items = sorted(items, key=lambda item: (item.nom, item.serveur))
        for item in items:
            self.collectionOut.ajouter(item)
            self.afficher(item.texte() if not self.utilisateur else item.texteUtilisateur())
        if not self.utilisateur:
            self.collectionOut.sauver()
        else:
            self.collectionOut.sauverUtilisateur()
