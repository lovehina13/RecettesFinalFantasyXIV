# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Traitements/Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition des traitements relatifs aux récoltes
# ==================================================================================================

import os
from UtilitairesFinalFantasyXIV.Collections.Recolte import CollectionRecoltes
from UtilitairesFinalFantasyXIV.Pages.Recolte import PageRecolte, PageRecoltes
from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPageRecolte(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        self.afficher("Traitement de la récolte %d sur %d" % (self.compteur, self.nombre))
        open(self.fichier, "a", encoding="utf-8").write(PageRecolte(self.donnee).executer().texte() + "\n")


class TraitementPageRecoltes(Traitement):

    def __init__(self, nombre=int(), fichier=str()):
        super().__init__(None)
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        if os.path.exists(self.fichier):
            os.remove(self.fichier)
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de récoltes %d sur %d" % (item + 1, self.nombre))
            pages += PageRecoltes(str("%d" % (item + 1))).executer().lister()
        for item, page in enumerate(pages):
            TraitementPageRecolte(page.nom, item + 1, len(pages), self.fichier).executer()


class TraitementCollectionRecoltes(Traitement):

    def __init__(self, fichier=str()):
        super().__init__(None)
        self.fichier = fichier
        self.collection = None

    def executer(self):
        self.collection = CollectionRecoltes(None, self.fichier)
        self.collection.charger()


class TraitementGestionRecoltes(TraitementCollectionRecoltes):

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
        self.collectionOut = CollectionRecoltes(None, self.fichierOut)
        items = self.collection.lister(self.filtres)
        if self.tri:
            items = sorted(items, key=lambda item: (item.nom, item.classe, item.sousClasse))
        for item in items:
            self.collectionOut.ajouter(item)
            self.afficher(item.texte() if not self.utilisateur else item.texteUtilisateur())
        if not self.utilisateur:
            self.collectionOut.sauver()
        else:
            self.collectionOut.sauverUtilisateur()
