import time
import datetime
import argparse
import sys
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main(args):
    #fecha=time.strftime("%d/%m/%y"))
    options = Options()
    options.add_argument('--headless')    
    driver = webdriver.Chrome('conf/chromedriver', chrome_options=options)

    data = {}
    data['empleos'] = []

    with open('urls_compu.json') as file:
        informacion = json.load(file)
    
    for e in informacion['todos']:        
        print(e['url'])

        try:
            driver.get(e['url'])
            elem=driver.find_elements_by_xpath("//header//span")

            temporal1=[] 
            for i in elem:                    
                temporal1.append(i.text)
            print(temporal1)        
            print('largo1')
            print(len(temporal1))
            
            if len(temporal1)!=10:
                publicado=temporal1[-1]           
                
                elem=driver.find_elements_by_xpath('//section[contains(@class,"box") and contains(@class, "box_r")]//ul// li//p')     
                temporal2=[]        
                for i in elem:                    
                    print i.text                    
                    temporal2.append(i.text)
                            
                try:
                    temporal2.remove('')
                except:
                    print('No existe elemento vacio en lista')
                    
                for i in range(1,5):            
                    print temporal2[i]
                print(temporal2)
                print('largo2')
                print(len(temporal2))
                descripcion = driver.find_element_by_class_name("cm-12 box_i bWord")
                print descripcion
                print (" d e  s  c r  i  p                   c  i  o  n ")
                for i in descripcion:
                    print i.text
                
                
                #Se agrega el empleo a 'empleos'
                data['empleos'].append({
                    'date_collected': datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f"),
                    'ciudad': temporal2[2],
                    'publicado': publicado,        
                    'cargo': temporal2[0],
                    'jornada': temporal2[3],
                    'contrato': temporal2[4],
                    'salario': temporal2[5],
                    'descripcion': temporal2[0],
                    'requerimientos': temporal2[2],
                    'empresa': temporal2[1]                
                    })
        except:
            continue
                
    #Se exporta a un json
    with open('empleos_computrabajo.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    driver.quit()
        
if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
