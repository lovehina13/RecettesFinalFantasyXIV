# coding: utf-8

# ==============================================================================
# Name        : Personnages.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.7 (21/06/2019)
# Description : Définition d'un personnage et d'une liste de personnages
# ==============================================================================


class Personnage(object):

    def __init__(self, nom=str(), titre=str(), serveur=str(), race=str(), ethnie=str(), sexe=str(),
                 dateNaissance=str(), divinite=str(), citeDepart=str(), grandeCompagnie=str(),
                 compagnieLibre=str(), classes=None):
        if classes is None:
            classes = {}
        self.nom = nom
        self.titre = titre
        self.serveur = serveur
        self.race = race
        self.ethnie = ethnie
        self.sexe = sexe
        self.dateNaissance = dateNaissance
        self.divinite = divinite
        self.citeDepart = citeDepart
        self.grandeCompagnie = grandeCompagnie
        self.compagnieLibre = compagnieLibre
        self.classes = classes

    def getTexteBrut(self):
        patron = "%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s"
        texte = patron % (self.nom, self.titre, self.serveur, self.race, self.ethnie, self.sexe,
                          self.dateNaissance, self.divinite, self.citeDepart, self.grandeCompagnie,
                          self.compagnieLibre, Personnage.classesVersTexte(self.classes))
        return texte

    def getTexteRiche(self):
        patron = str()
        patron += "Nom: %s\n"
        patron += "Titre: %s\n"
        patron += "Serveur: %s\n"
        patron += "Race: %s\n"
        patron += "Ethnie: %s\n"
        patron += "Sexe: %s\n"
        patron += "Date de naissance: %s\n"
        patron += "Divinité: %s\n"
        patron += "Cité de départ: %s\n"
        patron += "Grande compagnie: %s\n"
        patron += "Compagnie libre: %s\n"
        patron += "Classes: %s\n"
        texte = patron % (self.nom, self.titre, self.serveur, self.race, self.ethnie, self.sexe,
                          self.dateNaissance, self.divinite, self.citeDepart, self.grandeCompagnie,
                          self.compagnieLibre, Personnage.classesVersTexte(self.classes))
        return texte

    def getNiveauClasse(self, classe):
        return self.classes[classe] if classe in self.classes else None

    def getNiveauCategorie(self, categorie):
        classes = Personnage.classesCategories[categorie]
        niveauClasses = 0
        for classe in classes:
            niveauClasses += self.getNiveauClasse(classe)
        niveauCategorie = float(niveauClasses) / float(len(classes))
        return niveauCategorie

    @staticmethod
    def classesVersTexte(classes):
        texte = str()
        for classe, niveau in sorted(classes.iteritems()):
            texte += "%s %d, " % (classe, niveau)
        texte = texte.rstrip(", ")
        return texte

    @staticmethod
    def texteVersClasses(texte):
        classes = {}
        for element in texte.split(", "):
            classe = " ".join(element.split()[:-1])
            niveau = int(element.split()[-1])
            classes[classe] = niveau
        return classes

    classes = ["Paladin", "Guerrier", "Chevalier noir", "Mage blanc", "Érudit", "Astromancien",
               "Moine", "Chevalier dragon", "Ninja", "Samouraï", "Barde", "Machiniste", "Mage noir",
               "Invocateur", "Mage rouge", "Mage bleu", "Menuisier", "Forgeron", "Armurier",
               "Orfèvre", "Tanneur", "Couturier", "Alchimiste", "Cuisinier", "Mineur", "Botaniste",
               "Pêcheur"]

    categories = ["Tank", "Soigneur", "DPS de mêlée", "DPS physique à distance",
                  "DPS magique à distance", "Combattants / Mages", "Artisans", "Récolteurs",
                  "Général"]

    classesCategories = {"Tank": ["Paladin", "Guerrier", "Chevalier noir"],
                         "Soigneur": ["Mage blanc", "Érudit", "Astromancien"],
                         "DPS de mêlée": ["Moine", "Chevalier dragon", "Ninja", "Samouraï"],
                         "DPS physique à distance": ["Barde", "Machiniste"],
                         "DPS magique à distance": ["Mage noir", "Invocateur", "Mage rouge",
                                                    "Mage bleu"],
                         "Combattants / Mages": ["Paladin", "Guerrier", "Chevalier noir",
                                                 "Mage blanc", "Érudit", "Astromancien", "Moine",
                                                 "Chevalier dragon", "Ninja", "Samouraï", "Barde",
                                                 "Machiniste", "Mage noir", "Invocateur",
                                                 "Mage rouge", "Mage bleu"],
                         "Artisans": ["Menuisier", "Forgeron", "Armurier", "Orfèvre", "Tanneur",
                                      "Couturier", "Alchimiste", "Cuisinier"],
                         "Récolteurs": ["Mineur", "Botaniste", "Pêcheur"],
                         "Général": ["Paladin", "Guerrier", "Chevalier noir", "Mage blanc",
                                     "Érudit", "Astromancien", "Moine", "Chevalier dragon", "Ninja",
                                     "Samouraï", "Barde", "Machiniste", "Mage noir", "Invocateur",
                                     "Mage rouge", "Mage bleu", "Menuisier", "Forgeron", "Armurier",
                                     "Orfèvre", "Tanneur", "Couturier", "Alchimiste", "Cuisinier",
                                     "Mineur", "Botaniste", "Pêcheur"]}


