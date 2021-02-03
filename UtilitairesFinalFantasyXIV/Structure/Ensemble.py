# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Structure/Ensemble.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'un ensemble et d'un sous-ensemble
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import Element


class Ensemble:

    def __init__(self, elements=None):
        self.elements = dict()
        if isinstance(elements, dict):
            for _, element in elements.items():
                self.ajouter(element)

    def ajouter(self, element):
        if isinstance(element, Element):
            self.elements[element.identifiant()] = element

    def recuperer(self, identifiant):
        return self.elements[identifiant] if identifiant in self.elements else None

    def lister(self, filtres=None):
        # Note: Obligatoire de définir un import local pour contourner l'import cyclique
        from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
        filtres = filtres if isinstance(filtres, Filtres) else Filtres()
        return [element for _, element in self.elements.items() if filtres.valider(element)]

    def unicite(self):
        # Note: Permet d'identifier les éléments par leurs noms et de supprimer ainsi les doublons
        ensemble = Ensemble()
        for _, element in self.elements.items():
            ensemble.elements[element.nom] = element
        return ensemble

    def texte(self):
        # Note: Réimplémenter le format texte pour chaque ensemble si nécessaire
        return "\n".join([element.texte() for _, element in self.elements.items()])

    def texteUtilisateur(self):
        # Note: Réimplémenter le format texte utilisateur pour chaque ensemble si nécessaire
        return ", ".join([element.texteUtilisateur() for _, element in self.elements.items()])

    @staticmethod
    def creer(texte):
        return Ensemble(texte)  # Note: Implémenter la création pour chaque ensemble


class SousEnsemble(Ensemble):

    def texte(self):
        # Note: Réimplémenter le format texte pour chaque sous-ensemble si nécessaire
        return ",".join([element.texte() for _, element in self.elements.items()])

    @staticmethod
    def creer(texte):
        return SousEnsemble(texte)  # Note: Implémenter la création pour chaque sous-ensemble
