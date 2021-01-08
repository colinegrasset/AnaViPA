# vim: set fileencoding=utf-8 :

import os
import subprocess
import Pli_Struct
import crea_class
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

'''
 Function that calls the obrms native executable provided by OpenBabel 
 
 return RMS value as a float
 
'''
def call_obrms(molecule1, molecule2) :
    myPopen  = subprocess.Popen(["obrms", molecule1, molecule2],
                                stdout=subprocess.PIPE, encoding = 'ascii', shell = True)
    # retourne une ligne genre (la valeure cherchée est à la fin) :
    # RMSD C:\BGene\PDB/Q12634/1YBV\docking\enol3HTNfl_out_ligand_01.pdb:C:\BGene\PDB/Q12634/1YBV\docking\enol3HTNfl_out_ligand_02.pdb 3.73202
    line = myPopen.stdout.readline()
    myPopen.poll() 
    words = line.split()
    return float(words[len(words) - 1])


    
'''
 Function that computes many properties for  PliStruct : fingerproitns, protein-ligand interactions ...
 
    -  pli_array  :  array of PliStruct
 
'''
def compute_properties(pli_array, root_data_dir) :
    
    #boucle calculant les nouveaux parametres pour chaque complexe
    for pli in pli_array : 
        # read the protein file
        protein = next(oddt.toolkit.readfile('pdb', os.path.join(root_data_dir,pli.receptor)))
        protein.protein = True
        protein.addh(only_polar=True)
        
        # read the ligand file
        ligand = next(oddt.toolkit.readfile('pdb',  os.path.join(root_data_dir,pli.ligand) ))
        ligand.addh(only_polar=True)
        
    
        # calcul du fingerprint Simple de chaque complexe 
        pli.fingerprint = oddt.fingerprints.SimpleInteractionFingerprint(ligand ,  protein , strict = True )
        # calcul du fingerprint SPLIF de chaque complexe
        pli.fingerprintSPLIF = oddt.fingerprints.SPLIF(ligand ,  protein, distance_cutoff=4.5  )
        print("id du complexe: " , pli.id) 
        print ("fingerprints du complexe")
        print (pli.fingerprint)
        print (pli.fingerprintSPLIF)
        
        #calcul des hbonds
        pli.hbond = oddt.interactions.hbond_acceptor_donor(ligand, protein, cutoff=3.5, base_angle=120, tolerance=30)
        print("hbond du complexe:")
        print(pli.hbond)
        
        
        #calcul des halogen
        pli.halogen = oddt.interactions.halogenbond_acceptor_halogen(ligand, protein, base_angle_acceptor=120, base_angle_halogen=180, tolerance=30, cutoff=4)
        print("halogen bond du complexe: ")
        print(pli.halogen)
        
        #calcul des ponts salins
        pli.salt = oddt.interactions.salt_bridge_plus_minus(ligand, protein, cutoff=4)
        print("salt bridge du complexe: ")
        print(pli.salt)
        
        #calcul des interactions hydrophobes
        pli.hydrophobic = oddt.interactions.hydrophobic_contacts(ligand, protein, cutoff=4)
        print("hydrophobic interaction: ")
        print(pli.hydrophobic)
        
        #pi stacking
        pli.stacking = oddt.interactions.pi_stacking(ligand, protein , cutoff=5, tolerance=30)
        print("stacking: ")
        print(pli.stacking)
    
        print("\n", "\n")
