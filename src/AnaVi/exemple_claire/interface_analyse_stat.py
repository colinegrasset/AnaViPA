#_*_coding:Utf-8_*_

from tkinter import filedialog
from tkinter import *
from AnaVi.exemple_claire.fonctions import *
from lxml import etree

nom_fichier1 =''
nom_fichier2 =''
l=[]
l2=[]

###############################
##         FONCTIONS         ##
###############################


# Lecture du/des fichiers
def lecture_fichier1(nom_fichier):
    global l
    arbre = etree.parse(nom_fichier)
    racine = arbre.getroot()
    for noeud in arbre.xpath('//comparision'):
        for distances in noeud.xpath('distances'):
            s = distances.text
    l = s.split(' ')
    l = liste_entier(l)

def lecture_fichier2(nom_fichier):
    global l2
    arbre = etree.parse(nom_fichier)
    racine = arbre.getroot()
    for noeud in arbre.xpath('//comparision'):
        for distances in noeud.xpath('distances'):
            s = distances.text
    l2 = s.split(' ')
    l2 = liste_entier(l2)

# Détermination des paramètres des graphiques
def parametre_mini(l):
    try:
        mini = float(e1.get())
    except ValueError:
        mini = val_min(l)
    return mini

def parametre_maxi(l):
    try:
        maxi=float(e2.get())
    except ValueError:
        maxi = val_max(l)
    return maxi

def parametre_pas():
    try:
        pas = float(e3.get())
    except:
        pas = 0.001
    return pas

# Calculs statistiques 
def stat1(l):
    m=moyenne(l)
    moy1.set(m)
    vari=variance(l)
    var1.set(vari)
    etype=ecart_type(l)
    et1.set(etype)
    long=len(l)
    longueur1.set(long)
    valmin = val_min(l)
    vmin1.set(valmin)
    valmax = val_max(l)
    vmax1.set(valmax)

def stat2(l):
    m=moyenne(l)
    moy2.set(m)
    vari=variance(l)
    var2.set(vari)
    etype=ecart_type(l)
    et2.set(etype)
    long=len(l)
    longueur2.set(long)
    valmin = val_min(l)
    vmin2.set(valmin)
    valmax = val_max(l)
    vmax2.set(valmax)


##########################################
##         FONCTIONS DE COMMANDE        ##
##########################################

# Fonction pour choix du fichier
def fichier1():
    global nom_fichier1
    nom_fichier1 = filedialog.askopenfilename(filetypes=[("Text files","*.xml")])
    filename1.set(nom_fichier1)

def fichier2():
    global nom_fichier2
    nom_fichier2 = filedialog.askopenfilename(filetypes=[("Text files","*.xml")])
    filename2.set(nom_fichier2)


# Analyse des données du fichiers : calculs et tracés
def analyse():

    plt.close()
    
    global l
    global l2
    global nom_fichier1
    global nom_fichier2
    
    if nom_fichier1 and nom_fichier2:
        lecture_fichier1(nom_fichier1)
        lecture_fichier2(nom_fichier2)

        if courb.get() or point.get() or histo.get() or clisse.get():
            #parametres du tracé du graphique
            mini1 = parametre_mini(l)
            mini2 = parametre_mini(l2)
            if mini1 < mini2:
                mini = mini1
            else:
                mini = mini2

            maxi1 = parametre_maxi(l)
            maxi2 = parametre_maxi(l2)
            if maxi1 > maxi2:
                maxi = maxi1
            else:
                maxi = maxi2
            
            pas = parametre_pas()

            # creation de nouvelles listes correspondante aux paramètres
            lnew1 = nouvelle_liste(l,mini,maxi)
            lnew2 = nouvelle_liste(l2,mini,maxi)
            stat1(lnew1)
            stat2(lnew2)

            # tracés des graphiques demandés

            if histo.get():
                histodouble(lnew1,lnew2,mini,maxi,pas)
            if courb.get():
                courbedouble(lnew1,lnew2,mini,maxi,pas)
            if point.get():
                nuagedouble(lnew1,lnew2,mini,maxi,pas)
            if clisse.get():
                courbelissedouble(lnew1,lnew2,mini,maxi,pas)
            if courberep.get():
                courberepdouble(lnew1,lnew2)
            plt.show()

        else:
            stat1(l)
            stat2(l2)
            if courberep.get():
                courberepdouble(l,l2)
    elif nom_fichier1:
        lecture_fichier1(nom_fichier1)

        if courb.get() or point.get() or histo.get() or clisse.get():
            # parametres du tracé du graphique
            mini = parametre_mini(l)
            maxi = parametre_maxi(l)
            pas = parametre_pas()

            # création d'une nouvelle liste correspondante aux paramètres   
            lnew = nouvelle_liste(l,mini,maxi)
            stat1(lnew)

            # tracé des graphiques demandés
            if courb.get():
                courbe(lnew,mini,maxi,pas)
            if point.get():
                nuage_points(lnew,mini,maxi,pas)
            if histo.get():
                histogramme(lnew,mini,maxi,pas)
            if clisse.get():
                courbelisse(lnew,mini,maxi,pas)
            if courberep.get():
                courberepartition(lnew)
            plt.show()

        else:
            stat1(l)
            if courberep.get():
                courberepartition(l)
            plt.show()
            
    elif nom_fichier2:
        lecture_fichier2(nom_fichier2)

        if courb.get() or point.get() or histo.get() or clisse.get():
            # parametres du tracé du graphique
            mini = parametre_mini(l2)
            maxi = parametre_maxi(l2)
            pas = parametre_pas()

            # création d'une nouvelle liste correspondante aux paramètres   
            lnew = nouvelle_liste(l2,mini,maxi)
            stat2(lnew)

            # tracé des graphiques demandés 
            if courb.get():
                courbe(lnew,mini,maxi,pas)
            if point.get():
                nuage_points(lnew,mini,maxi,pas)
            if histo.get():
                histogramme(lnew,mini,maxi,pas)
            if clisse.get():
                courbelisse(lnew,mini,maxi,pas)
            if courberep.get():
                courberepartition(lnew)
            plt.show()

        else:
            stat2(l2)
            if courberep.get():
                courberepartition(l2)
            plt.show()

