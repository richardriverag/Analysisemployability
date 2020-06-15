import datetime
import argparse
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
            'cargo': e['tituloAviso'],
            'jornada': e['tipoPuesto'],
            'salario': e['salario'],
            'area': [e['areaSolicitante'],e['areaPortal']],
            'empresa': e['empresa'],
            'descripcion': e['descripcion']})

            
    with open('data_multitrabajos_cleanASDASD.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

