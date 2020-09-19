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
    #driver = webdriver.Chrome('conf/chromedriver')  
    
    #Variable global para ser usada en una funcion
    global data
    global contador
    contador=0
    
    data={}
    data['todos'] = []
    
    for i in range(129,1,-1):        
        driver.get('https://www.multitrabajos.com/empleos-ecuador-pagina-'+str(i)+'.html?recientes=true')

        elem = driver.find_elements_by_css_selector("div.col-sm-9.col-md-10.col-xs-9.wrapper")            
        url=''
        
        for i in elem:        
            url=i.find_element_by_css_selector('a').get_attribute('href')        
            print url
            data['todos'].append({        
            'url': url})
            contador=contador+1
            print contador

    print contador    
                
    driver.quit()
    #Se exporta a un json la variable data
    with open('urls_multitrabajos.json', 'w') as file:
        json.dump(data, file, indent=4)
    

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
