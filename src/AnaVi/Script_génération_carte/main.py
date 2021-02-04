#!/usr/bin/python

import xml.etree.ElementTree as ET
from AnaVi.Script_génération_carte.Link_svg import readmap, legende
from AnaVi.Script_génération_carte.dictionary_mutation import fillingDict

import re



def main(fileGeno,fileECnum,strainSearch,mapM):
    listEcSouche = fillingDict(fileGeno,fileECnum)
    print( "************************************")
    for i in listEcSouche:
        # tree = ET.parse(mapM)
        # root = tree.getroot()
        # legende(root)
        if i.strain == strainSearch:
            print(i.mutation)
            for p in i.mutation.keys():
                print(p)

                regleD = re.compile(r"^DELTA")
                repD = list(regleD.finditer(p))
                regleI = re.compile(r"^::")
                repI = list(regleI.finditer(p))
                regleSo = re.compile(r"\(-\)")
                repSo = list(regleSo.finditer(p))
                regleSu = re.compile(r"\(+\)")
                repSu = list(regleSu.finditer(p))
                regleM = re.compile(r"\(fbr\)")
                repM = list(regleM.finditer(p))

                print(i.mutation[p])

                if repD != []:
                    readmap(mapM, i.mutation[p], deletion)
                elif repI != []:
                    readmap(mapM, i.mutation[p], insertion)
                elif repSo != []:
                    readmap(mapM, i.mutation[p], sousExpression)
                elif repSu != []:
                    readmap(mapM, i.mutation[p], surExpression)
                elif repM != []:
                    readmap(mapM, i.mutation[p], mutantFbr)

            #tree.write('outputMap.svg')








sousExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f68c00;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
deletion = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f61800;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
mutantFbr = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#ab38bd;stroke-opacity:1'
insertion = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#4838bd;stroke-opacity:1'
surExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#22d327;stroke-opacity:1'


# path de coline
main("C://Users//User//IdeaProjects//AnaVi//src//AnaVi//Script_génération_carte//tablGeno.csv",
     "C://Users//User//IdeaProjects//AnaVi//src//AnaVi//Script_génération_carte//tablECnum.csv",
     "5","carte_metabolique_pentose-arginine.svg")

# path de Rachel
#fillingDict("C://Users//Utilisateur//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablGeno.csv",
#           "C://Users//Utilisateur//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablECnum.csv")

# path de lucie
#fillingDict("C://Users//yuibl//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablGeno.csv",
#            "C://Users//yuibl//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablECnum.csv")

#path Claire
#fillingDict("//Users//claire//Desktop//M1Gphy//ProjetAnnuel//src//AnaVi//Script_génération_carte//tablGeno.csv",
#            "//Users//claire//Desktop//M1Gphy//ProjetAnnuel//src//AnaVi//Script_génération_carte//tablECnum.csv")