import matplotlib.pyplot as plt

def barplot(listSouche,numSouche):
    fig = plt.figure()
    plt.bar(range(3), listSouche)
    plt.xticks(range(3), ['DO 6h','DO 24h','DO Production'])
    plt.title('DO souche '+str(numSouche))
    fig.savefig('barplot.png', dpi=fig.dpi)

liste = [12.5,3.5,6.8]
barplot(liste,12)
