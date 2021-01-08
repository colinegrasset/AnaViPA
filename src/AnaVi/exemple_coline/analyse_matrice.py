# vim: set fileencoding=utf-8 :
import os
import subprocess
import Pli_Struct
import crea_class
import ajout_val
import oddt
from oddt.fingerprints import (InteractionFingerprint,
                               SimpleInteractionFingerprint,
                               ECFP,
                               _ECFP_atom_repr,
                               SPLIF,
                               similarity_SPLIF,
                               PLEC,
                               fold,
                               MIN_HASH_VALUE,
                               MAX_HASH_VALUE,
                               sparse_to_dense,
                               sparse_to_csr_matrix,
                               csr_matrix_to_sparse,
                               dense_to_sparse,
                               dice,
                               tanimoto,
#                               hash32,
                               _ECFP_atom_hash)

from oddt.interactions import (pi_stacking,
                               hbond_acceptor_donor,
                               salt_bridge_plus_minus,
                               hydrophobic_contacts,
                               acceptor_metal,
                               close_contacts)
import pymol
import numpy as np
from numpy import (empty)
from pygments.lexers.csound import newline
import nt


#fichier .csv qui me sert d'exemple pour tester le script :  exportBindingEnol3HNT.csv
file1 = "exportBindingEnol3HNT.csv" # input("Saisissez le nom de votre fichier: ")
# Coline :  
root_data_dir = os.path.abspath('D:\PDB')
# Cyril :  
# root_data_dir = os.path.abspath('C:\BGene\PDB')

#seuil de distance max:
seuilrmsd = 3
seuilfingerprint = 0.6

# creation tableau de plistruct
pli_array = crea_class.csv_pli_struct(file1)  

# calcul des properties 
ajout_val.compute_properties(pli_array, root_data_dir)

# calcul des matrices .... sinon elles restent vides !
marixReceptorRMSPymol, marixLigandRMSOpenBabel, marixFingerprintSimilitude,  marixFingerprintSPLIFSimilitude = ajout_val.compute_matrices(pli_array, root_data_dir)
print()

print("   MATRICE DISTANCE RMSD: ")
print(marixLigandRMSOpenBabel)

clusterrmsd = []
coordonneeD = {}
allD = []
cmp = 0

for ligne in range(len(marixLigandRMSOpenBabel)):
    for colonne in range(len(marixLigandRMSOpenBabel)):
        if(marixLigandRMSOpenBabel[ligne][colonne] < seuilrmsd) and (marixLigandRMSOpenBabel[ligne][colonne] != 0):
            clusterrmsd.append(marixLigandRMSOpenBabel[ligne][colonne])
            c = colonne
            l = ligne
            cmp = cmp+1
            num = "n"+ str(cmp)
            coordonneeD = {num: { "ligne": l, "colonne": c}}
            allD.append(coordonneeD[num]) 

            
nbD = len(clusterrmsd)            
print("cluster rmsd: ", clusterrmsd)
print("les coordonnées des distances RMSD proches: ", allD)
print("nombre de distance < {} dans le cluster rmsd: ".format(seuilrmsd), len(clusterrmsd))

############################################

print("    MATRICE FINGERPRINT SIMILITUDE TANIMOTO: ")
print (marixFingerprintSimilitude)
            
clustertanimoto = []
coordonneeT = {}
allT = []
cmp = 0

for ligne in range (len(marixFingerprintSimilitude)):
    for colonne in range (len(marixFingerprintSimilitude)):
        if(marixFingerprintSimilitude[ligne][colonne] > seuilfingerprint):
            clustertanimoto.append(marixFingerprintSimilitude[ligne][colonne])
            c = colonne
            l = ligne
            cmp = cmp+1
            num = "n"+ str(cmp)
            coordonneeD = {num: { "ligne": l, "colonne": c}}
            allT.append(coordonneeD[num]) 

nbT =  len(clustertanimoto)    
if nbT == 0:
    for ligne in range (len(marixFingerprintSimilitude)):
        for colonne in range (len(marixFingerprintSimilitude)):
            if(marixFingerprintSimilitude[ligne][colonne] > 0.4):
                clustertanimoto.append(marixFingerprintSimilitude[ligne][colonne])
                c = colonne
                l = ligne
                cmp = cmp+1
                num = "n"+ str(cmp)
                coordonneeD = {num: { "ligne": l, "colonne": c}}
                allT.append(coordonneeD[num])
                   
print("cluster fingerprint tanimoto: ", clustertanimoto)
print("les coordonnées des fingerprints proche: ", allT)
print("nombre de distance < {} dans le cluster fingerprint similitude tanimoto: ".format(seuilfingerprint), len(clustertanimoto))

############################################

print("    MATRICE FINGERPRINT SIMILITUDE SPLIF: ")
print (marixFingerprintSPLIFSimilitude)
            
clustersplif = []
coordonneeS = {}
allS = []
cmp = 0

for ligne in range (len(marixFingerprintSPLIFSimilitude)):
    for colonne in range (len(marixFingerprintSPLIFSimilitude)):
        if(marixFingerprintSPLIFSimilitude[ligne][colonne] > seuilfingerprint):
            clustersplif.append(marixFingerprintSPLIFSimilitude[ligne][colonne])
            c = colonne
            l = ligne
            cmp = cmp+1
            num = "n"+ str(cmp)
            coordonneeS = {num: { "ligne": l , "colonne": c}}
            allS.append(coordonneeS[num])
            
nbS = len(clustersplif)

if nbS == 0:
    for ligne in range (len(marixFingerprintSPLIFSimilitude)):
        for colonne in range (len(marixFingerprintSPLIFSimilitude)):
            if(marixFingerprintSPLIFSimilitude[ligne][colonne] > seuilfingerprint):
                clustersplif.append(marixFingerprintSPLIFSimilitude[ligne][colonne])
                c = colonne
                l = ligne
                cmp = cmp+1
                num = "n"+ str(cmp)
                coordonneeS = {num: { "ligne": l, "colonne": c}}
                allS.append(coordonneeS[num])
                
print("cluster fingerprint splif: ", clustersplif)
print("les coordonnées des fingerprints proche: ", allS)
print("nombre de distance < {} dans le cluster fingerprint similitude SPLIF: ".format(seuilfingerprint), len(clustersplif))



            
        