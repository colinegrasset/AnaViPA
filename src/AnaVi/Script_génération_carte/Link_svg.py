import xml.etree.ElementTree as ET

class LinkSvg:

    def __init__(self):
        # Metabolic map
        self.mapM = None

    def legende(root):
        root.insert(3, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#09a001;stroke-width:5.15906" id="rect1488" width="63.462658" height="31.731329" x="1003.5033" y="-124.28104" transform="scale(1,-1)" '))
        root.insert(4, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#4838bd;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-8" width="63.462658" height="31.731329" x="1004.5184" y="196.98962" '))
        root.insert(5, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#ab38bd;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-6" width="63.462658" height="31.731329" x="1004.051" y="301.17517" '))
        root.insert(6, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#f61800;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-7" width="63.462658" height="31.731329" x="1004.1976" y="249.27013" '))
        root.insert(6, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#f68c00;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-5" width="63.462658" height="31.731329" x="1004.2778" y="144.39932" '))

    def readmap(mapM, idrect, modification):
        tree = ET.parse(mapM)
        root = tree.getroot()
        LinkSvg.legende(root)
        for child in root:
            if child.tag == "{http://www.w3.org/2000/svg}g":
                for grandchild in child:
                    if grandchild.tag == "{http://www.w3.org/2000/svg}rect":
                        if grandchild.attrib['id'] == idrect:
                            print(grandchild.tag, grandchild.attrib['id'])
                            grandchild.set('style', modification)
                            tree.write('outputMap.svg')


sousExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f68c00;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
deletion = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f61800;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
mutantFbr = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#ab38bd;stroke-opacity:1'
insertion = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#4838bd;stroke-opacity:1'
surExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#22d327;stroke-opacity:1'

idRect = "2.7.1.12"

map = "carte_metabolique_pentose-arginine.svg"

LinkSvg.readmap(map, idRect, insertion)


