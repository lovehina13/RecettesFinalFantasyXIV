# coding: utf-8

# ==============================================================================
# Name        : Recettes.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.8 (25/06/2019)
# Description : Définition d'une recette et d'une liste de recettes
# ==============================================================================


class Recette(object):

    def __init__(self, nom=str(), classe=str(), niveau=int(), categorie=str(), materiaux=None,
                 cristaux=None, quantite=int(), difficulte=int(), solidite=int(), qualite=int(),
                 degre=int()):
        if materiaux is None:
            materiaux = {}
        if cristaux is None:
            cristaux = {}
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.categorie = categorie
        self.materiaux = materiaux
        self.cristaux = cristaux
        self.quantite = quantite
        self.difficulte = difficulte
        self.solidite = solidite
        self.qualite = qualite
        self.degre = degre

    def calculerDegre(self, listeRecettes):
        degreRecette = 1
        for materiau, _ in sorted(self.materiaux.iteritems()):
            sousRecette = listeRecettes.recupererRecette(materiau)
            if sousRecette and len(sousRecette.materiaux):
                degreSousRecette = sousRecette.calculerDegre(listeRecettes)
                if degreSousRecette >= degreRecette:
                    degreRecette = degreSousRecette + 1
        return degreRecette

    def getTexteBrut(self):
        patron = "%s;%s;%d;%s;%s;%s;%d;%d;%d;%d;%d"
        texte = patron % (self.nom, self.classe, self.niveau, self.categorie,
                          Recette.objetsVersTexte(self.materiaux),
                          Recette.objetsVersTexte(self.cristaux), self.quantite, self.difficulte,
                          self.solidite, self.qualite, self.degre)
        return texte

    def getTexteRiche(self):
        patron = str()
        patron += "Nom: %s\n"
        patron += "Classe: %s\n"
        patron += "Niveau: %d\n"
        patron += "Catégorie: %s\n"
        patron += "Matériaux: %s\n"
        patron += "Cristaux: %s\n"
        patron += "Total fabriqué: %d\n"
        patron += "Difficulté: %d\n"
        patron += "Solidité: %d\n"
        patron += "Qualité maximum: %d\n"
        patron += "Degré: %d\n"
        texte = patron % (self.nom, self.classe, self.niveau, self.categorie,
                          Recette.objetsVersTexte(self.materiaux),
                          Recette.objetsVersTexte(self.cristaux), self.quantite, self.difficulte,
                          self.solidite, self.qualite, self.degre)
        return texte

    @staticmethod
    def objetsVersTexte(objets):
        texte = str()
        for objet, quantite in sorted(objets.iteritems()):
            texte += "%d %s, " % (quantite, objet)
        texte = texte.rstrip(", ")
        return texte

    @staticmethod
    def texteVersObjets(texte):
        objets = {}
        for element in texte.split(", "):
            objet = " ".join(element.split()[1:])
            quantite = int(element.split()[0])
            objets[objet] = quantite
        return objets


class ListeRecettes(object):

    def __init__(self, recettes=None):
        if recettes is None:
            recettes = {}
        self.recettes = recettes

    def ajouterRecette(self, recette):
        self.recettes[recette.nom] = recette

    def recupererRecette(self, nom):
        return self.recettes[nom] if nom in self.recettes else None

    def recupererRecettes(self, noms=None, classes=None, niveaux=None, categories=None,
                          materiaux=None, cristaux=None, quantites=None, difficultes=None,
                          solidites=None, qualites=None):
        recettes = []
        for _, recette in sorted(self.recettes.iteritems()):
            if noms and recette.nom not in noms:
                continue
            if classes and recette.classe not in classes:
                continue
            if niveaux and recette.niveau not in niveaux:
                continue
            if categories and recette.categorie not in categories:
                continue
            if materiaux and recette.materiaux not in materiaux:
                continue
            if cristaux and recette.cristaux not in cristaux:
                continue
            if quantites and recette.quantite not in quantites:
                continue
            if difficultes and recette.difficulte not in difficultes:
                continue
            if solidites and recette.solidite not in solidites:
                continue
            if qualites and recette.qualite not in qualites:
                continue
            # TODO Corriger les sélections par matériaux et cristaux
            if noms and recette.nom in noms:
                for _ in range(noms.count(recette.nom)):
                    recettes.append(recette)
            else:
                recettes.append(recette)
        return recettes


def construireListeRecettes(nomFichier):
    listeRecettes = ListeRecettes()
    lignes = open(nomFichier, "r").readlines()
    for ligne in lignes:
        elements = ligne.split(";")
        nom = elements[0]
        classe = elements[1]
        niveau = int(elements[2])
        categorie = elements[3]
        materiaux = Recette.texteVersObjets(elements[4])
        cristaux = Recette.texteVersObjets(elements[5])
        quantite = int(elements[6])
        difficulte = int(elements[7])
        solidite = int(elements[8])
        qualite = int(elements[9])
        recette = Recette(nom, classe, niveau, categorie, materiaux, cristaux, quantite, difficulte,
                          solidite, qualite)
        listeRecettes.ajouterRecette(recette)
    for recette in listeRecettes.recupererRecettes():
        recette.degre = recette.calculerDegre(listeRecettes)
    return listeRecettes
