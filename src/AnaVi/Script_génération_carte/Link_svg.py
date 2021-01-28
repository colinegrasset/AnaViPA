import xml.etree.ElementTree as ET


class LinkSvg:

    def __init__(self):
        # Metabolic map
        self.mapM = None

    def readmap(mapM, idrect, modification):
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

sousExpression = 'opacity:0.985;fill:none;fill-opacity:0;stroke:#f68c00;stroke-width:0.964999;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
surExpression = 'opacity:0.985;fill:none;fill-opacity:0;stroke:#f61800;stroke-width:0.964999;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
idRect = "2.7.1.12"
map = "carte_metabolique_pentose-arginine.svg"
LinkSvg.readmap(map, idRect, sousExpression)



violet = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:0.965;stroke-miterlimit:4;stroke-dasharray:none;stroke:#ab38bd;stroke-opacity:1'
bleu = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:0.965;stroke-miterlimit:4;stroke-dasharray:none;stroke:#4838bd;stroke-opacity:1'
vert = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.365;stroke-miterlimit:4;stroke-dasharray:none;stroke:#22d327;stroke-opacity:1'
