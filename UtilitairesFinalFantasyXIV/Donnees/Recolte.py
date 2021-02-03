# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Donnees/Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'une récolte et d'un ensemble de récoltes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Lieu import Lieux
from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Recolte(Element):

    def __init__(self, nom=str(), classe=str(), sousClasse=str(), niveau=int(), categorie=str(),
                 pointsRecolte=None):
        super().__init__(nom)
        self.classe = classe
        self.sousClasse = sousClasse
        self.niveau = niveau
        self.categorie = categorie
        self.pointsRecolte = pointsRecolte if isinstance(pointsRecolte, Lieux) else Lieux()

    def identifiant(self):
        return str("%s:%s" % (self.nom, self.sousClasse))

    @staticmethod
    def creer(texte):
        items = texte.split("|")
        return Recolte(items[0], items[1], items[2], int(items[3]), items[4], Lieux.creer(items[5]))

    # Libellés
    libelles = [str("Nom"), str("Classe"), str("Sous-classe"), str("Niveau"), str("Catégorie"),
                str("Points de récolte")]


class Recoltes(Ensemble):

    @staticmethod
    def creer(texte):
        ensemble = Recoltes()
        for item in texte.split("\n"):
            ensemble.ajouter(Recolte.creer(item) if item else None)
        return ensemble
