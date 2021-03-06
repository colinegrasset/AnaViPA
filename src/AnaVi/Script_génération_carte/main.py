#!/usr/bin/python

from optparse import OptionParser

from Crea_list_Pheno import csv_tablo_Pheno
from Link_svg import readmap
from dictionary_mutation import fillingDict
from Histogramme import barplot
from Histogramme import addBarplotSVG

def main(fileGeno,fileECnum,strainSearch,mapM,tableauDO):
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
    listPheno = csv_tablo_Pheno(tableauDO)
    # Range in the dictionnary of strain and modifications
    for i in listEcSouche:
        # Modification of the map according to the strain number
        if i.strain == strainSearch or i.strain == strainSearch + "(2)":
            readmap(mapM, i.mutation)

    print("the file outputMap.svg is updated for the strain", strainSearch)
    # Creation of a map with a DO barplot
    for i in listPheno:
        if i.strain == strainSearch :
             barplot(i.listdo,strainSearch)
             addBarplotSVG("outputMap.svg")
             print("the file outputMapBarplot.svg is updated for the strain", strainSearch)


tableGenotype = input("Genotype array pathway : ")
tableECnumber = input("EC number array pathway : ")
tableauDO = input("DO array pathway :")
nStrain = input("Strain number : ")
mapInput = input("Map pathway : ")

main(tableGenotype,tableECnumber,nStrain,mapInput,tableauDO)

