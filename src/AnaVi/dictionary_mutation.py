from AnaVi.Script_génération_carte import Crea_list_Num, Crea_list_Geno
from AnaVi.Script_génération_carte.classGeno import Geno
from AnaVi.Script_génération_carte.classNum import Num



def fillingDict():

    ListGeno = Crea_list_Geno.csv_tablo_Geno("tablGeno.csv")
    ListECnum = Crea_list_Num.csv_ECnum("tablECnum.csv")
    for pli in ListGeno:
        AllGeno = ListGeno.genotype
