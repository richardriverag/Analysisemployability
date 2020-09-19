import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt
import operator

def main(args):    
    ciudades=['Guayaquil','Quito','Cuenca','Santo','Machala','Durán','Manta','Portoviejo','Loja','Ambato','Esmeraldas','Quevedo','Riobamba','Milagro','Ibarra','Babahoyo','Sangolquí','Daule','Latacunga','Tulcán','Chone','Pasaje','Huaquillas','Montecristi', 'Samborondón','Otavalo','Cayambe','Rumiñahui']
    labels=['Guayaquil','Quito','Cuenca','Santo Domingo','Machala','Durán','Manta','Portoviejo','Loja','Ambato','Esmeraldas','Quevedo','Riobamba','Milagro','Ibarra','Babahoyo','Sangolquí','Daule','Latacunga','Tulcán','Chone','Pasaje','Huaquillas','Montecristi', 'Samborondón','Otavalo','Cayambe','Rumiñahui','Otros']
 
    y=[]
    for i in labels:
        y.append(0)    
    client = MongoClient()    
      
    collection = client['analisismercadolaboral']['empleos'].find({})
    #keyword=["ciberseguridad","ciber seguridad","ciber-seguridad","hacking","ethical hacker","seguridad en redes","informática","informatica"]
    keyword=["desarrollador","desarrollo de software","desarrollo","software","programacion","programación","informática","informatica"]
    #keyword=["energias","ambiente","renovable","ambiental","renovables","energía"]
    for i in collection:        
        var=i['ciudad']
        descripcion=i['descripcion'].lower()        
        h=var.capitalize()
        h=h.split()        
        h[0]=h[0].rstrip(",")
                
        for j in keyword:
            if j in descripcion:
                #print(i["date_collected"])
                if h[0] in ciudades:
                    n=ciudades.index(h[0])
                    y[n]=y[n]+1
                else:
                    y[-1]=y[-1]+1
                break
    
    #Creacion de diccionario para ordenamiento con area y numero de empleos por area       
    desordenado={} 
    for i in range(len(ciudades)):
        desordenado[ciudades[i]]=y[i]
    ordenado=sorted(desordenado.items(), key=operator.itemgetter(1), reverse=True)
    total=0
    for i in ordenado:        
        total=total+i[1]
    c=0
    sublabels=[]
    suby=[]
    for j in ordenado:
        if j[1]==0:
            break
        else:            
            sublabels.append(labels[c]+"("+str(j[1])+") "+str(round((j[1]/total)*100,2))+"% ")
            suby.append(j[1])
            c=c+1        
    x=range(len(sublabels))
    print(sublabels)

    fig = plt.figure(u'Analisis Mercado Laboral')
    ax = fig.add_subplot(111)
    plt.title("Empleos vs Ciudades") 
    plt.xlabel("Empleos") 
    plt.ylabel("Ciudades")
    ax.set_yticks(x)
    ax.set_yticklabels(sublabels)
    ax.barh(x,suby) 
    plt.show()

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

