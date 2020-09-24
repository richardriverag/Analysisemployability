import time
import datetime
import argparse
import sys
import os
import json
import pymongo
import pprint

def main(args):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["employability"]
	mycol = mydb["data"]

	with open('{}'.format(args.file), 'r') as f:
		data_dict = json.load(f)
	mylist = []
	for e in data_dict.values():
		if e:
			mylist.append(e)
	#pprint.pprint(mylist)
	i = mycol.insert_many(mylist)
	print(len(i.inserted_ids))

if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='Crawler template',
        description='''Load data in mongodb''')

    argparser.add_argument('-f','--file',
		required= True,
        help='file with data')
    args = argparser.parse_args()
    main(args)
