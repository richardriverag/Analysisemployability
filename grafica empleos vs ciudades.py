import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt

def main(args):    
    ciudades=['Guayaquil','Quito','Cuenca','Santo','Machala','Durán','Manta','Portoviejo','Loja','Ambato','Esmeraldas','Quevedo','Riobamba','Milagro','Ibarra','Babahoyo','Sangolquí','Daule','Latacunga','Tulcán','Chone','Pasaje','Huaquillas','Montecristi', 'Samborondón','Otavalo','Cayambe','Rumiñahui']
    labels=['Guayaquil','Quito','Cuenca','Santo Domingo','Machala','Durán','Manta','Portoviejo','Loja','Ambato','Esmeraldas','Quevedo','Riobamba','Milagro','Ibarra','Babahoyo','Sangolquí','Daule','Latacunga','Tulcán','Chone','Pasaje','Huaquillas','Montecristi', 'Samborondón','Otavalo','Cayambe','Rumiñahui','Otros']
    x=range(len(labels))
    
    y=[]
    for i in labels:
        y.append(0)    
    client = MongoClient()    
      
    collection = client['analisismercadolaboral']['empleos'].find({})
    for i in collection:

        var=i['ciudad']        
        h=var.capitalize()
        h=h.split()
        #print(h[0])
        h[0]=h[0].rstrip(",")
        c=0
        logico=0
        if h[0] in ciudades:
            n=ciudades.index(h[0])
            y[n]=y[n]+1
        else:
            y[-1]=y[-1]+1
            
    print(y)
    print(ciudades)

    fig = plt.figure(u'Analisis Mercado Laboral')
    ax = fig.add_subplot(111)
    plt.title("Empleos vs Ciudades") 
    plt.xlabel("Empleos") 
    plt.ylabel("Ciudades")
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.barh(x,y) 
    plt.show()     


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

