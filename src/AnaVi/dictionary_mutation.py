from AnaVi.Script_génération_carte import Crea_list_Geno,Crea_list_Num
from AnaVi.Script_génération_carte.classGeno import Geno
from AnaVi.Script_génération_carte.classNum import Num
import regex


def fillingDict():
    regle = regex.compile(r"(.*)\ (.*)\ (.*)")
    ListGeno = Crea_list_Geno.csv_tablo_Geno("tablGeno.csv")
    ListECnum = Crea_list_Num.csv_ECnum("tablECnum.csv")
    for pli in ListGeno:
        AllGeno = ListGeno.genotype
        rep = regle.search(AllGeno)
        print(rep.groups())
