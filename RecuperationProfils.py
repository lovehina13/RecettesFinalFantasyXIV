# coding: utf-8

# ==============================================================================
# Name        : RecuperationProfils.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 2.1 (14/06/2020)
# Description : Récupération des profils des personnages
# ==============================================================================


def recupererProfils(nomFichierPersonnages, nomFichierProfils):

    # Fonction de récupération des données
    def donnees(personnage, classes, categories):
        texte = str()
        patron = "%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;"
        if personnage is None:
            texte += patron % ("Nom", "Titre", "Serveur", "Race", "Ethnie", "Sexe",
                               "Date de naissance", "Divinité", "Cité de départ",
                               "Grande compagnie", "Compagnie libre")
            for classe in classes:
                texte += "%s;" % (classe)
            for categorie in categories:
                texte += "%s;" % (categorie)
        else:
            texte += patron % (personnage.nom, personnage.titre, personnage.serveur,
                               personnage.race, personnage.ethnie, personnage.sexe,
                               personnage.dateNaissance, personnage.divinite, personnage.citeDepart,
                               personnage.grandeCompagnie, personnage.compagnieLibre)
            for classe in classes:
                texte += "%d;" % (personnage.getNiveauClasse(classe))
            for categorie in categories:
                texte += "%.3f;" % (personnage.getNiveauCategorie(categorie))
        texte = texte.rstrip(";")
        return texte

    from Personnages import Personnage, construireListePersonnages

    texte = str()

    # Construction de la liste des personnages
    listePersonnages = construireListePersonnages(nomFichierPersonnages)

    # Récupération de l'entête
    texte += donnees(None, Personnage.classes, Personnage.categories) + "\n"

    # Sélection des personnages
    noms = None
    personnages = listePersonnages.recupererPersonnages(noms=noms)

    # Récupération des données des personnages
    for personnage in sorted(personnages, key=lambda personnage: personnage.nom):
        texte += donnees(personnage, Personnage.classes, Personnage.categories) + "\n"

    # Écriture des données des personnages
    if nomFichierProfils is not None:
        fichierProfils = open(nomFichierProfils, "w")
        fichierProfils.write(texte)
        fichierProfils.close()

    # Affichage des données des personnages
    print texte


if __name__ == "__main__":

    import sys
    nomFichierPersonnages = sys.argv[1] if len(sys.argv) > 1 else None
    nomFichierProfils = sys.argv[2] if len(sys.argv) > 2 else None
    recupererProfils(nomFichierPersonnages, nomFichierProfils)
