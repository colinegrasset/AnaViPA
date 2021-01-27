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
                            #print(grandchild.tag, grandchild.attrib['id'])
                            grandchild.set('style', 'opacity:0.99;fill:#e24620;fill-opacity:0.68032789;stroke-width:0.264583')
                            tree.write('outputMap.svg')

idRect = "2.7.1.12"
map = "carte_metabolique_pentose-arginine.svg"
LinkSvg.readmap(map, idRect)
