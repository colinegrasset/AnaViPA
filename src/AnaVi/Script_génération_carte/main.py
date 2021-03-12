#!/usr/bin/python

from optparse import OptionParser


from Link_html import readmap
from dictionary_mutation import fillingDict


def main(fileGeno,fileECnum,strainSearch,mapM):
    """
    Main function which create a map with all modifications of a given strain
    :param fileGeno: array with strains and modifications for each strain
    :param fileECnum: array with EC number and modifications for this gene
    :param strainSearch: the number of the strain (the one that appear on the map)
    :param mapM: the basemap
    :return: svg file which is a map with modifications of the given strain
    """

    # Create a dictionnary with ECnumber and modifications for each ECnumber
    listEcSouche = fillingDict(fileGeno,fileECnum)
    # Range in the dictionnary of strain and modifications
    for i in listEcSouche:
        # Modification of the map according to the strain number
        if i.strain == strainSearch or i.strain == strainSearch + "(2)":

            readmap(mapM, i.mutation)
    print("the file outputMap.svg is updated for the strain", '3.1.3.11')

##tableGenotype = input("Genotype array pathway : ")
# tableECnumber = input("EC number array pathway : ")
# nStrain = input("Strain number : ")
# mapInput = input("Map pathway : ")
main('tablGeno.csv','tablECnum.csv','42','carte_metabolique_pentose-arginine.html')
