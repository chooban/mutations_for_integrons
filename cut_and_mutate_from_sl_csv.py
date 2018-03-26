import os

bases = ['A', 'C', 'T', 'G']
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}


csv_files = []
path = '/Users/sclohise/Desktop/SamLycett_Human_Flu/summary_files/'
dirs = os.listdir(path)
for fle in dirs:
	if '.csv' in fle:
		csv_files.append(fle)

for infile in csv_files:
	outfile = '/Users/sclohise/Desktop/SamLycett_Human_Flu/summary_files/' + (infile.split('.'))[0] + '_for_agilent.csv'
	o = open(outfile, 'w')
	strain = (infile.split('sample'))[0]
	i = 0
	records = []

	infile = path + infile
	with open(infile, 'r') as inF:
		record = {}

		for line in inF:
			line = line.split(',')
			if 'Consensus' == line[0]:
				segments = []
				for l in line[1:]:
					if l.strip() is not '':
						segments.append(l.strip())
				record["segments"] = segments
			if 'Fract' == line[0]:
				fractions = []
				for l in line[1:]:
					if l.strip() is not '':
						fractions.append(float(l.strip()))
				record["fractions"] = fractions
			if 'a' == line[0]:
				a = []
				for l in line[1:]:
					if l.strip() is not '':
						a.append(float(l.strip()))
				record["A"] = a
			if 't' == line[0]:
				t = []
				for l in line[1:]:
					if l.strip() is not '':
						t.append(float(l.strip()))
				record["T"] = t
			if 'c' == line[0]:
				c = [] 
				for l in line[1:]:
					if l.strip() is not '':
						c.append(float(l.strip()))
				record["C"] = c
			if 'g' == line[0]:
				g = []
				for l in line[1:]:
					if l.strip() is not '':
						g.append(float(l.strip()))
				record["G"] = g
			if 'x' == line[0]:
				records.append(record)
				record = {}



	#now have all mutations as csv
	i = 1
	while i < len(records) + 1:
		fractions = (records[i-1])['fractions']
		segment = (records[i-1])['segments']
		#write segment
		segment_string = ''.join(str(s) for s in segment)
		o.write(('>' + strain + '_segment%s_\n%s\n')%(str(i), segment_string))
		#reverse complement
		reverse_complement = "".join(complement.get(b, b) for b in reversed(segment_string))
		o.write(('>' + strain + '_segment%s_reverse\n%s\n')%(str(i), reverse_complement))
		#get chunks to represent mutations
		for frac in fractions:
			frac_float = float(frac)
			if frac_float < 0.95:
				snp_location = int(fractions.index(frac))
				for base in bases:
					base_list = ((records[i-1])[base])
					if float(base_list[snp_location]) > 0:
						if base != ((records[i-1])['segments'])[snp_location]:
							sub_sequences = segment[(snp_location - 20):(snp_location + 20)]	
							if len(sub_sequences) > 10:
								sub_sequences[20] = base
								sub_sequence = ''.join(str(s) for s in sub_sequences)
								o.write(('>' + strain + '_segment%s_%s-%s_%s_%s->%s\n%s\n')%(str(i), str(snp_location - 20), str(snp_location + 20), str(snp_location + 1), str(segment[snp_location]), str(base), sub_sequence))
		i = i + 1





