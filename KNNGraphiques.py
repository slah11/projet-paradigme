from PyQt5.uic import loadUi as l
from PyQt5.QtWidgets import QApplication as QA
from math import *
import pandas as pd
import matplotlib.pyplot as plt
from numpy import*
import seaborn as sns
df = pd.read_csv("dataset.csv")

def Classerdataset():
   malin = df['diagnosis'] == 'M'
   benin = df['diagnosis'] == 'B'
   

   #sns.jointplot(x="perimeter_worst", y="area_worst", data= df, kind='kde')
   #sns.kdeplot(x=df.perimeter_worst, y=df.area_worst,  fill=True)
   #sns.kdeplot(x=df['perimeter_worst'], y=df['area_worst'], fill=True)
   #sns.kdeplot(x=df[malin]['perimeter_worst'], y=df[malin]['area_worst'], cmap="Reds",  fill=True, alpha=0.3, thresh=False)
   #sns.kdeplot(x=df[benin]['perimeter_worst'], y=df[benin]['area_worst'], cmap="Greens",fill=True, alpha=0.3, thresh=False)
   #fig = sns.FacetGrid(data=df, hue="diagnosis", aspect=3, palette="Set2") # aspect=3 permet d'allonger le graphique
   #fig.map(sns.kdeplot, "perimeter_worst", fill=True)
   #fig.add_legend()
   #sns.lmplot(x="radius_mean", y="texture_mean", data=df, fit_reg=False, hue='diagnosis')
   sns.lmplot(x="radius_mean", y="texture_mean", data=df, fit_reg=False, hue='diagnosis')
   plt.show()
   #plt.figure(figsize=(12,12))
def Placercible():
   dfM=df[df['diagnosis'] == 'M']
   dfB=df[df['diagnosis'] == 'B']
   # Données de type 1

   Malin1=dfM['radius_mean']
   Malin2=dfM['texture_mean']
   print(Malin1)
   print(Malin2)
   # Données de type 2
   Benin1=dfB['radius_mean']
   Benin2=dfB['texture_mean']
   #print(Benin1)
   #print(Benin2)

   plt.axis([0,15, 0, 50]) # Attention [x1,x2,y1,y2]
   plt.axis('equal')
   plt.xlabel('radius_mean')
   plt.ylabel('texture_mean')
   plt.title('Classification KNN')
   plt.grid()
   plt.scatter(Malin1,Malin2, label='Malin')
   plt.scatter(Benin1,Benin2, label='Benin')

   #plt.scatter(7,28.4, label='cible')
   x= float(T.l1.text())
   y= float(T.l2.text())
   plt.scatter(x,y, label='cible')
   plt.legend()

   table =[["",0,0]]
   n=Malin1.count()
   m=Benin1.count()

   for i in range(n):
    table.append(['M',Malin1.iloc[i],Malin2.iloc[i]])
   for j in range(n,n+m):
    table.append(['B',Benin1.iloc[j-n],Benin2.iloc[j-n]]) 
   #cible = [7,28.4]
    
   cible = [x,y]
   k=int(T.l3.text())
   res=k_plus_proches_voisins(table,cible,k)
   msg="La liste des "+str(k)+" plus proches voisins de la cible :\n"+res
   T.rs.setText(msg)
   #6print("La liste des ",k," plus proches voisins de la cible : ",k_plus_proches_voisins(table,cible,k))
   plt.show()
def k_plus_proches_voisins(table, cible, k):
    """Revoie la liste des k plus proches voisins de la cible"""

    def distance_cible(donnee):
        """ renvoie la distance entre la donnée et la cible, on choisit la distance de Manhattan"""
        distance = abs(donnee[1] - cible[0]) + abs(donnee[2] - cible[1])
        return distance

    table_triee = sorted(table, key=distance_cible)

    proches_voisins = []

    for i in range(k):
        proches_voisins.append(str(table_triee[i]))

    return ''.join(proches_voisins)

def Sortir():
    T.close()
def effacer():
    T.l1.clear()
    T.l2.clear()
    T.l3.clear()
    T.rs.clear()
app=QA([])
T=l("Knn.ui")
T.show()
#en clic sur bouton
T.bt1.clicked.connect(Classerdataset)
T.bt2.clicked.connect(Placercible)
T.bt3.clicked.connect(effacer)
T.bt4.clicked.connect(Sortir)
#Execution
app.exec_()