def export1(stats):
    fichier = etree.SubElement(stats, "fichier")
    fichier.set("nom_fichier", nom_fichier1)
    moyenne = etree.SubElement(fichier, "moyenne")
    moyenne.text = str(moy1.get())
    variance = etree.SubElement(fichier, "variance")
    variance.text = str(var1.get())
    etype = etree.SubElement(fichier, "ecart_type")
    etype.text = str(et1.get())
    long = etree.SubElement(fichier, "nombre_points")
    long.text = str(longueur1.get())
    valmin = etree.SubElement(fichier, "valeur_minimum")
    valmin.text = str(vmin1.get())
    valmax = etree.SubElement(fichier, "valeur_maximum")
    valmax.text = str(vmax1.get())
    return(stats)

def export2(stats):
    fichier = etree.SubElement(stats, "fichier")
    fichier.set("nom_fichier", nom_fichier2)
    moyenne = etree.SubElement(fichier, "moyenne")
    moyenne.text = str(moy2.get())
    variance = etree.SubElement(fichier, "variance")
    variance.text = str(var2.get())
    etype = etree.SubElement(fichier, "ecart_type")
    etype.text = str(et2.get())
    long = etree.SubElement(fichier, "nombre_points")
    long.text = str(longueur2.get())
    valmin = etree.SubElement(fichier, "valeur_minimum")
    valmin.text = str(vmin2.get())
    valmax = etree.SubElement(fichier, "valeur_maximum")
    valmax.text = str(vmax2.get())
    return(stats)

def export():
    stats = etree.Element("stats")
    doc = etree.ElementTree(stats)
    if nom_fichier1:
        stats = export1(stats)
    if nom_fichier2:
        stats = export2(stats)
    doc.write("statistiques.xml", xml_declaration=True, encoding='UTF-8', pretty_print=True)
    
# CREATION DE LA FENETRE
fenetre = Tk()
fenetre.title('Analyse statistique des comparaisons')
fenetre.geometry('440x650')


###########################
##       VARIABLES       ##
###########################

# Variables checkbox
courb = IntVar()
point = IntVar()
histo = IntVar()
clisse = IntVar()
courberep = IntVar()

#Variable nom fichier
filename1 = StringVar()
filename2 = StringVar()

#Variable pour les stats
moy1 = DoubleVar()
moy2 = DoubleVar()
var1 = DoubleVar()
var2 = DoubleVar()
et1 = DoubleVar()
et2 = DoubleVar()
longueur1 = IntVar()
longueur2 = IntVar()
vmin1 = DoubleVar()
vmin2 = DoubleVar()
vmax1 = DoubleVar()
vmax2 = DoubleVar()


##########################
##        FRAMES        ##
##########################

