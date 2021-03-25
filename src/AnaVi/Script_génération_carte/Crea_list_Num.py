#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import csv
from classNum import Num



def __repr__(line):
    return (print("listNumArray: ECnum({}), modif({})".format(line.ECnum, line.modif)))


def csv_ECnum(file):
    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    listNum_array = []
    for row in reader:
        line = Num()  # create a list which contains the classNum class X the number of line in csv file
        # range the csv file value by value n moving from left to right and go to the next line
        for column, value in row.items():
            if (column == "EC number"):
                line.ECnum = value
            if (column == "Modification"):
                line.modif = value

        listNum_array.append(line)  # command which add a line to the listNum_array list

    return listNum_array

