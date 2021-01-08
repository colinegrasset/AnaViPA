import os
import csv 

#changez le nom du fichier dans file = ("namefile.csv", "r")
file = open("exportBindingEnol3HNT.csv", "r")
plistruct = {}

try:
    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(file, dialect='myDialect')
     
    for row in reader:
        for column, value in row.items():
            plistruct.setdefault(column, []).append(value)
    print (plistruct) 
      
finally:
    # Fermeture du fichier source
    file.close()
