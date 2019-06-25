# coding: utf-8

# ==============================================================================
# Name        : RecuperationRecoltes.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.8 (25/06/2019)
# Description : Récupération des récoltes
# ==============================================================================


class LecteurPageRecoltes(object):

    def __init__(self):
        self.adressesPagesRecoltes = []

    def traitement(self, texteHTML):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(texteHTML, "html.parser")
        for item in soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            adressePageRecolte = "http://fr.finalfantasyxiv.com%s" % (item.get("href"))
            self.adressesPagesRecoltes.append(adressePageRecolte)


class LecteurPageRecolte(object):

    def __init__(self):
        from Recoltes import Recolte
        self.recolte = Recolte()

    def traitement(self, texteHTML):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(texteHTML, "html.parser")
        self.recolte.nom = soup.find("h2", {"class": "db-view__item__text__name"}).contents[0].strip()
        self.recolte.sousClasse = soup.find("p", {"class": "db-view__item__text__job_name"}).contents[0].strip()
        self.recolte.niveau = int(soup.find("span", {"class": "db-view__item__text__level__num"}).contents[0].strip())
        self.recolte.categorie = soup.find("p", {"class": "db-view__gathering__text__category"}).contents[0].strip()
        if self.recolte.sousClasse in [u"Extraction de minerai", u"Extraction de pierre"]:
            self.recolte.classe = u"Mineur"
        elif self.recolte.sousClasse in [u"Coupe", u"Fauche"]:
            self.recolte.classe = u"Botaniste"
        for item in soup.find_all("dl", {"class": "db-view__gathering__point"}):
            zone = item.contents[1].contents[0].strip()
            sousZone = " ".join(item.contents[3].contents[0].strip().replace("\n", " ").replace("\t", "").split()[2:])
            niveauSousZone = " ".join(item.contents[3].contents[0].strip().replace("\n", " ").replace("\t", "").split()[:2])
            pointRecolte = "%s - %s (%s)" % (zone, sousZone, niveauSousZone)
            self.recolte.pointsRecolte.append(pointRecolte)


def recupererRecoltes(nomFichierRecoltes):

    from urllib2 import urlopen
    import sys

    # Récupération des pages des récoltes
    nombrePagesRecoltes = 13
    adressesPagesRecoltes = []
    for numeroPageRecoltes in range(1, nombrePagesRecoltes + 1):
        print "Traitement de la liste de récoltes %d sur %d" % (numeroPageRecoltes, nombrePagesRecoltes)
        adressePageRecoltes = "http://fr.finalfantasyxiv.com/lodestone/playguide/db/gathering/?page=%d" % (numeroPageRecoltes)
        texteHTML = "".join(urlopen(adressePageRecoltes).readlines())
        lecteurPageRecoltes = LecteurPageRecoltes()
        lecteurPageRecoltes.traitement(texteHTML)
        for adressePageRecolte in lecteurPageRecoltes.adressesPagesRecoltes:
            adressesPagesRecoltes.append(adressePageRecolte)
        sys.stdout.flush()

    # Récupération des récoltes
    nombreRecoltes = len(adressesPagesRecoltes)
    fichierRecoltes = open(nomFichierRecoltes, "w")
    for adressePageRecolte in adressesPagesRecoltes:
        numeroRecolte = adressesPagesRecoltes.index(adressePageRecolte) + 1
        print "Traitement de la récolte %d sur %d" % (numeroRecolte, nombreRecoltes)
        texteHTML = "".join(urlopen(adressePageRecolte).readlines())
        lecteurPageRecolte = LecteurPageRecolte()
        lecteurPageRecolte.traitement(texteHTML)
        recolteTexteBrut = lecteurPageRecolte.recolte.getTexteBrut()
        fichierRecoltes.write(recolteTexteBrut.encode("utf-8") + "\n")
        fichierRecoltes.flush()
        sys.stdout.flush()
    fichierRecoltes.close()


if __name__ == "__main__":

    import sys
    nomFichierRecoltes = sys.argv[1] if len(sys.argv) > 1 else None
    recupererRecoltes(nomFichierRecoltes)
