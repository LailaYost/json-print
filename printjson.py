import os, json
import pandas as pd
num = 2

while num <= 33:
# this finds our json files
	path_to_json = 'C:/Users/N276928/Desktop/IRT Validation/%d' %(num)
	json_file = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
	print(json_file)

	for item in json_file:
	    new_file = (''.join(item))
	    print(new_file)

	filename = "C:/Users/N276928/Desktop/IRT Validation/%d/%s" %(num, new_file)
	with open(filename) as f:
		data = json.load(f)
		print(data)

	num = num + 1
	if num == 17:
		num = 18 
 
