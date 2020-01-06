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
    options.add_argument('log-level=3')
    driver = webdriver.Chrome('conf/chromedriver', chrome_options=options)

    #Variable data que va a almacenar la informacion
    data = {}
    #data['empleos'] = []

    """Bucle que toma los datos de los anuncios desde el primer anuncio que es del 2012 con numero 30372
    hasta el ultimo anuncio de este anio con numero 62812"""
    for i in range(30372,63200): # 62813
        try:
            data[i] = {}
            driver.get('https://www.porfinempleo.com/page/anuncio.php?cod='+str(i))
            elem = driver.find_elements_by_class_name("anuncio-container")
            #saltar anuncios vacios
            if not elem:
                print("anuncio {} vacio".format(i))
                continue
            #Variable temporal para almacenar la información de cada anuncio
            anuncio=[]
            #Bucle que recorre los elementos anuncio-container
            for e in elem:
                #print (e.text)
                anuncio.append(e.text)
            #Se agrega el empleo a 'empleos'

                """Formato estandar que tendran las tres paginas, la interseccion de datos de las 3 son:
                ciudad, fecha publicacion, cargo, contrato o jornada y salario"""
            elem = driver.find_elements_by_class_name("comment-content")
            #Variable temporal para almacenar los detalles de cada anuncio
            detalle = []
            #Bucle que recorre los elementos comment-content
            for e in elem:
                detalle.append(e.text)
            #print(anuncio)
            # data[i].append({
            # 'date_collected': datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f"),
            # 'codigo': anuncio[0],
            # 'ciudad': anuncio[1],
            # 'industria': anuncio[2],
            # 'publicado': anuncio[3],
            # 'vacantes': anuncio[4],
            # 'cargo': anuncio[5],
            # 'contrato': anuncio[6],
            # 'salario': anuncio[7],
            # 'descripcion': detalle[0],
            # 'beneficios':detalle[1]
            # })
            data[i]['date_collected']= datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")
            data[i]['codigo']= anuncio[0]
            data[i]['ciudad']= anuncio[1]
            data[i]['industria']= anuncio[2]
            data[i]['publicado']= anuncio[3]
            data[i]['vacantes']= anuncio[4]
            data[i]['cargo']= anuncio[5]
            data[i]['contrato']= anuncio[6]
            data[i]['salario']= anuncio[7]
            data[i]['descripcion']= detalle[0]
            data[i]['beneficios']=detalle[1]
            print("anuncio {} grabado exitosamente".format(i))
        except:
            continue
    driver.quit()
    #print(data)
    #Se exporta a un json la variable data
    with open('data_porfinempleo.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')

    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)