# end compute_properties
        
    
'''
 Function that computes distances and similitudes between each pair of PliStruct
 
    -  pli_array  :  array of PliStruct
 
'''
def compute_matrices(pli_array, root_data_dir ) :
    ############################################################################ 
    #
    #    Calcul des distances RMS des receptors et des ligands , et Tanimoto sur les fingerprint
    # 
    
    # I - MAtrices contenant les distances RMS
    # Ce sont des matrices contenant N lignes et M colonnes, 
    #      N = longueur de  pli_array 
    #      M = longueur de  pli_array 
    # Deux façons de calculer les distances RMS : 
    #     -  avec pymol pour les distances entre Receptor 
    #     -  avec openbabel pour les distances entre ligand 
    #dans les deux cas, les valeurs calculées sont des float, les valeurs sont initialisés à 0.
    #
    marixReceptorRMSPymol = np.full(shape=(len(pli_array),len(pli_array)),fill_value=0.0, dtype=float)
    marixLigandRMSOpenBabel = np.full(shape=(len(pli_array),len(pli_array)),fill_value=0.0, dtype=float)
    
   
    
    # II - Matrices contenant les similarité entre fingerprint 
    #
    # Les Fingerprint de chaque Pose sont calculées 
    #     - avec oddt.fingerprints.SimpleInteractionFingerprint (   Based on http://dx.doi.org/10.1016/j.csbj.2014.05.004. )
    #     - avec oddt.fingerprints.SPLIF (   based on http://pubs.acs.org/doi/abs/10.1021/ci500319f.)
    # 
    # 
    # La similitude entre deux fingerprints doit être calculée , respectivement grâce à
    #      -  oddt.fingerprints.tanimoto
    #      -  oddt.fingerprints.similarity_SPLIF
    #
    marixFingerprintSimilitude = np.full(shape=(len(pli_array),len(pli_array)),fill_value=0.0, dtype=float)
    marixFingerprintSPLIFSimilitude = np.full(shape=(len(pli_array),len(pli_array)),fill_value=0.0, dtype=float)
    
   
    # requis pour initialiser pymol 
    pymol.finish_launching() 
    
    for i in range(len(pli_array)):
        for j in range(len(pli_array)):
            if(i>j) : 
                # aucun sens de calculer une distance si i = j , et pas utile de calculer deux fois la même distance i%j et j%i 
                continue
            pliRow = pli_array[i]
            pliColumn = pli_array[j]
            print(pliRow.receptor)
            print(pliColumn.receptor)
            # on charge les fichiers PDB des protéines (receptor) dans pymol 
            pymol.cmd.load(os.path.join(root_data_dir,pliRow.receptor), 'row')
            pymol.cmd.load(os.path.join(root_data_dir,pliColumn.receptor), 'column') 
            
        
            # puis alignement sur les chjaines A 
            res_alignement =pymol.cmd.align( 'row & chain A', 'column & chain A' ) 
            
            '''
            This returns a list with 7 items:
                
                RMSD after refinement
                Number of aligned atoms after refinement
                Number of refinement cycles
                RMSD before refinement
                Number of aligned atoms before refinement
                Raw alignment score
                Number of residues aligned
             '''
            
            print(res_alignement)
            print(" receptor distance  " + str(res_alignement[0]))
            marixReceptorRMSPymol[i][j] = res_alignement[0]
            
            # on nettoie un peu le context pymol
            pymol.cmd.remove('row')
            pymol.cmd.remove('column') 
            
            # Utilisation de obrms.exe de OpenBabel 
            #
            dist = call_obrms(os.path.join(root_data_dir,pliRow.ligand), os.path.join(root_data_dir,pliColumn.ligand))
            print(" ligand distance  " +  str(dist) )
            marixLigandRMSOpenBabel[i][j] = dist
       
            
            # TODO : calcul des similartités entre fingerpriont (appeler les bonnes fonctions)
            #  les fingerprint et fingerprintSPLIF sont déja calcules au début du script
    #     print("id du complexe: " , pli.id) 
    #     print ("fingerprint du complexe: ")
    #     print (pli.fingerprint)
    #     print("fingersprint SPLIF: ")
    #     print(pli.fingerprintSPLIF)
    print("***************************************** Calcul de la matrice de fingerprint et de fingerprit_SPLIF ********************************************")
    for i in range(len(pli_array)):
        for j in range(len(pli_array)):
            if(i>j) :
              
                fingerp1 = pli_array[i].fingerprint
                fingerp2 = pli_array[j].fingerprint 
                marixFingerprintSimilitude [i][j]= oddt.fingerprints.tanimoto(fingerp1, fingerp2, sparse=False)
                print(marixFingerprintSimilitude [i][j])
                
                fingerp1 = pli_array[i].fingerprintSPLIF
                fingerp2 = pli_array[j].fingerprintSPLIF  
                val = oddt.fingerprints.similarity_SPLIF(fingerp1, fingerp2, rmsd_cutoff=1)
                marixFingerprintSPLIFSimilitude [i,j]= val
                
    print("similitude des fingerprint:")
    print(marixFingerprintSimilitude)
    print("similitude des fingerprintSPLIF: ")
    print(marixFingerprintSPLIFSimilitude)
        
    # quitte le programme Pymol
    pymol.cmd.quit()
    
    return marixReceptorRMSPymol, marixLigandRMSOpenBabel, marixFingerprintSimilitude,  marixFingerprintSPLIFSimilitude
# end 


'''
  Main 

'''
# # /!\    /!\    /!\    TOUS CES ELEMENTS SONT DEJA DANS LE FICHIER analyse_matrice.py     /!\    /!\    /!\
# # /!\    /!\    /!\    UTILISEZ CE MAIN UNIQUEMENT SI VOUS N'UTULISEZ PAS AVEC analys_matrice.py  /!\    /!\    /!\
# # 
# #fichier .csv qui me sert d'exemple pour tester le script :  exportBindingEnol3HNT.csv
# file1 = "exportBindingEnol3HNT.csv" # input("Saisissez le nom de votre fichier: ")
# # Coline :  
# root_data_dir = os.path.abspath('D:\PDB')
# # Cyril :  
# # root_data_dir = os.path.abspath('C:\BGene\PDB')
#  
#  
# # creation tableau de plistruct
# pli_array = crea_class.csv_pli_struct(file1)  
# # calcul des properties 
# compute_properties(pli_array, root_data_dir)
#  
# # calcul des matrices 
# marixReceptorRMSPymol, marixLigandRMSOpenBabel, marixFingerprintSimilitude,  marixFingerprintSPLIFSimilitude = compute_matrices(pli_array, root_data_dir )
