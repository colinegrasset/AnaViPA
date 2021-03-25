import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def barplot(listSouche,numSouche):
    fig = plt.figure()
    plt.bar(range(3), listSouche)
    plt.xticks(range(3), ['DO 6h','DO 24h','DO Production'])
    plt.title('DO souche '+str(numSouche))
    fig.savefig('barplot.png', dpi=fig.dpi)

def addBarplotSVG(mapOutput):
    tree = ET.parse(mapOutput)
    root = tree.getroot()
    ET.SubElement(root,'ns0:image', href="barplot.png",id="image1037", x="31.137264", y="695.38867", height="325.21158", width="361.79694")
    tree.write('outputMapBarplot.svg')