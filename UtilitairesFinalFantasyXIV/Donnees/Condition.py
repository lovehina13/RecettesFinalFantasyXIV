# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Donnees/Condition.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'une condition et d'un ensemble de conditions
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import SousElement
from UtilitairesFinalFantasyXIV.Structure.Ensemble import SousEnsemble


class Condition(SousElement):

    @staticmethod
    def creer(texte):
        return Condition(texte)


class Conditions(SousEnsemble):

    @staticmethod
    def creer(texte):
        sousEnsemble = Conditions()
        for item in texte.split(","):
            sousEnsemble.ajouter(Condition.creer(item) if item else None)
        return sousEnsemble
