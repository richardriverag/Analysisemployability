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
        var=i['jornada'].capitalize()
        if var not in jornadas:
            jornadas.append(var)

    y=[]
    for h in jornadas:
        y.append(0)
    collection = client['analisismercadolaboral']['empleos'].find({})  
    for i in collection:
        jornada=i['jornada'].capitalize()        
        if jornada in jornadas:
            n=jornadas.index(jornada)
            y[n]=y[n]+1
            
    y[0]=y[0]+y[16]
    y[2]=y[2]+y[18]
    y[14]=y[14]+y[19]
    y[5]=y[5]+y[20]
    y[23]=y[23]+y[24]
    jornadas.pop(16)
    jornadas.pop(17)
    jornadas.pop(17)
    jornadas.pop(17)
    jornadas.pop(20)
    jornadas.pop(8)
    y.pop(16)
    y.pop(17)
    y.pop(17)
    y.pop(17)
    y.pop(20)
    y.pop(8)

    for i in range(0,3):
        jornadas.pop()
        y.pop()        
    print(y)
    print(len(jornadas))
    
    for i in jornadas:        
        print(i+str(jornadas.index(i)))
        
    x=range(len(jornadas))
    fig = plt.figure(u'Analisis Mercado Laboral')
    ax = fig.add_subplot(111)
    plt.title("Empleos vs Jornadas") 
    plt.xlabel("Empleos") 
    plt.ylabel("Jornadas")
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

