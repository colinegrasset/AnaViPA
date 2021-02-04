#!/usr/bin/python

from AnaVi.Script_génération_carte.Link_svg import readmap
from AnaVi.Script_génération_carte.dictionary_mutation import fillingDict


def main(fileGeno,fileECnum,strainSearch,mapM):
    """
    Main function which create a map with all modifications of a given strain
    :param fileGeno: array with strains and modifications for each strain
    :param fileECnum: array with EC number and modifications for this gene
    :param strainSearch: the number of the strain (the one that appear on the map)
    :param mapM: the basemap
    :return: svg file which is a map with modifications of the given strain
    """
    listEcSouche = fillingDict(fileGeno,fileECnum,strainSearch)
    for i in listEcSouche:
        if i.strain == strainSearch or i.strain == strainSearch + "(2)":
            print(i.mutation.keys())
            readmap(mapM, i.mutation)

main("tablGeno.csv","tablECnum.csv","5","carte_metabolique_pentose-arginine.svg")