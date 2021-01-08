#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import os
import csv 
import Pli_Struct  

def __repr__(pli):
    return(print("pliArray: ID({}), PDB({}), receptor({}), ligand({}), poseview({}))".format(
           pli.id, pli.pdb, pli.receptor, pli.ligand, pli.poseview)))     

def csv_pli_struct (file):
    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    pli_array = [] #creation d'une liste qui va contenir la class plistruct x nb de ligne du .csv
    for row in reader:
        pli = Pli_Struct.PliStruct()#liste pli prendre les valeurs de la class plistruct du package PLIStruct

        for column, value in row.items():#parcours le fichiers csv valeur par valeur en aller de gauche a droite puis passe a la ligne suivante
            if(column == "ID") : 
                pli.id = value
            if(column == "PDB") : 
                pli.pdb = value
            if(column == "receptor") : 
                pli.receptor = value
            if(column == "ligand") : 
                pli.ligand = value 
            if (column == "poseview") :
                pli.poseview = value
            if (column == "fingerprint") :
                pli.fingerprint = value
            if (column =="fingerprintSPLIF") :
                pli.fingerprintSPLIF = value
            if (column == "hbond") :
                pli.hbond = value
        pli_array.append(pli)  # commande qui ajoute un pli a la liste pliArray
        
#     file.close()
    
    for pli in pli_array:
        __repr__(pli) 
   
    return pli_array
        

