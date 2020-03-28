import time
import datetime
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

    data = {}
    data['empleos'] = []

    with open('urls_computrabajo.json') as file:
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
            publicado=temporal1[-1]
                    
            elem=driver.find_element_by_class_name("detalle_textoempresa")
            empresa=elem.find_element_by_tag_name("h2")         
            descripcion=driver.find_element_by_xpath('//*[contains(@class,"bWord")]//ul//li')
            elem=driver.find_elements_by_xpath('//section[contains(@class,"box") and contains(@class, "box_r")]//ul//li//p')    
            
            temporal2=[]        
            for i in elem:                    
                print i.text                  
                temporal2.append(i.text)

            if (len(temporal2)==6):
                data['empleos'].append({
                        'date_collected': datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f"),
                        'ciudad': temporal2[2],
                        'publicado': publicado,        
                        'cargo': temporal2[0],
                        'jornada': temporal2[3],
                        'contrato': temporal2[4],
                        'salario': temporal2[5],
                        'descripcion': descripcion.text,                
                        'empresa': empresa.text               
                        })
            else:
                data['empleos'].append({
                        'date_collected': datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f"),
                        'ciudad': temporal2[1],
                        'publicado': publicado,        
                        'cargo': temporal2[0],
                        'jornada': temporal2[2],
                        'contrato': temporal2[3],
                        'salario': temporal2[4],
                        'descripcion': descripcion.text,                
                        'empresa': empresa.text                
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
