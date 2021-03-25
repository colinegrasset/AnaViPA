import xml.etree.ElementTree as ET
import re



def legende(root):
    '''
    Function to write the legend on the map
    :param root:the root of the svg file parsing
    '''

    # Addition of legend rectangle
    ET.SubElement(root, 'ns0:rect', style="fill:#f9f9f9;fill-opacity:0.26;stroke-width:7.55905512;stroke-miterlimit:4;stroke-dasharray:none;stroke:#0ea139;stroke-opacity:1", id="rect1488", width="63.462658", height="31.731329", x="1003.5033", y="-124.28104", transform="scale(1,-1)")
    ET.SubElement(root, 'ns0:rect', style="fill:#f9f9f9;fill-opacity:0.26;stroke-width:7.55905512;stroke-miterlimit:4;stroke-dasharray:none;stroke:#009fe3;stroke-opacity:1", id="rect1488-8", width="63.462658", height="31.731329", x="1004.5184", y="196.98962")
    ET.SubElement(root, 'ns0:rect', style="fill:#f9f9f9;fill-opacity:0.26;stroke:#ab38bd;stroke-width:7.55905512;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1", id="rect1488-6", width="63.462658", height="31.731329", x="1004.051", y="301.17517")
    ET.SubElement(root, 'ns0:rect', style="fill:#f9f9f9;fill-opacity:0.26;stroke:#f61800;stroke-width:7.55905512;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1", id="rect1488-7", width="63.462658", height="31.731329", x="1004.1976", y="249.27013")
    ET.SubElement(root, 'ns0:rect', style="fill:#f9f9f9;fill-opacity:0.26;stroke:#f7a600;stroke-width:7.55905512;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1", id="rect1488-5", width="63.462658", height="31.731329", x="1004.2778", y="144.39932")
    # Addition of the text of the legend
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
    """
    A function that modifies the map to make appear strain's modifications
    :param mapM: the basemap
    :param dict: the dictionary of modifications and EC number for this strain
    :return: create the map which is an output file named "outputMap.svg"
    """

    # Parsing of the svg file
    tree = ET.parse(mapM)
    root = tree.getroot()
    legende(root)
    # Range of the svg file to acces to "rect" tag
    #print(root.tag)

    for child in root:
        #print(child.tag)
        if child.tag == "{http://www.w3.org/2000/svg}g":
            for grandchild in child:
                if grandchild.tag == "{http://www.w3.org/2000/svg}rect":
                    for p in dict.keys():
                        # Searching for the modification type for each ECnumber (rectangle id)
                        if grandchild.attrib['id'] == dict[p] or grandchild.attrib['id'] == dict[p] + "(2)":
                            regleD = re.compile(r"^DELTA")
                            repD = list(regleD.finditer(p))
                            regleI = re.compile(r"^::")
                            repI = list(regleI.finditer(p))
                            regleSo = re.compile(r"\(-\)")
                            repSo = list(regleSo.finditer(p))
                            regleSu = re.compile(r"\([+]\)")
                            repSu = list(regleSu.finditer(p))
                            regleM = re.compile(r"\(fbr\)")
                            repM = list(regleM.finditer(p))


                            # Modification of the rectangle style according to the modification
                            if repD != []:
                                regle= re.compile(r"DELTA")
                                texte=regle.sub("", p)



                                grandchild.set('style', deletion)
                                x = grandchild.attrib['x']
                                y = grandchild.attrib['y']

                                y1 = float(y)+15
                                y2 = float(y)+30
                                ET.SubElement(root, 'ns0:rect', style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:50px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#ffffff;fill-opacity:1;stroke:none", id="rect1500", width="40", height="20", x=x, y=str(y1))
                                txt = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:italic;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:12px;line-height:1.5;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#ff0000;fill-opacity:1;stroke:true;", x=x, y=str(y2), id="text1531")
                                span = ET.SubElement(txt, 'ns0:tspan', role="line", id="tspan1529", x=x, y=str(y2))
                                span.text = texte
                            elif repI != []:
                                regle2 = re.compile(r"^::")
                                texte=regle2.sub("", p)
                                grandchild.set('style', deletion)
                                x = grandchild.attrib['x']
                                y = grandchild.attrib['y']

                                y1 = float(y)+15
                                y2 = float(y)+30
                                ET.SubElement(root, 'ns0:rect', style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:50px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#ffffff;fill-opacity:1;stroke:none", id="rect1500", width="40", height="20", x=x, y=str(y1))
                                txt = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:italic;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:12px;line-height:1.5;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#0000ff;fill-opacity:1;stroke:true;", x=x, y=str(y2), id="text1531")
                                span = ET.SubElement(txt, 'ns0:tspan', role="line", id="tspan1529", x=x, y=str(y2))
                                span.text = texte
                                grandchild.set('style', insertion)
                            elif repSo != []:
                                regle3 = re.compile(r"\(-\)")
                                texte=regle3.sub("", p)
                                grandchild.set('style', deletion)
                                x = grandchild.attrib['x']
                                y = grandchild.attrib['y']

                                y1 = float(y)+15
                                y2 = float(y)+30
                                ET.SubElement(root, 'ns0:rect', style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:50px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#ffffff;fill-opacity:1;stroke:none", id="rect1500", width="40", height="20", x=x, y=str(y1))
                                txt = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:italic;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:12px;line-height:1.5;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#ff7f2a;fill-opacity:1;stroke:true;", x=x, y=str(y2), id="text1531")
                                span = ET.SubElement(txt, 'ns0:tspan', role="line", id="tspan1529", x=x, y=str(y2))
                                span.text = texte

                                grandchild.set('style', sousExpression)
                            elif repSu != []:
                                regle4 = re.compile(r"\([+]\)")
                                texte=regle4.sub("", p)
                                grandchild.set('style', deletion)
                                x = grandchild.attrib['x']
                                y = grandchild.attrib['y']
                                y1 = float(y)+15
                                y2 = float(y)+30
                                ET.SubElement(root, 'ns0:rect', style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:50px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#ffffff;fill-opacity:1;stroke:none", id="rect1500", width="40", height="20", x=x, y=str(y1))
                                txt = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:italic;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:12px;line-height:1.5;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#008000;fill-opacity:1;stroke:true;", x=x, y=str(y2), id="text1531")
                                span = ET.SubElement(txt, 'ns0:tspan', role="line", id="tspan1529", x=x, y=str(y2))
                                span.text = texte

                                grandchild.set('style', surExpression)
                            elif repM != []:
                                regle5 = re.compile(r"\(fbr\)")
                                texte=regle5.sub("", p)
                                grandchild.set('style', deletion)
                                x = grandchild.attrib['x']
                                y = grandchild.attrib['y']
                                y1 = float(y)+15
                                y2 = float(y)+30
                                ET.SubElement(root, 'ns0:rect', style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:50px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#ffffff;fill-opacity:1;stroke:none", id="rect1500", width="40", height="20", x=x, y=str(y1))
                                txt = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:italic;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:12px;line-height:1.5;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#800080;fill-opacity:1;stroke:true;", x=x, y=str(y2), id="text1531")
                                span = ET.SubElement(txt, 'ns0:tspan', role="line", id="tspan1529", x=x, y=str(y2))
                                span.text = texte
                                grandchild.set('style', mutantFbr)
                # Write a new svg file : the map with gene modifications
                tree.write('outputMap.svg')



# Rectangle styles on the map according to the modification type
sousExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f7a600;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
deletion = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#f61800;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
mutantFbr = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke:#ab38bd;stroke-opacity:1'
insertion = 'fill:#f9f9f9;fill-opacity:0.26;stroke:#009fe3;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;opacity:1'
surExpression = 'fill:#f9f9f9;fill-opacity:0.26;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke:#0ea139;stroke-opacity:1'



