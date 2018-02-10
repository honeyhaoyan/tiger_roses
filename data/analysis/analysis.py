import numpy as np
import matplotlib.pyplot as plt
import pickle
import csv

data_file = '../data.csv'
tag_file = '../msn.csv'

X = []
prepared = False
tag = dict()
state = dict()
state['AZ'] = 0
state['CA'] = 1
state['NM'] = 2
state['TX'] = 3
start_year = 1960
# year start from 1960

def plot_tag_unit(X, e_type, s_type, unit, xlabel = 'Year', ylabel = None):
	prepare()
	data = np.zeros([4,50])
	for row in X:
		info = tag[row['MSN']]
		if info['Energy type'] == e_type and info['sector'] == s_type and info['Unit'] == unit:
			data[state[row['StateCode']]][int(row['Year']) - start_year] += float(row['Data'])
	print (data)
	l0, = plt.plot(range(1960,2010), data[0])
	l1, = plt.plot(range(1960,2010), data[1])
	l2, = plt.plot(range(1960,2010), data[2])
	l3, = plt.plot(range(1960,2010), data[3])
	plt.legend(['Arizona','California','New Mexico', 'Texas'])
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.show()

def plot_stacked_bar_graph(X, type_name, e_types, s_type = 'total', unit = 'Billion Btu', width = 0.35, xlabel = 'Year', ylabel = None, ylim='scalable'):
	'''
	X         : data array read from csv
	type_name : type name used to plot stacked graph
	e_types   : energy_types want to stack
	s_type    : sector type used
	unit      : unit used to determine which MSN
	width     : width of bar
	xlabel    : xlabel of graph
	ylabel    : ylabel of graph
	'''
	prepare()
	global tag
	global state
	fig = plt.figure()
	num_of_types = len(e_types)
	data = np.zeros([4, len(e_types), 50])
	min_v = 1e20
	max_v = -1e20
	for i in range(num_of_types):
		for row in X:
			info = tag[row['MSN']]
			if info['Energy type'] == e_types[i] and info['sector'] == s_type and info['Unit'] == unit:
				data[state[row['StateCode']]][i][int(row['Year']) - start_year] += float(row['Data'])
	if ylim == 'same':
		for i in range(4):
			for k in range(50):
				s = 0
				for j in range(num_of_types):
						s = s + data[i][j][k]
				min_v = min(min_v, s)
				max_v = max(max_v, s)
		
	print (data)
	ind = np.arange(1960, 2010, 1)
	legends = ['Arizona','California','New Mexico', 'Texas']
	for i in range(4):
		plt.subplot(2,2,i+1)
		plt.bar(ind, data[i][0], width)
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j], bottom=data[i][j-1])
		plt.legend(e_types)
		if ylim == 'same':
			plt.ylim((min_v, max_v))
#		fig.text(0.30,0.50,legends[i],ha='center')
		plt.title(legends[i], va='bottom')
	plt.show()

def plot_percentage_stacked_bar_chart(X, type_name, e_types, s_type = 'total', unit='Billion Btu', width = 0.35, xlabel='Year', ylabel=None):
	'''
	X         : data array read from csv
	type_name : type name used to plot stacked graph
	e_types   : energy_types want to stack
	s_type    : sector type used
	unit      : unit used to determine which MSN
	width     : width of bar
	xlabel    : xlabel of graph
	ylabel    : ylabel of graph
	'''
	prepare()
	print (e_types)
	global tag
	global state
	fig = plt.figure()
	num_of_types = len(e_types)
	data = np.zeros([4, len(e_types), 50])
	for i in range(num_of_types):
		for row in X:
			info = tag[row['MSN']]
			if info[type_name] == e_types[i] and info['sector'] == s_type and info['Unit'] == unit:
				data[state[row['StateCode']]][i][int(row['Year']) - start_year] += float(row['Data'])
	print (data)
	ind = np.arange(1960, 2010, 1)
	legends = ['Arizona','California','New Mexico', 'Texas']
	for i in range(4):
		sm = np.sum(data[i], axis=0)
		plt.subplot(2,2,i+1)
		plt.bar(ind, data[i][0]*100.0/sm, width)
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j]*100.0/sm, width,bottom=data[i][j-1]*100.0/sm)
		plt.legend(e_types)
#		fig.text(0.30,0.50,legends[i],ha='center')
		plt.title(legends[i], va='bottom')
	plt.show()


def prepare():
	global prepared
	if prepared == True:
		return
	else:
		prepared = True
	global tag
	global X
	with open(tag_file, 'r') as f:
		csv_reader = list(csv.DictReader(f))
		for row in csv_reader:
			# print(csv_reader)
			tag[row['MSN']] = row
	with open(data_file, 'r') as f:
		csv_reader = list(csv.DictReader(f))
		# print (csv_reader)
		for row in csv_reader:
			X.append(row)
def main():
	prepare()
#			X.append([row['MSN'], row['StateCode'], int(row['Year']), float(row['Data'])])
#		plot_tag_unit(X, 'fossil fuel', 'total', 'Billion Btu', ylabel = 'Total Fossil fuel')
#		plot_tag_unit(X, 'aviation gasoline', 'industrial', 'Billion Btu')
	types = ['unclean energy', 'clean energy']
#		plot_stacked_bar_graph(X, 'Energy type', types)
	plot_percentage_stacked_bar_chart(X, 'cleanliness', types)

if __name__=='__main__':
	main()
