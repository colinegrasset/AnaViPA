#!/usr/bin/python

from AnaVi.Script_génération_carte.Crea_list_Geno import csv_tablo_Geno
from AnaVi.Script_génération_carte.Crea_list_Num import csv_ECnum
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
         AllGeno = pli.genotype
         regle=re.compile(r"\S*")
         rep= list(regle.finditer(AllGeno))

         for i in rep:
            mut=i.group()

            for pli2 in ListNum:
                if mut == pli2.modif :
                    pli.mutation[mut]=pli2.ECnum

    return ListGeno