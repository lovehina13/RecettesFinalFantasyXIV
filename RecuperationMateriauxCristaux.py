# coding: utf-8

# ==============================================================================
# Name        : RecuperationMateriauxCristaux.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.6 (15/01/2019)
# Description : Récupération des matériaux et des cristaux des recettes
# ==============================================================================


def recupererMateriauxCristaux(nomFichierRecettes, nomFichierMateriauxCristaux):

    # Fonction de récupération des matériaux et des cristaux
    def recupererListeMateriauxCristaux(recettesSelectionnees, listeRecettes):
        listeMateriaux = {}
        listeCristaux = {}
        for recette in recettesSelectionnees:
            materiaux = recette.materiaux
            for materiau, quantite in sorted(materiaux.iteritems()):
                sousRecette = listeRecettes.recupererRecette(materiau)
                if sousRecette and len(sousRecette.materiaux):
                    sousListeMateriaux, sousListeCristaux = recupererListeMateriauxCristaux([sousRecette], listeRecettes)
                    for sousMateriau, sousQuantite in sorted(sousListeMateriaux.iteritems()):
                        listeMateriaux[sousMateriau] = (sousQuantite * quantite) if sousMateriau not in listeMateriaux else listeMateriaux[sousMateriau] + (sousQuantite * quantite)
                    for sousCristal, sousQuantite in sorted(sousListeCristaux.iteritems()):
                        listeCristaux[sousCristal] = (sousQuantite * quantite) if sousCristal not in listeCristaux else listeCristaux[sousCristal] + (sousQuantite * quantite)
                else:
                    listeMateriaux[materiau] = quantite if materiau not in listeMateriaux else listeMateriaux[materiau] + quantite
            cristaux = recette.cristaux
            for cristal, quantite in sorted(cristaux.iteritems()):
                listeCristaux[cristal] = quantite if cristal not in listeCristaux else listeCristaux[cristal] + quantite
        return listeMateriaux, listeCristaux

    # Fonction de récupération des données des matériaux et des cristaux
    def donnees(objet, quantite):
        texte = str()
        if objet is None and quantite is None:
            patron = "%s;%s"
            texte += patron % ("Objet", "Quantité")
        else:
            patron = "%s;%d"
            texte += patron % (objet, quantite)
        return texte

    from Recettes import construireListeRecettes

    texte = str()

    # Construction de la liste des recettes
    listeRecettes = construireListeRecettes(nomFichierRecettes)

    # Récupération de l'entête
    texte += donnees(None, None) + "\n"

    # Sélection des recettes
    noms = None
    recettes = listeRecettes.recupererRecettes(noms=noms)

    # Récupération des matériaux et des cristaux des recettes
    listeMateriaux, listeCristaux = recupererListeMateriauxCristaux(recettes, listeRecettes)

    # Récupération des données des matériaux et des cristaux des recettes
    for objet, quantite in sorted(listeMateriaux.iteritems()):
        texte += donnees(objet, quantite) + "\n"
    for objet, quantite in sorted(listeCristaux.iteritems()):
        texte += donnees(objet, quantite) + "\n"

    # Écriture des données des matériaux et des cristaux des recettes
    if nomFichierMateriauxCristaux is not None:
        fichierMateriauxCristaux = open(nomFichierMateriauxCristaux, "w")
        fichierMateriauxCristaux.write(texte)
        fichierMateriauxCristaux.close()

    # Affichage des données des matériaux et des cristaux des recettes
    print texte


if __name__ == "__main__":

    import sys
    nomFichierRecettes = sys.argv[1] if len(sys.argv) > 1 else None
    nomFichierMateriauxCristaux = sys.argv[2] if len(sys.argv) > 2 else None
    recupererMateriauxCristaux(nomFichierRecettes, nomFichierMateriauxCristaux)
