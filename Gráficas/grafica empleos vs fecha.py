import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt

def main(args):    
    jornadas=[]
    c=0
    client = MongoClient()      
    collection = client['analisismercadolaboral']['empleos'].find({})
    for i in collection:
        var=i['publicado']
        var=var[0:4]
        
        if var not in jornadas:
            jornadas.append(var)
    print(jornadas)
    print(len(jornadas))
            
    y=[]
    for h in jornadas:
        y.append(0)
    collection = client['analisismercadolaboral']['empleos'].find({})  
    for i in collection:
        jornada=i['publicado']
        jornada=jornada[0:4]
        if jornada in jornadas:
            n=jornadas.index(jornada)
            y[n]=y[n]+1    

        
    x=range(len(jornadas))
    fig = plt.figure(u'Analisis Mercado Laboral')
    ax = fig.add_subplot(111)
    plt.title("Empleos vs Años") 
    plt.xlabel("Empleos") 
    plt.ylabel("Año")
    ax.set_yticks(x)
    ax.set_yticklabels(jornadas)
    ax.barh(x,y) 
    plt.show()
    
if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

