import datetime
import argparse
import json

def main(args):
    data={}
    data['empleos'] = []
    with open('data_porfinempleo_original.json',encoding='utf-8') as file:
            informacion = json.load(file)    
    c=0    
    for i in informacion.values():        
        #print(i.get('date_collected'))   
        c=c+1        
        if i != {}:
            i['jornada'] = i.pop('contrato')
            i['area']=i.pop('industria')
            data['empleos'].append(i)      
        if c==21832:
            break

    with open('data_porfinempleo_clean_mongo.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Collects info from jobs portals.''')
    
    argparser.add_argument('-f',
        help='file with URLS')
    args = argparser.parse_args()
    main(args)

