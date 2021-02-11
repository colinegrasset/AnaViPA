#!/usr/bin/python
# vim: set encoding=utf-8 :

import csv
from classGeno import Geno



def __repr__(pli):
    print("pliArray: Strain({}), daughter({}), genotype({}))".format(
        pli.strain, pli.daughter, pli.genotype))

def csv_tablo_Geno(file):

    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    geno_array = []  # create a list which contains the classGeno class X the number of line in csv file

    for row in reader:
        pli = Geno()  # pli list take the values of the Geno class in classGeno package

        # range the csv file value by value n moving from left to right and go to the next line
        for column, value in row.items():
            if column == "Souche":
                pli.strain = value
            if column == "Fille de...":
                pli.daughter = value
            if column == "Genotype":
                pli.genotype = value
            geno_array.append(pli)  # command which add a pli to the geno_array list

    return geno_array