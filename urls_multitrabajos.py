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
    data['todos'] = []
    
    driver.get('https://www.multitrabajos.com/empleos-area-tecnologia-sistemas-y-telecomunicaciones.html')
    #driver.get('https://www.multitrabajos.com/empleos-ecuador.html?recientes=true')
    #driver.get('https://www.multitrabajos.com/empleos-area-tecnologia-sistemas-y-telecomunicaciones-pagina-7.html')

    #Variable de la flecha para cambiar a la siguiente pagina
    siguiente = driver.find_elements_by_class_name('next')
    largoinicial=len(siguiente[1].get_attribute('href'))    
    largo=len(siguiente[1].get_attribute('href'))    
    
    #Bucle while para recorrer automaticamente todas las paginas sin necesidad de saber el numero de paginas
    while(largoinicial==largo):           
        recoleccionLinks(driver)       
        driver.get(siguiente[1].get_attribute('href'))
        siguiente = driver.find_elements_by_class_name('next')
        largo=len(siguiente[1].get_attribute('href'))        
                
    driver.quit()
    #Se exporta a un json la variable data
    with open('urlsnuevas_multitrabajos.json', 'w') as file:
        json.dump(data, file, indent=4)


def recoleccionLinks(driversel):        
    elem = driversel.find_elements_by_css_selector("div.col-sm-9.col-md-10.col-xs-9.wrapper")            
    url=''
    for i in elem:        
        url=i.find_element_by_css_selector('a').get_attribute('href')        
        print url
        data['todos'].append({        
        'url': url})
    

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
