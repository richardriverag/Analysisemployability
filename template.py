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
    #options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('conf/chromedriver', chrome_options=options)
    driver.get('http://www.google.com/')
    # Let the user actually see something!
    time.sleep(5)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('EPN ecuador')
    search_box.submit()
    time.sleep(3)
    elem = driver.find_element_by_link_text("Carreras")
    print elem
    print elem.text
    # Let the user actually see something!
    time.sleep(5)
    driver.quit()
    

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
