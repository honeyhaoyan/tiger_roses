import numpy as np
import matplotlib.pyplot as plt
import pickle
import csv

data_file = '../data.csv'
tag_file = '../msn.csv'

tag = dict()
state = dict()
state['AZ'] = 0
state['CA'] = 1
state['NM'] = 2
state['TX'] = 3

start_year = 1960
# year start from 1960
def plot_tag_unit(X, e_type, s_type, unit, xlabel = 'Year', ylabel = None):
	data = np.zeros([4,50])
	for row in X:
		info = tag[row['MSN']]
		if info['Energy type'] == e_type and info['sector'] == s_type and info['Unit'] == unit:
			data[state[row['StateCode']]][int(row['Year']) - start_year] += float(row['Data'])
	print data
	l0, = plt.plot(range(1960,2010), data[0])
	l1, = plt.plot(range(1960,2010), data[1])
	l2, = plt.plot(range(1960,2010), data[2])
	l3, = plt.plot(range(1960,2010), data[3])
	plt.legend(['Arizona','California','New Mexico', 'Texas'])
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.show()


def plot_fossil_fuel(csv_reader):
	data = []
	for row in csv_reader:
		if tag[row['MSN']] == 'fossil fuel':
			nop
	
def main():
	global tag
	X = []
	with open(tag_file, 'rb') as f:
		csv_reader = csv.DictReader(f)
		for row in csv_reader:
			tag[row['MSN']] = row
	with open(data_file, 'rb') as f:
		csv_reader = csv.DictReader(f)
		print csv_reader
		for row in csv_reader:
			X.append(row)
#			X.append([row['MSN'], row['StateCode'], int(row['Year']), float(row['Data'])])
		plot_fossil_fuel(X)
#		plot_tag_unit(X, 'fossil fuel', 'total', 'Billion Btu', ylabel = 'Total Fossil fuel')
		plot_tag_unit(X, 'aviation gasoline', 'industrial', 'Billion Btu')

if __name__=='__main__':
	main()
