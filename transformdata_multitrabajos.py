import datetime
import argparse
import sys
import os
import json

def main(args):
    data={}
    data['empleos'] = []
    with open('data_multitrabajos.json',encoding='utf8') as file:
            informacion = json.load(file)    
    
    for e in informacion['empleos']:  
        fecha=e['publicado']
        fechadividida=fecha.split()        
        for i in fechadividida:
            try:                
                int(i)
                dias=int(i)                
            except:
                dia=0
                
        f=e['date_collected']
        nuevaFecha=datetime.datetime.strptime(f,'%d-%b-%Y %H:%M:%S.%f')-datetime.timedelta(days=dias)

        data['empleos'].append({
            'date_collected': e['date_collected'],
            'ciudad': e['ciudad'],
            'publicado': str(nuevaFecha),        
            'tituloAviso': e['tituloAviso'],
            'tipoPuesto': e['tipoPuesto'],
            'salario': e['salario'],
            'areaSolicitante': e['areaSolicitante'],
            'areaPortal': e['areaPortal'],
            'empresa': e['empresa'],
            'descripcion': e['descripcion']})

            
    with open('data_multitrabajos_clean.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