# Frame pour le choix du fichier
f1 = Frame(fenetre, bg='#eeeeee')
f1.place(x=0, y=0, width = 440, height = 95)
sf11 = Frame(f1, bg='#eeeeee')
sf11.place(x=10, y=30, width = 400, height =75)
sf12 = Frame(fenetre, bg='#eeeeee')
sf12.place(x=10, y=10, width = 400, height = 20)

#Frame boutons quitter et exporter
f2 = Frame(fenetre, bg='#aaaaaa')
f2.place(x=0, y=620, width = 440, height = 45)

#Frame du choix du graphique
f3 = Frame(fenetre)
f3.place(x=10, y=300, width = 440, height = 150)
sf1 = Frame(f3)
sf1.place (x=0,y=0, width = 300, height = 20)
sf2 = Frame(f3)
sf2.place (x=10,y=30, width = 300, height =15)
sf3 = Frame(f3)
sf3.place (x=10,y=50, width = 300, height =15)
sf4 = Frame(f3)
sf4.place (x=10,y=70, width = 300, height =15)
sf5 = Frame(f3)
sf5.place (x=10,y=90, width = 300, height =15)
sf6 = Frame(f3)
sf6.place (x=10,y=120, width = 400, height =30)

#Frame du paramétrage
f5 = Frame(fenetre, bg='#dddddd')
f5.place(x=0,y=95, width = 440, height = 180)
sf51 = Frame(f5, bg='#dddddd')
sf51.place(x=10,y=5, width = 350, height = 20)
sf52 = Frame(f5, bg='#dddddd')
sf52.place(x=20,y=80, width = 350, height = 100)
sf53 = Frame(f5, bg='#dddddd')
sf53.place(x=20,y=30, width = 350, height = 30)
sf54 = Frame(f5, bg='#dddddd')
sf54.place(x=20,y=150, width = 300, height = 20)

#Frame des résultats (stats)
f4 = Frame(fenetre, bg='#aaaaaa')
f4.place(x=0,y=455, width=440, height=165)
sf41 = Frame(f4, bg='#aaaaaa')
sf41.place(x=10,y=10, width=300,height=20)
sf42 = Frame(f4, bg='#aaaaaa')
sf42.place(x=20,y=40, width=410,height=20)
sf43 = Frame(f4, bg='#aaaaaa')
sf43.place(x=20,y=60, width=410,height=20)
sf44 = Frame(f4, bg='#aaaaaa')
sf44.place(x=20,y=80, width=410,height=20)
sf45 = Frame(f4, bg='#aaaaaa')
sf45.place(x=20,y=100, width=410,height=20)
sf46 = Frame(f4, bg='#aaaaaa')
sf46.place(x=20,y=120, width=410,height=20)
sf47 = Frame(f4, bg='#aaaaaa')
sf47.place(x=20,y=140, width=410,heigh=20)
sf48 = Frame(f4, bg='#aaaaaa')
sf48.place(x=170, y=20, width=90, height=20)
sf49 = Frame(f4, bg='#aaaaaa')
sf49.place(x=290, y=20, width=90, height=20)

##########################
##      AFFICHAGE       ##
##########################

#Affichage stats
Resultat = Label (sf41, text = 'Résultats : ', font = ("Futura", 12), bg='#aaaaaa')
Resultat.pack(side='left')

fich1 = Label (sf48, text = 'fichier 1',  bg='#aaaaaa')
fich1.pack()

fich2 = Label (sf49, text = 'fichier 2',  bg='#aaaaaa')
fich2.pack()

Nom_moy = Label (sf42, text='Moyenne des distances : ', bg='#aaaaaa')
Nom_moy.grid(row=1,column=0)
Affmoy1 = Label(sf42, textvariable=moy1, bg='#aaaaaa')
Affmoy1.place(x=170)
Affmoy1 = Label(sf42, textvariable=moy2, bg='#aaaaaa')
Affmoy1.place(x=290)

Nom_var = Label(sf43, text='Variance : ', bg='#aaaaaa')
Nom_var.grid(row=2,column=0)
Affvar1 = Label(sf43, textvariable=var1, bg='#aaaaaa')
Affvar1.place(x=170)
Affvar2 = Label(sf43, textvariable=var2, bg='#aaaaaa')
Affvar2.place(x=290)

Nom_et = Label(sf44, text='Ecart-type : ', bg='#aaaaaa')
Nom_et.grid(row=3,column=0)
Affet1 = Label(sf44, textvariable=et1, bg='#aaaaaa')
Affet1.place(x=170)
Affet2 = Label(sf44, textvariable=et2, bg='#aaaaaa')
Affet2.place(x=290)

