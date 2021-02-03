# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Collection/Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'une collection de personnages
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Personnage import Personnages
from UtilitairesFinalFantasyXIV.Structure.Collection import Collection


class CollectionPersonnages(Collection, Personnages):

    def charger(self):
        self.elements = Personnages.creer(open(self.fichier, "r", encoding="utf-8").read()).elements

    def sauver(self):
        fichier = open(self.fichier, "w", encoding="utf-8")
        for _, element in self.elements.items():
            fichier.write(element.texte() + "\n")

    def sauverUtilisateur(self):
        fichier = open(self.fichier, "w", encoding="utf-8")
        for _, element in self.elements.items():
            fichier.write(element.texteUtilisateur() + "\n\n")
