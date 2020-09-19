import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt
import operator

def main(args):    
    areas=[]
    c=0
    client = MongoClient()   
    # client['analisismercadolaboral']['empleos'].find({}).count()    
    collection = client['analisismercadolaboral']['empleos'].find({})
    
    #Creacion de arreglo de areas
    for i in collection:
        
        #Manejo de excepción para Computrabajo que no tiene 'area'
        try:
            var=i['area']
            #Condición para no tomar las áreas de Multitrabajos
            if len(var)!=2:
                if var not in areas:
                    areas.append(var)
        except:
            c=0
            
    #Creacion de arreglo para contar la repeticion de areas    
    y=[]
    conta=0
    for i in areas:
        y.append(0)
    x=range(len(areas))
    collection = client['analisismercadolaboral']['empleos'].find({})
    #keyword=["ciberseguridad","ciber seguridad","ciber-seguridad","hacking","ethical hacker","seguridad en redes","informática","informatica"]
    #keyword=["desarrollador","desarrollo de software","desarrollo","software","programacion","programación","informática","informatica"]
    keyword=["energias","ambiente","renovable","ambiental","renovables","energía"]
    for i in collection:
        descripcion=i['descripcion'].lower()

        for j in keyword:
            if j in descripcion:
        
                try:
                    area=i['area']            
                    if len(area)!=2:                
                        if area in areas:
                            n=areas.index(area)
                            y[n]=y[n]+1
                except:
                    c=0
                break
    print(conta)
    #Creacion de diccionario para ordenamiento con area y numero de empleos por area       
    empleosareas={} 
    for i in range(len(areas)):
        empleosareas[areas[i]]=y[i]
    empleosareas_ordenado=sorted(empleosareas.items(), key=operator.itemgetter(1), reverse=True)

    #Paso de diccionario a arreglos para grafica de barras
    subareas=[]
    suby=[]    
    for i in empleosareas_ordenado:
        suby.append(i[1])
        subareas.append(i[0]+"("+str(i[1])+") ")        

    fig = plt.figure(u'Analisis Mercado Laboral')
    ax = fig.add_subplot()
    plt.title("Empleos vs Areas") 
    plt.xlabel("Empleos") 
    plt.ylabel("Areas")
    ax.set_yticks(x[0:45])
    ax.set_yticklabels(subareas[0:45])
    ax.barh(x[0:45],suby[0:45])
    plt.show()

    #Creacion de arreglos para grafica de pastel
    pastelp=[]    
    pastelp.append(suby[0:16])
    pastelp[0].append(sum(suby[16:len(suby)]))
    pasteln=[]
    pasteln.append(subareas[0:16])
    pasteln[0].append("Otros")
    
    porcentajes = pastelp[0][0:17]
    nombres = pasteln[0][0:17]   
    plt.pie(porcentajes, labels=nombres, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

