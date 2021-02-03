# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Donnees/Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'un personnage et d'un ensemble de personnages
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Classe import Classes
from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Personnage(Element):

    def __init__(self, nom=str(), titre=str(), serveur=str(), race=str(), ethnie=str(), sexe=str(),
                 dateNaissance=str(), divinite=str(), citeDepart=str(), grandeCompagnie=str(),
                 rang=str(), compagnieLibre=str(), classes=None):
        super().__init__(nom)
        self.titre = titre
        self.serveur = serveur
        self.race = race
        self.ethnie = ethnie
        self.sexe = sexe
        self.dateNaissance = dateNaissance
        self.divinite = divinite
        self.citeDepart = citeDepart
        self.grandeCompagnie = grandeCompagnie
        self.rang = rang
        self.compagnieLibre = compagnieLibre
        self.classes = classes if isinstance(classes, Classes) else Classes()

    def identifiant(self):
        return str("%s:%s" % (self.nom, self.serveur))

    @staticmethod
    def creer(texte):
        items = texte.split("|")
        return Personnage(items[0], items[1], items[2], items[3], items[4], items[5], items[6],
                          items[7], items[8], items[9], items[10], items[11],
                          Classes.creer(items[12]))

    # Libellés
    libelles = [str("Nom"), str("Titre"), str("Serveur"), str("Race"), str("Ethnie"), str("Sexe"),
                str("Date de naissance"), str("Divinité"), str("Cité de départ"),
                str("Grande compagnie"), str("Rang"), str("Compagnie libre"), str("Classes")]


class Personnages(Ensemble):

    @staticmethod
    def creer(texte):
        ensemble = Personnages()
        for item in texte.split("\n"):
            ensemble.ajouter(Personnage.creer(item) if item else None)
        return ensemble
