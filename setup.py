# coding: utf-8

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UtilitairesFinalFantasyXIV",
    version="3.0.0",
    author="Alexis Foerster",
    author_email="alexis.foerster@gmail.com",
    description="Application console permettant la gestion des membres d'une compagnie libre, des recettes et des récoltes du jeu Final Fantasy XIV.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lovehina13/UtilitairesFinalFantasyXIV",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["beautifulsoup4>=4.7.1"],
    python_requires=">=3.7.3",
)
