import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt

def main(args):    
    jornadas=[]
    salario=[]
    c=0
    client = MongoClient()      
    collection = client['analisismercadolaboral']['empleos'].find({})
    for i in collection:
        var=i['salario'].capitalize()
        var=var.split()
        salario=var[0]
        if salario not in jornadas:
            try:
                jornadas.append(salario)
            except:
                c=c+1
    
    print(c)
    print(jornadas)
    print(len(jornadas))
    print(max(jornadas))
    print(min(jornadas))
    """
    y=[]
    for h in jornadas:
        y.append(0)
    collection = client['analisismercadolaboral']['empleos'].find({})  
    for i in collection:
        jornada=i['jornada'].capitalize()
        jornada=jornada.split()
        salario=var[0]
        if salario in jornadas:
            n=jornadas.index(salario)
            y[n]=y[n]+1

    print(y)
    print(len(y))


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

