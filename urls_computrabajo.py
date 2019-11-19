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
        
    data={}
    data['informatica y telecomunicaciones'] = []

    for i in range(1,10):        
        driver.get('https://www.computrabajo.com.ec/empleos-de-informatica-y-telecom?p='+str(i))    
        elem = driver.find_elements_by_class_name("js-o-link")
        url=''
        for i in elem:
            print i.text
            url=i.get_attribute('href')
            print url
            data['informatica y telecomunicaciones'].append({        
            'url': url})       

    driver.quit()
    
    #Se exporta a un json la variable data
    with open('urls_computrabajo_informatica.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
