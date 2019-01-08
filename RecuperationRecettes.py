# coding: utf-8

# ==============================================================================
# Name        : RecuperationRecettes.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.5 (08/01/2019)
# Description : Récupération des recettes
# ==============================================================================


class LecteurPageRecettes(object):

    def __init__(self):
        self.adressesPagesRecettes = []

    def traitement(self, texteHTML):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(texteHTML, "html.parser")
        for item in soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            adressePageRecette = "http://fr.finalfantasyxiv.com%s" % (item.get("href"))
            self.adressesPagesRecettes.append(adressePageRecette)


class LecteurPageRecette(object):

    def __init__(self):
        from Recettes import Recette
        self.recette = Recette()

    def traitement(self, texteHTML):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(texteHTML, "html.parser")
        self.recette.nom = soup.find("h2", {"class": "db-view__item__text__name"}).contents[0].strip()
        self.recette.classe = soup.find("p", {"class": "db-view__item__text__job_name"}).contents[0].strip()
        self.recette.niveau = int(soup.find("span", {"class": "db-view__item__text__level__num"}).contents[0].strip())
        self.recette.categorie = soup.find("p", {"class": "db-view__recipe__text__category"}).contents[0].strip()
        self.recette.quantite = int(soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[1].contents[1].strip())
        self.recette.difficulte = int(soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[2].contents[1].strip())
        self.recette.solidite = int(soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[3].contents[1].strip())
        self.recette.qualite = int(soup.find("ul", {"class": "db-view__recipe__craftdata"}).contents[4].contents[1].strip())
        self.recette.materiaux = {}
        self.recette.cristaux = {}
        for item in soup.find_all("div", {"class": "db-view__data__reward__item__name"}):
            objet = item.contents[3].contents[1].contents[0].contents[0].strip()
            quantite = int(item.contents[1].contents[0].strip())
            if objet in [u"Éclat de feu", u"Éclat de glace", u"Éclat de vent", u"Éclat de terre",
                         u"Éclat de foudre", u"Éclat d'eau", u"Cristal de feu", u"Cristal de glace",
                         u"Cristal de vent", u"Cristal de terre", u"Cristal de foudre",
                         u"Cristal d'eau", u"Agrégat de feu", u"Agrégat de glace",
                         u"Agrégat de vent", u"Agrégat de terre", u"Agrégat de foudre",
                         u"Agrégat d'eau"]:
                self.recette.cristaux[objet] = quantite
            else:
                self.recette.materiaux[objet] = quantite


def recupererRecettes(nomFichierRecettes):

    from urllib2 import urlopen
    import sys

    # Récupération des pages des recettes
    nombrePagesRecettes = 141
    adressesPagesRecettes = []
    for numeroPageRecettes in range(1, nombrePagesRecettes + 1):
        print "Traitement de la liste de recettes %d sur %d" % (numeroPageRecettes, nombrePagesRecettes)
        adressePageRecettes = "http://fr.finalfantasyxiv.com/lodestone/playguide/db/recipe/?page=%d" % (numeroPageRecettes)
        texteHTML = "".join(urlopen(adressePageRecettes).readlines())
        lecteurPageRecettes = LecteurPageRecettes()
        lecteurPageRecettes.traitement(texteHTML)
        for adressePageRecette in lecteurPageRecettes.adressesPagesRecettes:
            adressesPagesRecettes.append(adressePageRecette)
        sys.stdout.flush()

    # Récupération des recettes
    nombreRecettes = len(adressesPagesRecettes)
    fichierRecettes = open(nomFichierRecettes, "w")
    for adressePageRecette in adressesPagesRecettes:
        numeroRecette = adressesPagesRecettes.index(adressePageRecette) + 1
        print "Traitement de la recette %d sur %d" % (numeroRecette, nombreRecettes)
        texteHTML = "".join(urlopen(adressePageRecette).readlines())
        lecteurPageRecette = LecteurPageRecette()
        lecteurPageRecette.traitement(texteHTML)
        recetteTexteBrut = lecteurPageRecette.recette.getTexteBrut()
        fichierRecettes.write(recetteTexteBrut.encode("utf-8") + "\n")
        fichierRecettes.flush()
        sys.stdout.flush()
    fichierRecettes.close()


if __name__ == "__main__":

    import sys
    nomFichierRecettes = sys.argv[1] if len(sys.argv) > 1 else None
    recupererRecettes(nomFichierRecettes)
