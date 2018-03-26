#count bases included

import os

csv_files = []
path = '/Users/sclohise/Desktop/SamLycett_Human_Flu/summary_files/'
dirs = os.listdir(path)
for fle in dirs:
	if '_for_agilent.csv' in fle:
		csv_files.append(fle)

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

total_characters = []
for infile in csv_files:
	with open(infile, 'r') as inF:
		for line in inF:
			if '>' not in line:
				line = line.strip()
				total_characters.append(line)
total = ((concatenate_list_data(total_characters)))

print len(total)

