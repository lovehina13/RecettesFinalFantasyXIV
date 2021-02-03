# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Structure/Page.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'une page, d'une page d'élément et d'une page d'ensemble
# ==================================================================================================

import urllib.request
from bs4 import BeautifulSoup
from UtilitairesFinalFantasyXIV.Structure.Element import Element


class Page(Element):

    def __init__(self, nom=str(), adresse=str()):
        super().__init__(nom)
        self.adresse = adresse
        self.texte = None
        self.soup = None

    def lire(self):
        # Note: Implémenter une nouvelle tentative en cas d'échec ?
        self.texte = urllib.request.urlopen(self.adresse).read()
        self.soup = BeautifulSoup(self.texte, "html.parser")

    def extraire(self):
        pass  # Note: Implémenter l'extraction pour chaque page

    def recuperer(self):
        pass  # Note: Implémenter la récupération pour chaque page

    def executer(self):
        self.lire()
        self.extraire()
        return self.recuperer()

    def afficher(self):
        print(self.soup.prettify("utf-8"))


class PageElement(Page):

    def __init__(self, nom=str(), adresse=str()):
        super().__init__(nom, adresse)
        self.element = None

    def recuperer(self):
        return self.element


class PageEnsemble(Page):

    def __init__(self, nom=str(), adresse=str()):
        super().__init__(nom, adresse)
        self.ensemble = None

    def recuperer(self):
        return self.ensemble
