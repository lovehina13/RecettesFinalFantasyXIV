# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Donnees/Objet.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'un objet et d'un ensemble d'objets
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import SousElement
from UtilitairesFinalFantasyXIV.Structure.Ensemble import SousEnsemble


class Objet(SousElement):

    def __init__(self, nom=str(), quantite=int()):
        super().__init__(nom)
        self.quantite = quantite

    @staticmethod
    def creer(texte):
        items = texte.split(":")
        return Objet(items[0], int(items[1]))

    def texteUtilisateur(self):
        return str("%d %s" % (self.quantite, self.nom))


class Objets(SousEnsemble):

    @staticmethod
    def creer(texte):
        sousEnsemble = Objets()
        for item in texte.split(","):
            sousEnsemble.ajouter(Objet.creer(item) if item else None)
        return sousEnsemble
