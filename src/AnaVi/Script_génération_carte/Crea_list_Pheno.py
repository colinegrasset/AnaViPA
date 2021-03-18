#!/usr/bin/python
# vim: set encoding=utf-8 :

import csv

from AnaVi.Script_génération_carte.classPheno import Pheno


def __repr__(pli):
    print("pliArray: Strain({}), do1({}), do2({}), do3({})".format(
        pli.strain, pli.do1, pli.do2, pli.do3))

def csv_tablo_Pheno(file):

    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    pheno_array = []  # create a list which contains the classGeno class X the number of line in csv file

    for row in reader:
        pli = Pheno()  # pli list take the values of the Pheno class in classPheno package

        # range the csv file value by value n moving from left to right and go to the next line
        for column, value in row.items():

            if column == "ï»¿souche":
                pli.strain = value


            if column == "DO6":
                pli.do1 = value

            if column == "DO24":
                pli.do2 = value

            if column == "Production":
                pli.do3 = value

        pli.listdo.append(pli.do1)
        pli.listdo.append(pli.do2)
        pli.listdo.append(pli.do3)
        pheno_array.append(pli)  # command which add a pli to the geno_array list


    return pheno_array