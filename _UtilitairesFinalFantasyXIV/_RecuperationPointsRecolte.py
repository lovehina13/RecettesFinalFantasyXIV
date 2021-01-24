# coding: utf-8

# ==============================================================================
# Name        : RecuperationPointsRecolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 2.2 (14/01/2021)
# Description : Récupération des points de récolte des récoltes
# ==============================================================================


def recupererPointsRecolte(nomFichierRecoltes, nomFichierPointsRecolte):

    # Fonction de récupération des données
    def donnees(recolte):
        from Recoltes import Recolte
        texte = str()
        patron = "%s;%s;%s;%s"
        if recolte is None:
            texte += patron % ("Récolte", "Classe", "Sous-classe", "Points de récolte")
        else:
            texte += patron % (recolte.nom, recolte.classe, recolte.sousClasse,
                               Recolte.pointsRecolteVersTexte(recolte.pointsRecolte).strip())
        return texte

    from Recoltes import construireListeRecoltes

    texte = str()

    # Construction de la liste des récoltes
    listeRecoltes = construireListeRecoltes(nomFichierRecoltes)

    # Récupération de l'entête
    texte += donnees(None) + "\n"

    # Sélection des récoltes
    noms = None
    recoltes = listeRecoltes.recupererRecoltes(noms=noms)

    # Récupération des points de récolte des récoltes
    for recolte in sorted(recoltes, key=lambda recolte: recolte.nom):
        texte += donnees(recolte) + "\n"

    # Écriture des données des points de récolte des récoltes
    if nomFichierPointsRecolte is not None:
        fichierPointsRecolte = open(nomFichierPointsRecolte, "w")
        fichierPointsRecolte.write(texte)
        fichierPointsRecolte.close()

    # Affichage des données des points de récolte des récoltes
    print texte


if __name__ == "__main__":

    import sys
    nomFichierRecoltes = sys.argv[1] if len(sys.argv) > 1 else None
    nomFichierPointsRecolte = sys.argv[2] if len(sys.argv) > 2 else None
    recupererPointsRecolte(nomFichierRecoltes, nomFichierPointsRecolte)
