#_*_coding:Utf-8_*_

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev


## FONCTIONS CALCULS STATISTIQUES ##

def liste_entier(l):
    i=0
    while i<len(l):
        l[i] = float(l[i])
        i +=1
    else:
        return(l)

def moyenne(l):
    somme=0
    for elt in l:
        somme+=elt
    if len(l) != 0:
        return(somme/len(l))
    else :
        return(0)

def variance(l):
    somme=0
    for elt in l:
        somme+=((elt-moyenne(l))**2)
    if len(l) != 0:
        return(somme/len(l))
    else:
        return(0)

def ecart_type(l):
    return(np.sqrt(variance(l)))


def val_min(l):
    mini=1000
    for elt in l:
        if elt < mini:
            mini = elt
    else:
        if mini != 1000:
            return(mini)
        else:
            return(0)

def val_max(l):
    maxi=0
    for elt in l:
        if elt > maxi:
            maxi = elt
    else:
        return(maxi)


## FONCTIONS GRAPHIQUES ##
    
# Fonctions pour la création des listes pour les tracés graphiques

def gener_liste(mini,maxi,pas):
    liste = np.arange(mini,(maxi+pas),pas)
    return(liste)

def gener_liste_dixieme():
    liste = np.arange(0.0,1.1,0.1)
    return(liste)

def count_range(l,mini,maxi):
    nb = 0
    for elt in l:
        if isinstance(elt, float):
            if (elt >= mini) and (elt < maxi):
                nb += 1
    else:
        return(nb)


def nb_occurence(l,lx,pas):
    ly=[]
    long = len(l)
    for elt in lx:
        nb = count_range(l,elt-(pas/2),elt+(pas/2))
        if long != 0:
            pourcentage = (nb*100)/long
            ly.append(pourcentage)
        else:
            ly.append(0)
    else:
        return(ly)
    
def nb_occur_dixieme(l,lx):
    ly=[]
    for elt in lx:
        nb=count_range(l,elt-0.05,elt+0.05)
        ly.append(nb)
    else:
        return(ly)


# Création d'une nouvelle liste adaptée aux paramètres

def nouvelle_liste(l,mini,maxi):
    liste = []
    for elt in l:
        if elt >= mini and elt <= maxi:
            liste.append(elt)
    else:
        return(liste)


# Fonctions pour les tracés des graphiques

def courbe(l,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly = nb_occurence(l,lx,pas)
    plt.figure('courbe')
    plt.plot(lx,ly)
    plt.xlabel('distances')
    plt.ylabel('nombre de points')


def courbelisse(l,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly = nb_occurence(l,lx,pas)
    plt.figure('courbe lisse')
    bspl = splrep(lx,ly,s=0.8)
    bspl_y = splev(lx,bspl)
    plt.plot(lx,ly)
    plt.plot(lx,bspl_y)
    plt.xlabel('distances')
    plt.ylabel('nombre de points')

def courbedouble(l1,l2,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly1 = nb_occurence(l1,lx,pas)
    ly2 = nb_occurence(l2,lx,pas)
    plt.figure('courbe')
    plt.plot(lx,ly1,color='blue')
    plt.plot(lx,ly2,color='red')
    plt.xlabel('distances')
    plt.ylabel('pourcentage de points')
    plt.legend(labels=['fichier 1','fichier 2'])


def courbelissedouble(l1,l2,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly1 = nb_occurence(l1,lx,pas)
    ly2 = nb_occurence(l2,lx,pas)
    plt.figure('courbe lisse')
    bspl1 = splrep(lx,ly1,s=0.8)
    bspl_y1 = splev(lx,bspl1)
    plt.plot(lx,bspl_y1)
    bspl2 = splrep(lx,ly2,s=0.8)
    bspl_y2 = splev(lx,bspl2)
    plt.plot(lx,bspl_y2)
    plt.xlabel('distances')
    plt.ylabel('pourcentage de points')
    plt.legend(labels=['fichier 1','fichier 2'])

def nuage_points(l,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly = nb_occurence(l,lx,pas)
    plt.figure('nuage de points')
    plt.scatter(lx,ly,s=5)
    plt.xlabel('distances')
    plt.ylabel('nombre de points')

def nuagedouble(l1,l2,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly1 = nb_occurence(l1,lx,pas)
    ly2 = nb_occurence(l2,lx,pas)
    plt.figure('courbe')
    plt.scatter(lx,ly1,color='blue',s=5)
    plt.scatter(lx,ly2,color='red',s=5)
    plt.xlabel('distances')
    plt.ylabel('pourcentage de points')
    plt.legend(labels=['fichier 1','fichier 2'])

def histogramme(l,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly = nb_occurence(l,lx,pas)
    plt.figure('histogramme')
    plt.bar(lx,ly,pas,color='yellow',edgecolor='blue')
    plt.xlabel('distances')
    plt.ylabel('pourcentage de points')

def histodouble(l1,l2,mini,maxi,pas):
    lx = gener_liste(mini,maxi,pas)
    ly1 = nb_occurence(l1,lx,pas)
    ly2 = nb_occurence(l2,lx,pas)
    plt.figure('histogramme')
    plt.bar(lx,ly1,pas,color='blue')
    plt.bar(lx,ly2,pas,color='red')
    plt.xlabel('distances')
    plt.ylabel('pourcentage de points')
    plt.legend(labels=['fichier 1','fichier 2'])
    

def courberepartition(l):
    l.sort()
    lx = list(range(0,len(l)))
    plt.figure('courbe de repartition')
    plt.plot(lx,l)
    plt.xlabel('points')
    plt.ylabel('distance')

def courberepdouble(l1,l2):
    l1.sort()
    l2.sort()
    lx1 = list(range(0,len(l1)))
    lx2 = list(range(0,len(l2)))
    plt.figure('courbe de repartition 1')
    plt.plot(lx1,l1)
    plt.xlabel('points')
    plt.ylabel('distance')
    plt.figure('courbe de repartition 2')
    plt.plot(lx2,l2)
    plt.xlabel('points')
    plt.ylabel('distance')
              
    
