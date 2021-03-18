import matplotlib.pyplot as plt

def barplot(listSouche):
    fig = plt.figure()
    plt.bar(range(3), listSouche)
    fig.savefig('barplot.png', dpi=fig.dpi)

liste = [12.5,3.5,6.8]
barplot(liste)
