"""
parse PASCAL VOC xml annotations
"""

import os
import sys

def pascal_voc_clean_xml(ANN, pick, exclusive = False):
	print('Parsing for {} {}'.format(
			pick, 'exclusively' * int(exclusive)))
	def pp(l): # pretty printing 
		for i in l: print('{}: {}'.format(i,l[i]))

	def parse(line): # exclude the xml tag
		x = line.split('>')[1].split('<')[0]
		try: r = int(x)
		except: r = x
		return r

	def _int(literal): # for literals supposed to be int 
		return int(float(literal))

	dumps = list()
	cur_dir = os.getcwd()
	os.chdir(ANN)
	annotations = os.listdir('.')
	annotations = [file for file in annotations if '.xml' in file]
	print(len(annotations),os.getcwd())
	#pp(pick)
	size = len(os.listdir('.'))

	for i, file in enumerate(annotations):

		# progress bar		
		sys.stdout.write('\r')
		percentage = 1. * (i+1) / size
		progress = int(percentage * 20)
		bar_arg = [progress*'=', ' '*(19-progress), percentage*100]
		bar_arg += [file]
		sys.stdout.write('[{}>{}]{:.0f}%  {}'.format(*bar_arg))
		sys.stdout.flush()
		
		# actual parsing 
		with open(file, 'r') as f:
			lines = f.readlines()
		fileinfo=lines[0].split()
		h =int(fileinfo[1]);w=int(fileinfo[2])
		all = current = list()
		jpg = fileinfo[0]
		#obj = False
		#flag = False
		for i in range(1,len(lines)):
			line = lines[i].split()
			#print(line)
			current = [line[0],_int(line[1]),_int(line[2]),_int(line[3]),_int(line[4])]
		if current != list() and current[0] in pick:
			all += [current]

		add = [[jpg, [w, h, all]]]
		dumps += add

	# gather all stats
	stat = dict()
	for dump in dumps:
		all = dump[1][2]
		for current in all:
			if current[0] in pick:
				if current[0] in stat:
					stat[current[0]]+=1
				else:
					stat[current[0]] =1

	print() 
	print('Statistics:')
	pp(stat)
	print('Dataset size: {}'.format(len(dumps)))

	os.chdir(cur_dir)
	return dumps
