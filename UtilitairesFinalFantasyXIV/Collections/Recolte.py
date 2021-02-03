# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Collection/Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'une collection de récoltes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Recolte import Recoltes
from UtilitairesFinalFantasyXIV.Structure.Collection import Collection


class CollectionRecoltes(Collection, Recoltes):

    def charger(self):
        self.elements = Recoltes.creer(open(self.fichier, "r", encoding="utf-8").read()).elements

    def sauver(self):
        fichier = open(self.fichier, "w", encoding="utf-8")
        for _, element in self.elements.items():
            fichier.write(element.texte() + "\n")

    def sauverUtilisateur(self):
        fichier = open(self.fichier, "w", encoding="utf-8")
        for _, element in self.elements.items():
            fichier.write(element.texteUtilisateur() + "\n\n")
