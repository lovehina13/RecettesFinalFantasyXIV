# coding: utf-8

# ==============================================================================
# Name        : Traitements.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.7 (21/06/2019)
# Description : Traitements des récupérations
# ==============================================================================

if __name__ == "__main__":

    from RecuperationPersonnages import recupererPersonnages
    recupererPersonnages("9233364398528028107", "ListePersonnages.csv")

    from RecuperationProfils import recupererProfils
    recupererProfils("ListePersonnages.csv", "ListeProfils.csv")

    from RecuperationRecettes import recupererRecettes
    recupererRecettes("ListeRecettes.csv")

    from RecuperationMateriauxCristaux import recupererMateriauxCristaux
    recupererMateriauxCristaux("ListeRecettes.csv", "ListeMateriauxCristaux.csv")

    from Personnages import construireListePersonnages
    listePersonnages = construireListePersonnages("ListePersonnages.csv")
    for nom, personnage in sorted(listePersonnages.personnages.iteritems()):
        print "==================== %s ====================" % (nom)
        print "%s" % (personnage.getTexteRiche())

    from Recettes import construireListeRecettes
    listeRecettes = construireListeRecettes("ListeRecettes.csv")
    for nom, recette in sorted(listeRecettes.recettes.iteritems()):
        print "==================== %s ====================" % (nom)
        print "%s" % (recette.getTexteRiche())
