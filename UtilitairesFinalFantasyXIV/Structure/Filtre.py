# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Structure/Filtre.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'un filtre et d'un ensemble de filtres
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Filtre(Element):

    def __init__(self, nom=str(), valeurs=None):
        super().__init__(nom)
        self.valeurs = valeurs


class Filtres(Ensemble):

    def valider(self, element):
        for _, filtre in self.elements.items():
            if filtre.valeurs is not None and getattr(element, filtre.nom) not in filtre.valeurs:
                return False
        return True

    @staticmethod
    def filtres(dictionnaire):
        filtres = Filtres()
        for nom, valeur in dictionnaire.items():
            if len(valeur) > 0:
                filtres.ajouter(Filtre(nom, valeur))
        return filtres
