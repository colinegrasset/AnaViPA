import xml.etree.ElementTree as ET

def legendePheno(root):
    ET.SubElement(root, "ns0:rect", style="opacity:0.75299986;mix-blend-mode:normal;fill:#e30613;fill-opacity:0.64344263;fill-rule:nonzero;stroke:none;stroke-width:5.159;stroke-miterlimit:4;stroke-dasharray:none", id="rect1488", width="63.462658", height="31.731329", x="1004.5184", y="-124.28104", transform="scale(1,-1)")
    ET.SubElement(root, "ns0:rect", style='opacity:0.75;fill:#fab200;fill-opacity:0.76862746;stroke:none;stroke-width:6.09834;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1', id="rect1488-5", width="63.462658", height="31.731329", x="1004.5184", y="144.39932")
    ET.SubElement(root, "ns0:rect", style='fill:#bfffbf;fill-opacity:1;stroke:none;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;opacity:0.56', id="rect1488-8", width="63.462658", height="31.731329", x="1004.5184", y="196.98962")
    ET.SubElement(root, "ns0:rect", style='fill:#83d0f5;fill-opacity:0.7764706;stroke:none;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;opacity:0.69', id="rect1488-7", width="63.462658", height="31.731329", x="1004.1976", y="249.27013")
    ET.SubElement(root, "ns0:rect", style='fill:#0094da;fill-opacity:0.7647059;stroke:none;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.31275719;opacity:0.77299998', id="rect1488-6", width="63.462658", height="31.731329", x="1004.5184", y="301.17517")
    texte = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="115.92677", id="text1531")
    span = ET.SubElement(texte, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="115.92677")
    span.text = "Très négatif"
    texte2 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="166.48784", id="text1531-0")
    span = ET.SubElement(texte2, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="166.48784")
    span.text = "Négatif"
    texte3 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="221.64655", id="text1531")
    span = ET.SubElement(texte3, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="221.64655")
    span.text = "Neutre"
    texte4 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="275.87033", id="text1531")
    span = ET.SubElement(texte4, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="275.87033")
    span.text = "Positif"
    texte5 = ET.SubElement(root, "ns0:text", space="preserve", style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:24px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;fill:#000000;fill-opacity:1;stroke:none", x="1082.6063", y="325.41968", id="text1531")
    span = ET.SubElement(texte5, 'ns0:tspan', role="line", id="tspan1529", x="1082.6063", y="325.41968")
    span.text = "Très positif"

def carte_Pheno(map):
    tree = ET.parse(map)
    root = tree.getroot()
    legendePheno(root)
    tree.write('outputMapPheno.svg')

#Rectangle style
Tneg = 'opacity:0.75299986;mix-blend-mode:normal;fill:#e30613;fill-opacity:0.64344263;fill-rule:nonzero;stroke:none;stroke-width:5.159;stroke-miterlimit:4;stroke-dasharray:none'
neg = 'opacity:0.75;fill:#fab200;fill-opacity:0.76862746;stroke:none;stroke-width:6.09834;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1'
neutre = 'fill:none;fill-opacity:0.459272'
pos = 'fill:#83d0f5;fill-opacity:0.7764706;stroke:none;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;opacity:0.69'
Tpos = 'fill:#0094da;fill-opacity:0.7647059;stroke:none;stroke-width:6.04724;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.31275719;opacity:0.77299998'
carte_Pheno("carte_metabolique_pentose-arginine.svg")