import time
import argparse
import sys
import os
import json
from selenium import webdriver



def main(args):
    driver = webdriver.Chrome('conf/chromedriver.exe')
    driver.get('http://www.google.com/')
    # Let the user actually see something!
    time.sleep(5)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
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