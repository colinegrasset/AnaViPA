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
                            return True


idRect = "2.7.1.12"
map = "carte_metabolique_pentose-arginine.svg"
find = LinkSvg.readmap(map, idRect)
print(find)
