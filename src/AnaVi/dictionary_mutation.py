#!/usr/bin/python
from AnaVi.Script_génération_carte import Crea_list_Geno,Crea_list_Num
import regex

def fillingDict(fileGeno,fileECnum):
    #regle = regex.compile(r"(.)\ (.)\ (.*)")

    ListGeno = Crea_list_Geno.csv_tablo_Geno(fileGeno)
    ListECnum = Crea_list_Num.csv_ECnum(fileECnum)
# for pli in ListGeno:
#     AllGeno = ListGeno.genotype
#    rep = regle.search(AllGeno)
#print(rep.groups())

#path de coline
fillingDict("C://Users//Utiisateur//IdeaProjects//AnaVi//src//AnaVi//Script_génération_carte//tablGeno.csv",
            "C://Users//Utilisateur//IdeaProjects//AnaVi//src//AnaVi//Script_génération_carte//tablECnum.csv")


