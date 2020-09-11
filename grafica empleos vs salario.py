import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt
import operator

def main(args):        
    labels=['Negociable',"0USD a 500USD",'500USD a 1000USD','1000USD a 1500USD','1500USD a 2000USD',' Mayor a 2000USD']
    entero=0
    c=0
    n=0
    y=[]
    for i in labels:
        y.append(0)    
    client = MongoClient()    
    salarios=[] 
    collection = client['analisismercadolaboral']['porfinempleo'].find({})
    #keyword=["ciberseguridad","ciber seguridad","ciber-seguridad","hacking","ethical hacker","seguridad en redes","informática","informatica"]
    #keyword=["desarrollador","desarrollo de software","desarrollo","software","programacion","programación","informática","informatica"]
    keyword=["energias","ambiente","renovable","ambiental","renovables","energía"]  
    
    for i in collection:
        var=i['salario']
        por=var.split()
        try:
            if por[0]=="NEGOCIABLE":
                y[0]=y[0]+1
            else:
                entero=int(por[0])
                salarios.append(entero)
        except:
            print("error")

    for j in salarios:
        if j<500:
            y[1]=y[1]+1
        elif j<1000:
            y[2]=y[2]+1
        elif j<1500:
            y[3]=y[3]+1
        elif j<2000:
            y[4]=y[4]+1
        else:
            y[5]=y[5]+1

    x=range(len(labels))
    fig = plt.figure(u'Analisis Mercado Laboral')
    ax = fig.add_subplot()
    plt.title("Empleos vs Salario") 
    plt.xlabel("Empleos") 
    plt.ylabel("Salario")
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

