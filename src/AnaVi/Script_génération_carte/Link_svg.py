from lxml import etree

class Link_svg:

    def __init__(self):
        # Carte métabolique
        self.carteM = None

    def readCarte(carteM):
        tree = etree.parse(carteM)
        root = tree.getroot()
        #for noeud in tree.xpath('.//svg/g/rect'):
        #print(tree.findall('.//svg/g/rect[@id]'))
        print(tree.find(getelementpath(id))
carte = "carte_metabolique_pentose-arginine.svg"
Link_svg.readCarte(carte)