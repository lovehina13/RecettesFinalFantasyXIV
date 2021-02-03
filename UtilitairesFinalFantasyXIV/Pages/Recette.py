# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Pages/Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition des pages relatives aux recettes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Condition import Condition
from UtilitairesFinalFantasyXIV.Donnees.Objet import Objet
from UtilitairesFinalFantasyXIV.Donnees.Recette import Recette, Recettes
from UtilitairesFinalFantasyXIV.Structure.Page import PageElement, PageEnsemble


class PageRecette(PageElement):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/recipe/%s/" % nom)

    def extraire(self):

        def _cristal(objet):
            cristaux = [str("Éclat de feu"), str("Éclat de glace"), str("Éclat de vent"),
                        str("Éclat de terre"), str("Éclat de foudre"), str("Éclat d'eau"),
                        str("Cristal de feu"), str("Cristal de glace"), str("Cristal de vent"),
                        str("Cristal de terre"), str("Cristal de foudre"), str("Cristal d'eau"),
                        str("Agrégat de feu"), str("Agrégat de glace"), str("Agrégat de vent"),
                        str("Agrégat de terre"), str("Agrégat de foudre"), str("Agrégat d'eau")]
            return objet in cristaux

        def _condition(condition):
            return condition.replace("≥", ">=").replace("≧", ">=")

        self.element = Recette()
        self.element.nom = self.soup.find("h2", {"class": "db-view__item__text__name"}).contents[0].strip()
        self.element.classe = self.soup.find("p", {"class": "db-view__item__text__job_name"}).contents[0].strip()
        self.element.niveau = int(self.soup.find("span", {"class": "db-view__item__text__level__num"}).contents[0].strip())
        if self.soup.find("p", {"class": "db-view__recipe__text__book_name"}):
            self.element.livre = self.soup.find("p", {"class": "db-view__recipe__text__book_name"}).contents[0].strip()
        self.element.categorie = self.soup.find("p", {"class": "db-view__recipe__text__category"}).contents[0].strip()
        self.element.totalFabrique = int(self.soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[1].contents[1].strip())
        self.element.difficulte = int(self.soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[2].contents[1].strip())
        self.element.solidite = int(self.soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[3].contents[1].strip())
        self.element.qualiteMaximum = int(self.soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[4].contents[1].strip())
        self.element.qualite = self.soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[5].contents[1].strip()
        for item in self.soup.find_all("div", {"class": "db-view__data__reward__item__name"}):
            if int(item.contents[1].attrs["data-depth"]) == 1:
                objet = Objet()
                objet.nom = item.contents[3].contents[1].contents[0].contents[0].strip()
                objet.quantite = int(item.contents[1].contents[0].contents[0].strip())
                if _cristal(objet.nom):
                    self.element.cristaux.ajouter(objet)
                else:
                    self.element.materiaux.ajouter(objet)
        for item in self.soup.find("dl", {"class": "db-view__recipe__crafting_conditions"}):
            if item.name == str("dd"):
                condition = Condition()
                condition.nom = _condition(item.contents[0].strip())
                self.element.conditions.ajouter(condition)
        # Note: Degré non récupéré car inconnu


class PageRecettes(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/recipe/?page=%s" % nom)

    def extraire(self):
        self.ensemble = Recettes()
        for item in self.soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            self.ensemble.ajouter(PageRecette(item.get("href").split("/")[5]))
