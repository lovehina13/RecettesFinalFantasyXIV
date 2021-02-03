# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Pages/Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition des pages relatives aux récoltes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Classe import Classe
from UtilitairesFinalFantasyXIV.Donnees.Lieu import Lieu
from UtilitairesFinalFantasyXIV.Donnees.Recolte import Recolte, Recoltes
from UtilitairesFinalFantasyXIV.Structure.Page import PageElement, PageEnsemble


class PageRecolte(PageElement):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/gathering/%s/" % nom)

    def extraire(self):

        def _classe(sousClasse):
            classes = {str("Extraction de minerai"): Classe.MIN,
                       str("Extraction de pierre"): Classe.MIN, str("Coupe"): Classe.BOT,
                       str("Fauche"): Classe.BOT}
            return classes[sousClasse] if sousClasse in classes else None

        def _simplifier(texte):
            return " ".join(texte.replace("\n", " ").replace("\t", " ").split())

        def _nomLieu(nomNiveauLieu):
            return " ".join(_simplifier(nomNiveauLieu).split()[2:])

        def _niveauLieu(nomNiveauLieu):
            niveau = _simplifier(nomNiveauLieu).split()[1]
            return int(niveau) if niveau.isdigit() else niveau

        self.element = Recolte()
        self.element.nom = self.soup.find("h2", {"class": "db-view__item__text__name"}).contents[0].strip()
        self.element.classe = _classe(self.soup.find("p", {"class": "db-view__item__text__job_name"}).contents[0].strip())
        self.element.sousClasse = self.soup.find("p", {"class": "db-view__item__text__job_name"}).contents[0].strip()
        self.element.niveau = int(self.soup.find("span", {"class": "db-view__item__text__level__num"}).contents[0].strip())
        self.element.categorie = self.soup.find("p", {"class": "db-view__gathering__text__category"}).contents[0].strip()
        for item in self.soup.find("div", {"class": "db-view__gathering__data"}).contents:
            if item.name == str("h5"):
                region = item.contents[0].strip()
            if item.name == str("dl"):
                for item2 in item.contents:
                    if item2.name == str("dd"):
                        lieu = Lieu()
                        lieu.nom = _nomLieu(item2.contents[-1].strip())
                        lieu.zone = item.contents[1].contents[0].strip()
                        lieu.region = region
                        lieu.niveau = _niveauLieu(item2.contents[-1].strip())
                        lieu.intact = str("db-view__gathering__point__01") in item2.contents[1].attrs["class"] if len(item2.contents) > 1 else False
                        lieu.ephemere = str("db-view__gathering__point__02") in item2.contents[1].attrs["class"] if len(item2.contents) > 1 else False
                        self.element.pointsRecolte.ajouter(lieu)


class PageRecoltes(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/gathering/?page=%s" % nom)

    def extraire(self):
        self.ensemble = Recoltes()
        for item in self.soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            self.ensemble.ajouter(PageRecolte(item.get("href").split("/")[5]))
