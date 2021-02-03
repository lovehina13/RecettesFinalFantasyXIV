# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Donnees/Lieu.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'un lieu et d'un ensemble de lieux
# ==================================================================================================

import distutils.util
from UtilitairesFinalFantasyXIV.Structure.Element import SousElement
from UtilitairesFinalFantasyXIV.Structure.Ensemble import SousEnsemble


class Lieu(SousElement):

    def __init__(self, nom=str(), zone=str(), region=str(), niveau=int(), intact=bool(),
                 ephemere=bool()):
        super().__init__(nom)
        self.zone = zone
        self.region = region
        self.niveau = niveau
        self.intact = intact
        self.ephemere = ephemere

    def identifiant(self):
        return str("%s:%s" % (self.nom, self.niveau))

    def texteUtilisateur(self):

        def _temporaire(intact, ephemere):
            return str(" (temporaire)") if intact or ephemere else str()

        return str("%s - %s - %s: %s%s" % (self.region, self.zone, self.nom, self.niveau,
                                           _temporaire(self.intact, self.ephemere)))

    @staticmethod
    def creer(texte):
        items = texte.split(":")
        return Lieu(items[0], items[1], items[2], int(items[3]) if items[3].isdigit() else items[3],
                    bool(distutils.util.strtobool(items[4])),
                    bool(distutils.util.strtobool(items[5])))


class Lieux(SousEnsemble):

    @staticmethod
    def creer(texte):
        sousEnsemble = Lieux()
        for item in texte.split(","):
            sousEnsemble.ajouter(Lieu.creer(item) if item else None)
        return sousEnsemble
