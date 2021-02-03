# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Structure/Configuration.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'une configuration
# ==================================================================================================

import json
from UtilitairesFinalFantasyXIV.Structure.Collection import Collection


class Configuration(Collection):

    def charger(self):
        self.elements = json.loads(open(self.fichier, "r", encoding="utf-8").read())

    def sauver(self):
        open(self.fichier, "w", encoding="utf-8").write(json.dumps(self.elements, indent=4) + "\n")

    def afficher(self):
        print(self.elements)
