from lxml import etree
import xml.etree.ElementTree as ET

class Link_svg:

    def __init__(self):
        # Carte métabolique
        self.carteM = None

    def readCarte(carteM):
        NS = {'svg': 'http://www.w3.org/2000/svg'}

        #print(carteM)
        tree = ET.parse(carteM)
        root = tree.getroot()

        for r in root:
            for i in r.tag:
                print(i);
                if i == "g":
                    return("ok");
                    print("tot");
            #print(r.find(".//g").tag)
            #id = r.get('id')
            #print(r.tag)
        #print(tree.findall(.//svg/g/rect.attrib['id']))
        #print(tree.find(tree.getelementpath(id)))

carte = "carte_metabolique_pentose-arginine.svg"
print(Link_svg.readCarte(carte));