# coding: utf-8

# ==============================================================================
# Name        : RecuperationMateriauxCristaux.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 2.0 (03/07/2019)
# Description : Récupération des matériaux et des cristaux des recettes
# ==============================================================================


def recupererMateriauxCristaux(nomFichierRecettes, nomFichierMateriauxCristaux):

    # Fonction de récupération des matériaux et des cristaux
    def recupererListeMateriauxCristaux(recettesSelectionnees, listeRecettes):
        from math import ceil
        # Initialisation des listes de matériaux et de cristaux
        listeMateriaux = {}
        listeCristaux = {}
        # Récupération du degré maximal des recettes sélectionnées
        degreRecetteMax = max(recette.degre for recette in recettesSelectionnees)
        # Constitution des recettes par degré
        recettesDegres = {degre: {} for degre in range(1, degreRecetteMax + 1)}
        # Ajout des recettes sélectionnées par degré
        for recette in recettesSelectionnees:
            degreRecette = recette.degre
            if recette not in recettesDegres[degreRecette]:
                recettesDegres[degreRecette][recette] = 0
            recettesDegres[degreRecette][recette] += 1.0 / recette.quantite
        # Traitement des recettes sélectionnées par degré
        for degre, recettes in sorted(recettesDegres.iteritems(), reverse=True):
            for recette, quantiteRecette in sorted(recettes.iteritems()):
                quantiteRecette = ceil(quantiteRecette)
                for materiau, quantite in sorted(recette.materiaux.iteritems()):
                    sousRecette = listeRecettes.recupererRecette(materiau)
                    if sousRecette and len(sousRecette.materiaux):
                        degreSousRecette = sousRecette.degre
                        if sousRecette not in recettesDegres[degreSousRecette]:
                            recettesDegres[degreSousRecette][sousRecette] = 0
                        recettesDegres[degreSousRecette][sousRecette] += quantite * quantiteRecette / sousRecette.quantite
                    else:
                        listeMateriaux[materiau] = quantite * quantiteRecette if materiau not in listeMateriaux else listeMateriaux[materiau] + quantite * quantiteRecette
                for cristal, quantite in sorted(recette.cristaux.iteritems()):
                    listeCristaux[cristal] = quantite * quantiteRecette if cristal not in listeCristaux else listeCristaux[cristal] + quantite * quantiteRecette
        # Transmission des listes de matériaux et de cristaux
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
