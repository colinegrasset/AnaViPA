#!/usr/bin/python

from Crea_list_Geno import csv_tablo_Geno
from Crea_list_Num import csv_ECnum
import re

def fillingDict(fileGeno,fileECnum):
    """
    Function which associate modifications and ECnumber for each strain
    :param fileGeno: array with strains and modifications for each strain
    :param fileECnum: array with EC number and modifications for this gene
    :param nbStrain: the number of the strain
    :return: a dictionary list (each dictionary is composed of modifications and EC number for one strain)
    """

    ListGeno = csv_tablo_Geno(fileGeno)
    ListNum = csv_ECnum(fileECnum)

    for pli in ListGeno:
        # we create regex for pick the mutation of strain
         AllGeno = pli.genotype
         regle=re.compile(r"\S*")
         rep= list(regle.finditer(AllGeno))

         for i in rep: # for each mutations for each strains
            mut=i.group()

            for pli2 in ListNum: # we see each EC number with mutation in ListNum
                if mut == pli2.modif :  # we compare if the mutation of train correspond to Ec number
                    pli.mutation[mut]=pli2.ECnum  # we save the mutation and the Ec number in the dictionnary of the strain

    return ListGeno
#fillingDict("tablGeno.csv","tablECnum.csv")