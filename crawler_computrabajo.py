import time
import argparse
import sys
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main(args):
    data = {}
    data['empleos'] = []
     
    #fecha=time.strftime("%d/%m/%y"))
    
    options = Options()
    options.add_argument('--headless')    
    driver = webdriver.Chrome('conf/chromedriver', chrome_options=options)    

    with open('urls_computrabajo_informatica.json') as file:
        informacion = json.load(file)

    for e in informacion['informatica y telecomunicaciones']:        
        print(e['url'])
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
            
            elem=driver.find_elements_by_xpath('//section[contains(@class,"box") and contains(@class, "box_r")]//ul//li//p')     
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
            
            
            #Se agrega el empleo a 'empleos'
            data['empleos'].append({        
                'ciudad': temporal2[1],
                'publicado': publicado,        
                'cargo': temporal2[0],
                'contrato': temporal2[2],
                'salario': temporal2[4]})        
            
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
