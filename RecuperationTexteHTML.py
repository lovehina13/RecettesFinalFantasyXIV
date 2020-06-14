# coding: utf-8

# ==============================================================================
# Name        : RecuperationTexteHTML.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 2.1 (14/06/2020)
# Description : Récupération d'un texte HTML
# ==============================================================================


def recupererTexteHTML(adressePage):

    from urllib2 import urlopen

    texteHTML = None
    while not texteHTML:
        try:
            texteHTML = "".join(urlopen(adressePage).readlines())
        except:
            pass
    return texteHTML
