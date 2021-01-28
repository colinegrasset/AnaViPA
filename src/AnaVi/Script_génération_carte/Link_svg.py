import xml.etree.ElementTree as ET


class LinkSvg:

    def __init__(self):
        # Metabolic map
        self.mapM = None

    def readmap(mapM, idrect):
        tree = ET.parse(mapM)
        root = tree.getroot()
        for child in root:
            if child.tag == "{http://www.w3.org/2000/svg}g":
                for grandchild in child:
                    if grandchild.tag == "{http://www.w3.org/2000/svg}rect":

                        if grandchild.attrib['id'] == idrect:
                            print(grandchild.tag, grandchild.attrib['id'])
                            grandchild.set('style', vert)
                            tree.write('outputMap.svg')

idRect = "2.7.1.12"
map = "carte_metabolique_pentose-arginine.svg"


violet = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:0.965;stroke-miterlimit:4;stroke-dasharray:none;stroke:#ab38bd;stroke-opacity:1'
bleu = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:0.965;stroke-miterlimit:4;stroke-dasharray:none;stroke:#4838bd;stroke-opacity:1'
vert = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.365;stroke-miterlimit:4;stroke-dasharray:none;stroke:#22d327;stroke-opacity:1'

LinkSvg.readmap(map, idRect)