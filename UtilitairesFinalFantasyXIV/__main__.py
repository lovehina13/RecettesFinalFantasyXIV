# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/__main__.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (03/02/2021)
# Description : Définition du programme principal
# ==================================================================================================

import os
import sys
from UtilitairesFinalFantasyXIV.Donnees.Configuration import ConfigurationPrincipale, \
    ConfigurationPagePersonnages, ConfigurationPageRecettes, ConfigurationPageRecoltes, \
    ConfigurationGestionPersonnages, ConfigurationGestionRecettes, ConfigurationGestionRecoltes, \
    ConfigurationGestionInventaire
from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
from UtilitairesFinalFantasyXIV.Traitements.Inventaire import TraitementGestionInventaire
from UtilitairesFinalFantasyXIV.Traitements.Personnage import TraitementPagePersonnages, \
    TraitementGestionPersonnages
from UtilitairesFinalFantasyXIV.Traitements.Recette import TraitementPageRecettes, \
    TraitementGestionRecettes
from UtilitairesFinalFantasyXIV.Traitements.Recolte import TraitementPageRecoltes, \
    TraitementGestionRecoltes

if __name__ == "__main__":

    # Gestion de la configuration
    conf = ConfigurationPrincipale(None, sys.argv[1] if len(sys.argv) > 1
                                   else ConfigurationPrincipale.fichierEntree)
    if len(sys.argv) > 1 and os.path.exists(conf.fichier):
        conf.charger()
    else:
        conf.sauver()

    # Traitement des pages de personnages
    item = conf.elements[ConfigurationPrincipale.pagePersonnages]
    if item[ConfigurationPagePersonnages.activer]:
        TraitementPagePersonnages(item[ConfigurationPagePersonnages.compagnieLibre],
                                  item[ConfigurationPagePersonnages.nombrePages],
                                  item[ConfigurationPagePersonnages.fichierSortie]).executer()

    # Traitement des pages de recettes
    item = conf.elements[ConfigurationPrincipale.pageRecettes]
    if item[ConfigurationPageRecettes.activer]:
        TraitementPageRecettes(item[ConfigurationPageRecettes.nombrePages],
                               item[ConfigurationPageRecettes.fichierSortie]).executer()

    # Traitement des pages de récoltes
    item = conf.elements[ConfigurationPrincipale.pageRecoltes]
    if item[ConfigurationPageRecoltes.activer]:
        TraitementPageRecoltes(item[ConfigurationPageRecoltes.nombrePages],
                               item[ConfigurationPageRecoltes.fichierSortie]).executer()

    # Traitement de la gestion des personnages
    item = conf.elements[ConfigurationPrincipale.gestionPersonnages]
    if item[ConfigurationGestionPersonnages.activer]:
        TraitementGestionPersonnages(item[ConfigurationGestionPersonnages.fichierEntree],
                                     item[ConfigurationGestionPersonnages.fichierSortie],
                                     Filtres.filtres(item[ConfigurationGestionPersonnages.filtres]),
                                     item[ConfigurationGestionPersonnages.trier],
                                     item[ConfigurationGestionPersonnages.formatUtilisateur]).executer()

    # Traitement de la gestion des recettes
    item = conf.elements[ConfigurationPrincipale.gestionRecettes]
    if item[ConfigurationGestionRecettes.activer]:
        TraitementGestionRecettes(item[ConfigurationGestionRecettes.fichierEntree],
                                  item[ConfigurationGestionRecettes.fichierSortie],
                                  Filtres.filtres(item[ConfigurationGestionRecettes.filtres]),
                                  item[ConfigurationGestionPersonnages.trier],
                                  item[ConfigurationGestionRecettes.formatUtilisateur]).executer()

    # Traitement de la gestion des récoltes
    item = conf.elements[ConfigurationPrincipale.gestionRecoltes]
    if item[ConfigurationGestionRecoltes.activer]:
        TraitementGestionRecoltes(item[ConfigurationGestionRecoltes.fichierEntree],
                                  item[ConfigurationGestionRecoltes.fichierSortie],
                                  Filtres.filtres(item[ConfigurationGestionRecoltes.filtres]),
                                  item[ConfigurationGestionPersonnages.trier],
                                  item[ConfigurationGestionRecoltes.formatUtilisateur]).executer()

    # Traitement de la gestion de l'inventaire
    item = conf.elements[ConfigurationPrincipale.gestionInventaire]
    if item[ConfigurationGestionInventaire.activer]:
        TraitementGestionInventaire(item[ConfigurationGestionInventaire.fichierRecettesEntree],
                                    item[ConfigurationGestionInventaire.fichierRecoltesEntree],
                                    item[ConfigurationGestionInventaire.fichierSortie],
                                    Filtres.filtres(item[ConfigurationGestionInventaire.filtres])).executer()
