import csv
import sys
import json

with open(sys.argv[1]) as test:
	data = test.read();

pragam_json = json.loads(data)

for item in pragam_json:
	if pragam_json[item]['pragma type'] != 'NULL':
		print("pragam :" + pragam_json[item]['pragma type'])
		for item1 in pragam_json[item]:
			if item1 != 'body' and type(pragam_json[item][item1]) == list and pragam_json[item][item1] != []:
				print("clause :" + item1)
