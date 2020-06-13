# coding: utf-8

# ==============================================================================
# Name        : Recoltes.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 2.1 (14/06/2020)
# Description : Définition d'une récolte et d'une liste de récoltes
# ==============================================================================


class Recolte(object):

    def __init__(self, nom=str(), classe=str(), sousClasse=str(), niveau=int(), categorie=str(),
                 pointsRecolte=None):
        if pointsRecolte is None:
            pointsRecolte = []
        self.nom = nom
        self.classe = classe
        self.sousClasse = sousClasse
        self.niveau = niveau
        self.categorie = categorie
        self.pointsRecolte = pointsRecolte

    def getTexteBrut(self):
        patron = "%s;%s;%s;%d;%s;%s"
        texte = patron % (self.nom, self.classe, self.sousClasse, self.niveau, self.categorie,
                          Recolte.pointsRecolteVersTexte(self.pointsRecolte))
        return texte

    def getTexteRiche(self):
        patron = str()
        patron += "Nom: %s\n"
        patron += "Classe: %s\n"
        patron += "Sous-classe: %s\n"
        patron += "Niveau: %d\n"
        patron += "Catégorie: %s\n"
        patron += "Points de récolte: %s\n"
        texte = patron % (self.nom, self.classe, self.sousClasse, self.niveau, self.categorie,
                          Recolte.pointsRecolteVersTexte(self.pointsRecolte))
        return texte

    @staticmethod
    def pointsRecolteVersTexte(pointsRecolte):
        texte = str()
        for pointRecolte in sorted(pointsRecolte):
            texte += "%s, " % (pointRecolte)
        texte = texte.rstrip(", ")
        return texte

    @staticmethod
    def texteVersPointsRecolte(texte):
        pointsRecolte = []
        for element in texte.split(", "):
            pointRecolte = element
            pointsRecolte.append(pointRecolte)
        return pointsRecolte


class ListeRecoltes(object):

    def __init__(self, recoltes=None):
        if recoltes is None:
            recoltes = {}
        self.recoltes = recoltes

    def ajouterRecolte(self, recolte):
        self.recoltes[(recolte.nom, recolte.sousClasse)] = recolte

    def recupererRecolte(self, nom, sousClasse):
        return self.recoltes[(nom, sousClasse)] if (nom, sousClasse) in self.recoltes else None

    def recupererRecoltes(self, noms=None, classes=None, sousClasses=None, niveaux=None,
                          categories=None, pointsRecolte=None):
        recoltes = []
        for _, recolte in sorted(self.recoltes.iteritems()):
            if noms and recolte.nom not in noms:
                continue
            if classes and recolte.classe not in classes:
                continue
            if sousClasses and recolte.sousClasse not in sousClasses:
                continue
            if niveaux and recolte.niveau not in niveaux:
                continue
            if categories and recolte.categorie not in categories:
                continue
            if pointsRecolte and recolte.materiaux not in pointsRecolte:
                continue
            # TODO Corriger les sélections par points de récolte
            recoltes.append(recolte)
        return recoltes


def construireListeRecoltes(nomFichier):
    listeRecoltes = ListeRecoltes()
    lignes = open(nomFichier, "r").readlines()
    for ligne in lignes:
        elements = ligne.strip("\n").split(";")
        nom = elements[0]
        classe = elements[1]
        sousClasse = elements[2]
        niveau = int(elements[3])
        categorie = elements[4]
        pointsRecolte = Recolte.texteVersPointsRecolte(elements[5])
        recolte = Recolte(nom, classe, sousClasse, niveau, categorie, pointsRecolte)
        listeRecoltes.ajouterRecolte(recolte)
    return listeRecoltes
