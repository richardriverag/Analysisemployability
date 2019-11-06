import time
import argparse
import sys
import os
import json
from selenium import webdriver
from pyvirtualdisplay import Display


def main(args):
    #display to execute in a server without gui(commented for test)
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome('conf/chromedriver')
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
    
    display.stop()

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
