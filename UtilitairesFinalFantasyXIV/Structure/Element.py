# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Structure/Element.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition d'un élément et d'un sous-élément
# ==================================================================================================


class Element:

    def __init__(self, nom=str()):
        self.nom = nom

    def identifiant(self):
        # Note: Réimplémenter l'identifiant pour chaque élément si nécessaire
        return self.nom

    def texte(self):
        # Note: Réimplémenter le format texte pour chaque élément si nécessaire
        return "|".join([item.texte() if hasattr(item, "texte") else str(item)
                         for _, item in self.__dict__.items()])

    def texteUtilisateur(self):
        # Note: Réimplémenter le format texte utilisateur pour chaque élément si nécessaire
        libelles = self.libelles if hasattr(self, "libelles") else [item for item, _ in self.__dict__.items()]
        return "\n".join([str("%s: %s" % (libelles[item1], item2[1].texteUtilisateur() if hasattr(item2[1], "texteUtilisateur") else item2[1])) for item1, item2 in enumerate(self.__dict__.items())])

    @staticmethod
    def creer(texte):
        return Element(texte)  # Note: Implémenter la création pour chaque élément

    # Libellés
    libelles = [str("Nom")]


class SousElement(Element):

    def texte(self):
        # Note: Réimplémenter le format texte pour chaque sous-élément si nécessaire
        return ":".join([item.texte() if hasattr(item, "texte") else str(item)
                         for _, item in self.__dict__.items()])

    def texteUtilisateur(self):
        # Note: Réimplémenter le format texte utilisateur pour chaque sous-élément si nécessaire
        return ", ".join([str("%s" % item.texteUtilisateur() if hasattr(item, "texteUtilisateur") else item) for _, item in self.__dict__.items()])

    @staticmethod
    def creer(texte):
        return SousElement(texte)  # Note: Implémenter la création pour chaque sous-élément
