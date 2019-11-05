import time
import argparse
import sys
import os
import json
from selenium import webdriver

def main(args):    
    driver = webdriver.Chrome('conf/chromedriver.exe')
    #Variable data que va a almacenar la informacion
    data = {}
    data['empleos'] = []

    #Bucle que toma los datos de 2 anuncios con codigo 62695 y 62696
    for i in range(62695,62697):        
        driver.get('https://www.porfinempleo.com/page/anuncio.php?cod='+str(i))        
        elem = driver.find_elements_by_class_name("anuncio-container")
        #Variable temporal que almacena el codigo, ciudad, industria,etc
        temporal=[]
        #Bucle que recorre los elementos anuncio-container
        for i in elem:
            print i.text
            temporal.append(i.text)
        #Se agrega el empleo a 'empleos'
        data['empleos'].append({
        'codigo': temporal[0],
        'ciudad': temporal[1],
        'industria': temporal[2],
        'publicado': temporal[3],
        'vacantes': temporal[4],
        'cargo': temporal[5],
        'contrato': temporal[6],
        'salario': temporal[7]})
        
    driver.quit()
    print(data)
    #Se exporta a un json la variable data
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4) 


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