class ListePersonnages(object):

    def __init__(self, personnages=None):
        if personnages is None:
            personnages = {}
        self.personnages = personnages

    def ajouterPersonnage(self, personnage):
        self.personnages[personnage.nom] = personnage

    def recupererPersonnage(self, nom):
        return self.personnages[nom] if nom in self.personnages else None

    def recupererPersonnages(self, noms=None, titres=None, serveurs=None, races=None, ethnies=None,
                             sexes=None, datesNaissance=None, divinites=None, citesDepart=None,
                             grandesCompagnies=None, compagniesLibres=None, classes=None):
        personnages = []
        for _, personnage in sorted(self.personnages.iteritems()):
            if noms and personnage.nom not in noms:
                continue
            if titres and personnage.titre not in titres:
                continue
            if serveurs and personnage.serveur not in serveurs:
                continue
            if races and personnage.race not in races:
                continue
            if ethnies and personnage.ethnie not in ethnies:
                continue
            if sexes and personnage.sexe not in sexes:
                continue
            if datesNaissance and personnage.dateNaissance not in datesNaissance:
                continue
            if divinites and personnage.divinite not in divinites:
                continue
            if citesDepart and personnage.citeDepart not in citesDepart:
                continue
            if grandesCompagnies and personnage.grandeCompagnie not in grandesCompagnies:
                continue
            if compagniesLibres and personnage.compagnieLibre not in compagniesLibres:
                continue
            if classes and personnage.classes not in classes:
                continue
            # TODO Corriger les sélections par classes
            personnages.append(personnage)
        return personnages


def construireListePersonnages(nomFichier):
    listePersonnages = ListePersonnages()
    lignes = open(nomFichier, "r").readlines()
    for ligne in lignes:
        elements = ligne.split(";")
        nom = elements[0]
        titre = elements[1]
        serveur = elements[2]
        race = elements[3]
        ethnie = elements[4]
        sexe = elements[5]
        dateNaissance = elements[6]
        divinite = elements[7]
        citeDepart = elements[8]
        grandeCompagnie = elements[9]
        compagnieLibre = elements[10]
        classes = Personnage.texteVersClasses(elements[11])
        personnage = Personnage(nom, titre, serveur, race, ethnie, sexe, dateNaissance, divinite,
                                citeDepart, grandeCompagnie, compagnieLibre, classes)
        listePersonnages.ajouterPersonnage(personnage)
    return listePersonnages
