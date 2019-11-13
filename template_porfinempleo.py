import time
import argparse
import sys
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main(args):
    options = Options()
    options.add_argument('--headless')    
    driver = webdriver.Chrome('conf/chromedriver', chrome_options=options)
    
    #Variable data que va a almacenar la informacion
    data = {}
    data['empleos'] = []

    """Bucle que toma los datos de los anuncios desde el primer anuncio que es del 2012 con numero 30372
    hasta el ultimo anuncio de este anio con numero 62812"""
    for i in range(30372,62813):        
        driver.get('https://www.porfinempleo.com/page/anuncio.php?cod='+str(i))        
        elem = driver.find_elements_by_class_name("anuncio-container")
        #Variable temporal
        temporal=[]
        #Bucle que recorre los elementos anuncio-container
        for i in elem:
            print i.text
            temporal.append(i.text)
        #Se agrega el empleo a 'empleos'
            
            """Formato estandar que tendran las tres paginas, la interseccion de datos de las 3 son:
            ciudad, fecha publicacion, cargo, contrato o jornada y salario"""
            
        data['empleos'].append({        
        'ciudad': temporal[1],
        'publicado': temporal[3],        
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