Nom_long = Label(sf45, text='Nombre de points : ', bg='#aaaaaa')
Nom_long.grid(row=4,column=0)
Afflongueur1 = Label(sf45, textvariable=longueur1, bg='#aaaaaa')
Afflongueur1.place(x=170)
Afflongueur2 = Label(sf45, textvariable=longueur2, bg='#aaaaaa')
Afflongueur2.place(x=290)

Nom_vmin = Label(sf46, text='Valeur minimale : ', bg='#aaaaaa')
Nom_vmin.grid(row=5,column=0)
Affvmin1 = Label(sf46, textvariable=vmin1, bg='#aaaaaa')
Affvmin1.place(x=170)
Affvmin2 = Label(sf46, textvariable=vmin2, bg='#aaaaaa')
Affvmin2.place(x=290)

Nom_vmax = Label(sf47, text='Valeur maximale : ', bg='#aaaaaa')
Nom_vmax.grid(row=6,column=0)
Affvmax1 = Label(sf47, textvariable=vmax1, bg='#aaaaaa')
Affvmax1.place(x=170)
Affvmax2 = Label(sf47, textvariable=vmax2, bg='#aaaaaa')
Affvmax2.place(x=290)

# Affichage choix fichier
message = Label(sf12, text = "Fichiers a analysé : ", font = ("Futura", 12))
message.pack(side='left')

bouton1=Button(sf11, text="choix fichier 1", font=("Futura", 10),relief="groove", command = fichier1)
bouton1.grid(row=1, column=1)

fichier1 = Label (sf11, textvariable = filename1, font=("Futura", 10),borderwidth=1,bg='white', relief="sunken", width="38", height="1",anchor="nw")
fichier1.grid(row=1,column=0)

bouton2=Button(sf11, text="choix fichier 2", font=("Futura", 10),relief="groove", command = fichier2)
bouton2.grid(row=2, column=1)

fichier2 = Label (sf11, textvariable = filename2, font=("Futura", 10),borderwidth=1,bg='white', relief="sunken", width="38", height="1",anchor="nw")
fichier2.grid(row=2,column=0)

#Affichage du paramétrage
param= Label(sf51, bg='#dddddd', text = 'Paramétrage des représentations graphiques : ', font = ("Futura", 12))
param.pack(side='left')

infos = Label(sf53, bg='#dddddd', text = "Les valeurs par défaut sont les valeurs minimales et \n maximales de l'échantillon avec un pas de 0.001", font = ("Futura", 9))
infos.pack(side='left')    

te1 = Label(sf52, text ='X min : ', font =("Futura",9), bg='#dddddd')
te1.grid(row=0,column=0)
e1 = Entry(sf52)
e1.grid(row=0,column=1)

te2 = Label(sf52, text ='X max : ', font =("Futura",9), bg='#dddddd')
te2.grid(row=1,column=0)
e2 = Entry(sf52)
e2.grid(row=1,column=1)

te3 = Label(sf52, text ='Pas : ', font =("Futura",9), bg='#dddddd')
te3.grid(row=2,column=0)
e3 = Entry(sf52)
e3.grid(row=2,column=1)

cr=Checkbutton(sf54, text='Tracé une courbe de répartition', variable=courberep, bg='#dddddd')
cr.pack(side='left')

#Affichage boutons exporter et quitter
b2=Button(f2, text="quitter", font=("Futura", 10),relief="groove", command = fenetre.destroy)
b2.place(x=390)

bexport = Button (f2, text="exporter", font=("Futura", 10),relief="groove", command = export)
bexport.place(x=320)

#Affichage choix de graphique
graph= Label(sf1, text = 'Représentations graphiques : ', font = ("Futura", 12))
graph.pack(side='left')

g1=Checkbutton(sf2, text='Courbe', variable=courb)
g2=Checkbutton(sf3, text='Nuage de points', variable=point)
g3=Checkbutton(sf4, text='Histogramme', variable=histo)
g4=Checkbutton(sf5, text='Courbe lissée', variable=clisse)
g1.pack(side='left')
g2.pack(side='left')
g3.pack(side='left')
g4.pack(side='left')

b3=Button(sf6, text='Analyser', font=("Futura", 10),relief="groove", command = analyse)
b3.pack(side='bottom')

#LANCEMENT DE LA FENETRE
fenetre.mainloop()
