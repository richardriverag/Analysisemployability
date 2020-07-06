import datetime
import argparse
import json
import pymongo
from pymongo import MongoClient
import numpy as np 
from matplotlib import pyplot as plt

def main(args):    
    areas=[]
    c=0
    client = MongoClient()   
    #holo = client['analisismercadolaboral']['empleos'].find({}).count()    
    collection = client['analisismercadolaboral']['empleos'].find({})
    for i in collection:        
        try:
            var=i['area']
            if len(var)!=2:
                if var not in areas:
                    areas.append(var)
        except:
            c=0
            

    y=[]
    for i in areas:
        y.append(0)
    x=range(len(areas))
    collection = client['analisismercadolaboral']['empleos'].find({})
    for i in collection:        
        try:
            area=i['area']
            
            if len(area)!=2:                
                if area in areas:
                    n=areas.index(area)
                    y[n]=y[n]+1
        except:
            c=0
            

    print(y)
    subareas=[]
    suby=[]
    for i in areas:
        n=areas.index(i)
        if y[n]>=60:
            subareas.append(i)
            suby.append(y[n])
    print("AREAS NO TOMADAS EN CUENTA")
    for i in areas:
        if i not in subareas:
            print(i)

    x=range(len(subareas))
    print(len(areas))
    print(len(subareas))
    fig = plt.figure(u'Analisis Mercado Laboral')
    ax = fig.add_subplot(111)
    plt.title("Empleos vs Areas") 
    plt.xlabel("Empleos") 
    plt.ylabel("Areas")
    ax.set_yticks(x)
    ax.set_yticklabels(subareas)
    #plt.legend(labels)
   # plt.set_xticklabels(labels)
    #plt.plot(x,y)
    ax.barh(x,suby) 
    plt.show() 


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

