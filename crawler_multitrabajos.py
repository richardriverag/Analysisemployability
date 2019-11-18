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

    with open('urls_multitrabajos_sistemas.json') as file:
        informacion = json.load(file)
    c=0
    for e in informacion['tecnologia sistemas y telecomunicaciones']:
        c=c+1
        print(c)
        print(e['url'])    
    
    for e in informacion['tecnologia sistemas y telecomunicaciones']:
        
        print(e['url'])
        driver.get(e['url'])    
        cargo = driver.find_element_by_class_name("aviso_title")
        print cargo.text
    
        elem = driver.find_elements_by_css_selector("div.col-sm-12.col-md-6.col-lg-10.spec_def")
        temporal=[]
        for i in elem:        
            print i.text
            temporal.append(i.text)
                
        #Se agrega el empleo a 'empleos'
           
        data['empleos'].append({        
        'ciudad': temporal[0],
        'publicado': temporal[1],        
        'cargo': cargo.text,
        'contrato': temporal[3],
        'salario': temporal[2]})
        
        
    driver.quit()
    
    #Se exporta a un json
    with open('empleos_multitrabajos.json', 'w') as file:
        json.dump(data, file, indent=4) 


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
