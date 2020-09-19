import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt

def main(args):    
    empresas=[]
    c=0
    d=0
    client = MongoClient()      
    collection = client['analisismercadolaboral']['empleos'].find({})
    for i in collection:
        try:
            var=i['empresa'].capitalize()
            d=d+1
            if var not in empresas:
                empresas.append(var)                
        except:
            c=c+1
    print(d)
    print(len(empresas))
    print(c)
    e=c+d
    print(e)

    #Dato tomado del INEC del año 2018
    totalempresaspais=899208
    emps = [len(empresas),totalempresaspais]
    nombres = ["Empresas Multitrabajos y Computrabajo","Total de empresas en el país"]
    desfase = (0.3,0.3)
    plt.pie(emps, labels=nombres, autopct="%0.1f %%",explode=desfase)
    plt.axis("equal")
    plt.show()
"""
    y=[]
    for h in jornadas:
        y.append(0)
    collection = client['analisismercadolaboral']['empleos'].find({})  
    for i in collection:
        jornada=i['jornada'].capitalize()        
        if jornada in jornadas:
            n=jornadas.index(jornada)
            y[n]=y[n]+1

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
    plt.show()"""
    
if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

