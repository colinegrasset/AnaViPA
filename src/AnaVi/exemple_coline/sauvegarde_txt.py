# vim: set fileencoding=utf-8 :
import os
import subprocess
import json
import pickle
import analyse_matrice

######################   VERSION FORMAT JSON     ############################

#pour importer chaine json utiliser la m�thode: json.loads()
#pour convertir en chaine python en chaine JSON utiliser la methode: json.dumps()
name = "nom du complexe: "
complexe = analyse_matrice.file1
xyT = "coordonnees des solutions Tanimoto: "
tanimoto = analyse_matrice.allT
xyD = "coordonnees des solutions Distance RMSD: "
rmsd = analyse_matrice.allD
data = [name,complexe,xyT,tanimoto,xyD, rmsd]


with open("result_analysis.json", "w+") as out :
  json.dump(data, out)
out.close()
# with open("result_analysis.json", "w") as write_file:
#    integration = json.dumps(data)
#    print("voici ce qui est insere dans le fichier json")
#    print(integration)
# write_file.close()    

    # ... A COMPLETER ENCORE AVEC D'AUTRES DONNEES ..?
    
    ######################   VERSION FORMAT TEXTE     ##########################
path = os.path.abspath('C:/Users/bgene-admin/git/python/stagecoline/resultat_analyse.txt')

with open(path, 'w') as save_data:
    save_data.write("***********************************")
    save_data.write("\n")
    save_data.write("ANALYSE DU COMPLEXE:")
    save_data.write(analyse_matrice.file1)
    save_data.write("\n")
    save_data.write("***********************************")
    save_data.write("\n")
    save_data.write("\n")
  
    ########    #######    ########    ######
    save_data.write("Analyse des distances RMSD il y a ")
    save_data.write(str(analyse_matrice.nbD))
    
    save_data.write(" solutions correspondant au(x) coordonnees suivantes: " )
    save_data.write("\n")
    save_data.write(str(analyse_matrice.allD))
    save_data.write("\n")
    save_data.write("ayant pour distance RMSD respective:")
    save_data.write(str(analyse_matrice.clusterrmsd))
    save_data.write("\n")
    save_data.write("le plafond de distance max etant fixe a ")
    save_data.write(str(analyse_matrice.seuilrmsd))
    save_data.write("\n")
    save_data.write("\n")
    save_data.write("\n")
    
    ########    #######    ########    ######
    save_data.write("Comparaison des fingerprint TANIMOTO il y a ")
    save_data.write(str(analyse_matrice.nbT))
    
    save_data.write(" solutions correspondant au(x) coordonnees suivantes: " )
    save_data.write("\n")
    save_data.write(str(analyse_matrice.allT))
    save_data.write("\n")
    save_data.write("ayant pour score de similitude respectif (score_max = 1) :")
    save_data.write(str(analyse_matrice.clustertanimoto))
    save_data.write("\n")
    save_data.write("le seuil score mini etant fixe a ")
    if analyse_matrice.nbT == 0:
        save_data.write(str(analyse_matrice.seuilfingerprint))
    else:
        save_data.write("0.4")
    save_data.write("\n") 
    save_data.write("\n")       

    ########    #######    ########    ######

    save_data.write("Resultats de comparaison Tanimoto avec celle du fingerprintSPLIF: ")
    save_data.write("\n")
    save_data.write("le nombre de solution de fingerprintSPLIF est de ")
    save_data.write(str(analyse_matrice.nbS))
    save_data.write("\n")
    
    save_data.write("leurs coordonnees sont: " )
    save_data.write(str(analyse_matrice.allS))
    save_data.write("\n")
    save_data.write("ayant pour score de similitude respectif (score_max = 1) :")
    save_data.write(str(analyse_matrice.clustersplif))
    save_data.write("\n")
    save_data.write("le seuil score mini etant fixe a ")
    if analyse_matrice.nbS == 0:
        save_data.write(str(analyse_matrice.seuilfingerprint))
    else:
        save_data.write("0.4")
    save_data.write("\n")  
    save_data.write("\n")  
    
    

save_data.close()