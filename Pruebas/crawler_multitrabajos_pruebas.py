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
    #options.add_argument('log-level=3')
    driver = webdriver.Chrome('conf/chromedriver', chrome_options=options)

    data = {}
    data['empleos'] = []

    with open('urls_multitrabajos_pruebas.json') as file:
        informacion = json.load(file)
    c=0    
    
    for e in informacion['todos']:        
        print(e['url'])        

        try:
            driver.get(e['url'])    
            tituloAviso = driver.find_element_by_class_name("aviso_title")
            areaPortal=driver.find_elements_by_class_name("breadcrumb-item")
            empresa=driver.find_element_by_class_name("aviso_company")            
            descripcionAviso = driver.find_element_by_class_name("aviso_description")
            
            """print (tituloAviso.text)
            print (descripcionAviso.text)"""
            print (datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f"))
        
            elem = driver.find_elements_by_css_selector("div.col-sm-12.col-md-6.col-lg-10.spec_def")
            temporal=[]
            for i in elem:        
                print (i.text)
                temporal.append(i.text)

            """for i in temporal:
                print i"""
                            
            #Se agrega el empleo a 'empleos'           
            data['empleos'].append({
            'date_collected': datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f"),
            'ciudad': temporal[0],
            'publicado': temporal[1],        
            'tituloAviso': tituloAviso.text,
            'tipoPuesto': temporal[3],
            'salario': temporal[2],
            'areaSolicitante': temporal[4],
            'areaPortal': areaPortal[1].text,
            'empresa': empresa.text,
            'descripcion': descripcionAviso.text})
        except:
            continue
        
    driver.quit()
    
    #Se exporta a un json
    with open('data_multitrabajos_prueba.json', 'w') as file:
        json.dump(data, file, indent=4) 


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

