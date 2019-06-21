# coding: utf-8

# ==============================================================================
# Name        : RecuperationPersonnages.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.7 (21/06/2019)
# Description : Récupération des personnages
# ==============================================================================


class LecteurPagePersonnages(object):

    def __init__(self):
        self.adressesPagesPersonnages = []

    def traitement(self, texteHTML):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(texteHTML, "html.parser")
        for item in soup.find_all("a", {"class": "entry__bg"}):
            adressePagePersonnage = "http://fr.finalfantasyxiv.com%s" % (item.get("href"))
            self.adressesPagesPersonnages.append(adressePagePersonnage)


class LecteurPagePersonnage(object):

    def __init__(self):
        from Personnages import Personnage
        self.personnage = Personnage()

    def traitement(self, texteHTML):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(texteHTML, "html.parser")
        self.personnage.nom = soup.find("p", {"class": "frame__chara__name"}).contents[0].strip()
        self.personnage.titre = soup.find("p", {"class": "frame__chara__title"}).contents[0].strip() if soup.find("p", {"class": "frame__chara__title"}) is not None else str()
        self.personnage.serveur = soup.find("p", {"class": "frame__chara__world"}).contents[1].strip()
        self.personnage.race = soup.find_all("p", {"class": "character-block__name"})[0].contents[0].strip()
        self.personnage.ethnie = soup.find_all("p", {"class": "character-block__name"})[0].contents[2].strip().split("/")[0].strip()
        self.personnage.sexe = soup.find_all("p", {"class": "character-block__name"})[0].contents[2].strip().split("/")[1].strip()
        self.personnage.dateNaissance = soup.find("p", {"class": "character-block__birth"}).contents[0].strip()
        self.personnage.divinite = soup.find_all("p", {"class": "character-block__name"})[1].contents[0].strip()
        self.personnage.citeDepart = soup.find_all("p", {"class": "character-block__name"})[2].contents[0].strip()
        self.personnage.grandeCompagnie = soup.find_all("p", {"class": "character-block__name"})[3].contents[0].strip() if len(soup.find_all("p", {"class": "character-block__name"})) > 3 else str()
        self.personnage.compagnieLibre = soup.find("div", {"class": "character__freecompany__name"}).contents[3].contents[0].contents[0].strip()
        if self.personnage.sexe == u"♂":
            self.personnage.sexe = u"Homme"
        elif self.personnage.sexe == u"♀":
            self.personnage.sexe = u"Femme"
        for item in soup.find_all("img", {"class": "js__tooltip"}):
            classe = item.attrs["data-tooltip"].strip()
            if u"Gladiateur" in classe or u"Paladin" in classe:
                classe = u"Paladin"
            elif u"Maraudeur" in classe or u"Guerrier" in classe:
                classe = u"Guerrier"
            elif u"Élémentaliste" in classe or u"Mage blanc" in classe:
                classe = u"Mage blanc"
            elif u"Pugiliste" in classe or u"Moine" in classe:
                classe = u"Moine"
            elif u"Maître d'hast" in classe or u"Chevalier dragon" in classe:
                classe = u"Chevalier dragon"
            elif u"Surineur" in classe or u"Ninja" in classe:
                classe = u"Ninja"
            elif u"Archer" in classe or u"Barde" in classe:
                classe = u"Barde"
            elif u"Occultiste" in classe or u"Mage noir" in classe:
                classe = u"Mage noir"
            elif u"Arcaniste" in classe or u"Invocateur" in classe:
                classe = u"Invocateur"
            elif u"Mage bleu" in classe:
                classe = u"Mage bleu"
            if len(item.parent.contents) > 1:
                niveau = int(item.parent.contents[1].strip()) if item.parent.contents[1].strip() != "-" else 0
                self.personnage.classes[classe] = niveau


def recupererPersonnages(numeroCompagnieLibre, nomFichierPersonnages):

    from urllib2 import urlopen
    import sys

    # Récupération des pages des personnages
    nombrePagesPersonnages = 1
    adressesPagesPersonnages = []
    for numeroPagePersonnages in range(1, nombrePagesPersonnages + 1):
        print "Traitement de la liste de personnages %d sur %d" % (numeroPagePersonnages, nombrePagesPersonnages)
        adressePagePersonnages = "http://fr.finalfantasyxiv.com/lodestone/freecompany/%s/member/?page=%d" % (numeroCompagnieLibre, numeroPagePersonnages)
        texteHTML = "".join(urlopen(adressePagePersonnages).readlines())
        lecteurPagePersonnages = LecteurPagePersonnages()
        lecteurPagePersonnages.traitement(texteHTML)
        for adressePagePersonnage in lecteurPagePersonnages.adressesPagesPersonnages:
            adressesPagesPersonnages.append(adressePagePersonnage)
        sys.stdout.flush()

    # Récupération des personnages
    nombrePersonnages = len(adressesPagesPersonnages)
    fichierPersonnages = open(nomFichierPersonnages, "w")
    for adressePagePersonnage in adressesPagesPersonnages:
        numeroPersonnage = adressesPagesPersonnages.index(adressePagePersonnage) + 1
        print "Traitement du personnage %d sur %d" % (numeroPersonnage, nombrePersonnages)
        texteHTML = "".join(urlopen(adressePagePersonnage).readlines())
        lecteurPagePersonnage = LecteurPagePersonnage()
        lecteurPagePersonnage.traitement(texteHTML)
        personnageTexteBrut = lecteurPagePersonnage.personnage.getTexteBrut()
        fichierPersonnages.write(personnageTexteBrut.encode("utf-8") + "\n")
        fichierPersonnages.flush()
        sys.stdout.flush()
    fichierPersonnages.close()


if __name__ == "__main__":

    import sys
    numeroCompagnieLibre = sys.argv[1] if len(sys.argv) > 1 else None
    nomFichierPersonnages = sys.argv[2] if len(sys.argv) > 2 else None
    recupererPersonnages(numeroCompagnieLibre, nomFichierPersonnages)
