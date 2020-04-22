import datetime
import argparse
import sys
import os
import json

def main(args):
    data={}
    data['empleos'] = []
    with open('data_computrabajo.json',encoding='utf8') as file:
            informacion = json.load(file)    
    c=0
    anio='2020'
    mes=''
    dia=''
    for e in informacion['empleos']:                
        fecha=e['publicado']
        fechadividida=fecha.split()        
        for i in range(0,2):
            try:                
                int(fechadividida[i])
                dia=fechadividida[i]                                
            except:                
                m=fechadividida[i]                

        if m=='enero':
            mes='01'
        elif m=='febrero':
            mes='02'
        elif m=='marzo':
            mes='03'
        else:
            mes='03'
            dia='27'

        
        data['empleos'].append({
            'date_collected': e['date_collected'],
            'ciudad': e['ciudad'],
            'publicado': anio+'-'+mes+'-'+dia,
            'cargo': e['cargo'],
            'jornada': e['jornada'],
            'contrato': e['contrato'],
            'salario': e['salario'],
            'descripcion': e['descripcion'],                
            'empresa': e['empresa']                
            })
            
    with open('data_computrabajo_clean.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

