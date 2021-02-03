# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Pages/Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition des pages relatives aux personnages
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Classe import Classe, Classes
from UtilitairesFinalFantasyXIV.Donnees.Personnage import Personnage, Personnages
from UtilitairesFinalFantasyXIV.Structure.Page import PageElement, PageEnsemble


class PagePersonnage(PageElement):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/character/%s/" % nom)

    def extraire(self):

        def _sexe(sexe):
            sexes = {str("♂"): str("Homme"), str("♀"): str("Femme")}
            return sexes[sexe] if sexe in sexes else None

        def _classe(classe):
            classes = {Classe.PLD: str("Gladiateur"), Classe.GUE: str("Maraudeur"),
                       Classe.MBL: str("Élémentaliste"), Classe.MOI: str("Pugiliste"),
                       Classe.DRG: str("Maître d'hast"), Classe.NIN: str("Surineur"),
                       Classe.BRD: str("Archer"), Classe.MNO: str("Occultiste"),
                       Classe.INV: str("Arcaniste")}
            return classes[classe] if classe in classes else None

        self.element = Personnage()
        self.element.nom = self.soup.find("p", {"class": "frame__chara__name"}).contents[0].strip()
        if self.soup.find("p", {"class": "frame__chara__title"}):
            self.element.titre = self.soup.find("p", {"class": "frame__chara__title"}).contents[0].strip()
        self.element.serveur = self.soup.find("p", {"class": "frame__chara__world"}).contents[1].strip()
        self.element.race = self.soup.find_all("p", {"class": "character-block__name"})[0].contents[0].strip()
        self.element.ethnie = self.soup.find_all("p", {"class": "character-block__name"})[0].contents[2].split("/")[0].strip()
        self.element.sexe = _sexe(self.soup.find_all("p", {"class": "character-block__name"})[0].contents[2].split("/")[1].strip())
        self.element.dateNaissance = self.soup.find("p", {"class": "character-block__birth"}).contents[0].strip()
        self.element.divinite = self.soup.find_all("p", {"class": "character-block__name"})[1].contents[0].strip()
        self.element.citeDepart = self.soup.find_all("p", {"class": "character-block__name"})[2].contents[0].strip()
        if len(self.soup.find_all("p", {"class": "character-block__name"})) > 3:
            self.element.grandeCompagnie = self.soup.find_all("p", {"class": "character-block__name"})[3].contents[0].split("/")[0].strip()
            self.element.rang = self.soup.find_all("p", {"class": "character-block__name"})[3].contents[0].split("/")[1].strip()
        if self.soup.find("div", {"class": "character__freecompany__name"}):
            self.element.compagnieLibre = self.soup.find("div", {"class": "character__freecompany__name"}).contents[1].contents[0].contents[0].strip()
        for item in self.soup.find_all("img", {"class": "js__tooltip"}):
            for _, classeBase in Classes.classesBase.items():
                if classeBase.nom in item.attrs["data-tooltip"] or _classe(classeBase.nom) and _classe(classeBase.nom) in item.attrs["data-tooltip"]:
                    classe = Classe()
                    classe.nom = classeBase.nom
                    classe.categorie = classeBase.categorie
                    if item.parent.contents[1].strip().isdigit():
                        classe.niveau = int(item.parent.contents[1].strip())
                    self.element.classes.ajouter(classe)


class PagePersonnages(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/freecompany/%s/member/?page=%s" % (nom.split(":")[0], nom.split(":")[1]))

    def extraire(self):
        self.ensemble = Personnages()
        for item in self.soup.find_all("a", {"class": "entry__bg"}):
            self.ensemble.ajouter(PagePersonnage(item.get("href").split("/")[3]))
