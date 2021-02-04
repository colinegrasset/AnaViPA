import xml.etree.ElementTree as ET
import re



def legende(root):
    root.insert(3, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#09a001;stroke-width:5.15906" id="rect1488" width="63.462658" height="31.731329" x="1003.5033" y="-124.28104" transform="scale(1,-1)" '))
    root.insert(4, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#4838bd;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-8" width="63.462658" height="31.731329" x="1004.5184" y="196.98962" '))
    root.insert(5, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#ab38bd;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-6" width="63.462658" height="31.731329" x="1004.051" y="301.17517" '))
    root.insert(6, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#f61800;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-7" width="63.462658" height="31.731329" x="1004.1976" y="249.27013" '))
    root.insert(7, ET.Element('ns0:rect style="fill:#f9f9f9;fill-opacity:0.26;stroke:#f68c00;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" id="rect1488-5" width="63.462658" height="31.731329" x="1004.2778" y="144.39932" '))
    #root.insert(8, ET.Element("ns0":"text", xml:space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="115.92677", id="text1531" "))
    texte = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="115.92677", id="text1531")
    span = ET.SubElement(texte, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="115.92677")
    span.text = "Sur-expression"
    texte2 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="166.48784", id="text1531-0")
    span = ET.SubElement(texte2, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="166.48784")
    span.text = "Sous-expression"
    texte3 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="221.64655", id="text1531")
    span = ET.SubElement(texte3, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="221.64655")
    span.text = "Insertion"
    texte4 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="275.87033", id="text1531")
    span = ET.SubElement(texte4, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="275.87033")
    span.text = "Délétion"
    texte5 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="325.41968", id="text1531")
    span = ET.SubElement(texte5, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="325.41968")
    span.text = "Mutant"
    span2 = ET.SubElement(span, 'ns0:tspan', style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal", id="tspan1575")
    span2.text = " fbr"

def readmap(mapM, dict):
    tree = ET.parse(mapM)
    root = tree.getroot()
    legende(root)
    for child in root:
        if child.tag == "{http://www.w3.org/2000/svg}g":
            for grandchild in child:
                if grandchild.tag == "{http://www.w3.org/2000/svg}rect":
                    for p in dict.keys():

                        if grandchild.attrib['id'] == dict[p]:

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

                            print(dict[p])

                            if repD != []:
                                grandchild.set('style', deletion)
                            elif repI != []:
                                grandchild.set('style', insertion)
                            elif repSo != []:
                                grandchild.set('style', sousExpression)
                            elif repSu != []:
                                grandchild.set('style', surExpression)
                            elif repM != []:
                                grandchild.set('style', mutantFbr)

    tree.write('outputMap.svg')


sousExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f68c00;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
deletion = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f61800;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
mutantFbr = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#ab38bd;stroke-opacity:1'
insertion = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#4838bd;stroke-opacity:1'
surExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:1.600;stroke-miterlimit:4;stroke-dasharray:none;stroke:#22d327;stroke-opacity:1'

#idRect = "2.7.1.12"

#map = "carte_metabolique_pentose-arginine.svg"

#LinkSvg.readmap(map, idRect, insertion)


