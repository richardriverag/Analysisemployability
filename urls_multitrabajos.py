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
    #driver = webdriver.Chrome('conf/chromedriver', chrome_options=options)
    driver = webdriver.Chrome('conf/chromedriver')  
    
    #Variable global para ser usada en una funcion
    global data
    data={}
    data['tecnologia sistemas y telecomunicaciones'] = []

    driver.get('https://www.multitrabajos.com/empleos-area-tecnologia-sistemas-y-telecomunicaciones.html')
    #driver.get('https://www.multitrabajos.com/empleos-area-tecnologia-sistemas-y-telecomunicaciones-pagina-7.html')

    #Variable la flecha para cambiar a la siguiente pagina
    siguiente = driver.find_elements_by_class_name('next')
    largoinicial=len(siguiente[1].get_attribute('href'))
    largo=len(siguiente[1].get_attribute('href'))
    
    #Bucle while para recorrer automaticamente todas las paginas sin necesidad de saber el numero de paginas
    while(largoinicial==largo):    
        #print(largo)
        #print siguiente[1].get_attribute('href')
        recoleccionLinks(driver)
        siguiente[1].click()
        time.sleep(1)
        siguiente = driver.find_elements_by_class_name('next')
        largo=len(siguiente[1].get_attribute('href'))
        
    #print('FINAL')            
    driver.quit()
    #Se exporta a un json la variable data
    with open('urls_multitrabajos_sistemas.json', 'w') as file:
        json.dump(data, file, indent=4) 


def recoleccionLinks(driversel):
    elem = driversel.find_elements_by_css_selector("div.col-sm-9.col-md-10.col-xs-9.wrapper")        
    #c=0
    url=''
    for i in elem:        
        #c=c+1        
        #print c
        url=i.find_element_by_css_selector('a').get_attribute('href')
        print url
        data['tecnologia sistemas y telecomunicaciones'].append({        
        'url': url})        

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
