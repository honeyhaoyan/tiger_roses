import numpy as np
import matplotlib.pyplot as plt
import pickle
import csv

data_file = '../data.csv'
tag_file = '../msn.csv'

fig_path = '../figure/'
X = []
prepared = False
tag = dict()
state = dict()
state['AZ'] = 0
state['CA'] = 1
state['NM'] = 2
state['TX'] = 3
start_year = start_year
end_year = 2010
# year start from start_year

def set_start_year(year):
	global start_year
	start_year = year
def set_end_year(year):
	global end_year
	end_year = year
def plot_tag_unit(e_type, s_type, unit, plot_start_year = start_year, figsize = (16,10), xlabel = 'Year', ylabel = None, title = ""):
	prepare()
	global X
	global tag
	global state
	fig = plt.figure(figsize=figsize)
	data = np.zeros([4,50])
	for row in X:
		info = tag[row['MSN']]
		if info['Energy type'] == e_type and info['sector'] == s_type and info['Unit'] == unit:
			data[state[row['StateCode']]][int(row['Year']) - start_year] += float(row['Data'])
#	print (data)
	ind = np.arange(plot_start_year,end_year)
	if plot_start_year > start_year:
		data = data[:,plot_start_year-start_year:50]
	l0, = plt.plot(ind, data[0])
	l1, = plt.plot(ind, data[1])
	l2, = plt.plot(ind, data[2])
	l3, = plt.plot(ind, data[3])
	plt.legend(['Arizona','California','New Mexico', 'Texas'])
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
#	plt.show()
	if title == "":
		title = ylabel
	plt.suptitle(title)
	fig.savefig(fig_path+title + "=" + e_type+'--line.png')

def get_matrix(
	change_type, c_types, 
	stable_type = ['sector', 'Unit'], s_type = ['TC','Billion Btu']):
	'''
	change_type : type name used to plot stacked graph
	c_types     : energy_types want to stack
	stable_type : type name which are same between msncodes
	s_type      : stable_type values
	'''
	prepare()
	global X
	global tag
	global state
	global start_year
	num_of_types = len(c_types)
	data = np.zeros([4, num_of_types, 50])
	for i in range(num_of_types):
		for row in X:
			info = tag[row['MSN']]
			flag = True
			for j in range(len(stable_type)):
				if info[stable_type[j]] != s_type[j]:
					flag = False
					break
			if info[change_type] == c_types[i] and flag == True:
				data[state[row['StateCode']]][i][int(row['Year']) - start_year] += float(row['Data'])
	return data

def single_state_stacked_bar_chart_by_matrix(
	data, legends, 
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	ind = np.arange(plot_start_year, end_year, 1)
	num_of_types = len(legends)
	last = np.zeros([4, num_of_types, end_year-plot_start_year])
	if plot_start_year > start_year:
		data = data[:,:,plot_start_year - start_year:50]
	for i in range(4):
		fig = plt.figure(figsize=figsize)
		plt.bar(ind, data[i][0], width)
		last[i][0] = data[i][0]
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j], width,bottom=last[i][j-1])
			last[i][j] = last[i][j-1]+data[i][j]
		plt.legend(legends)
		fig.savefig(fig_path+titles[i]+"-"+title+"-"+','.join(legends)+'-bar_chart.png')

def plot_stacked_bar_chart_by_matrix(
	data, legends, 
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	fig = plt.figure(figsize=figsize)
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	ind = np.arange(plot_start_year, end_year, 1)
	num_of_types = len(legends)
	last = np.zeros([4, num_of_types, end_year-plot_start_year])
	if plot_start_year > start_year:
		data = data[:,:,plot_start_year - start_year:50]
	for i in range(4):
		plt.subplot(2,2,i+1)
		plt.bar(ind, data[i][0], width)
		last[i][0] = data[i][0]
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j], width,bottom=last[i][j-1])
			last[i][j] = last[i][j-1]+data[i][j]
		plt.legend(legends)
		plt.title(titles[i], va='bottom')
#	plt.show()
	plt.suptitle(title+"="+','.join(legends))
	fig.savefig(fig_path+title+"="+','.join(legends)+'-bar_chart.png')

def plot_stacked_bar_chart(
	change_type, c_types, 
	stable_type = ['sector', 'Unit'], s_type = ['TC','Billion Btu'],
	figsize=(16,10), width = 0.5, xlabel='Year', ylabel=None, ylim='scalable', title = ""):
	'''
	change_type : type name used to plot stacked graph
	c_types     : energy_types want to stack
	stable_type : type name which are same between msncodes
	s_type      : stable_type values
	width       : width of bar
	xlabel      : xlabel of graph
	ylabel      : ylabel of graph
	'''
	prepare()
	global X
	global tag
	global state
	fig = plt.figure(figsize=figsize)
	num_of_types = len(c_types)
	data = np.zeros([4, num_of_types, 50])
	min_v = 1e20
	max_v = -1e20
	for i in range(num_of_types):
		for row in X:
			info = tag[row['MSN']]
			flag = True
			for j in range(len(stable_type)):
				if info[stable_type[j]] != s_type[j]:
					flag = False
					break
			if info[change_type] == c_types[i] and flag == True:
				data[state[row['StateCode']]][i][int(row['Year']) - start_year] += float(row['Data'])
	if ylim == 'same':
		for i in range(4):
			for k in range(50):
				s = 0
				for j in range(num_of_types):
						s = s + data[i][j][k]
				min_v = min(min_v, s)
				max_v = max(max_v, s)
	ind = np.arange(start_year, end_year, 1)
	titles = ['Arizona','California','New Mexico', 'Texas']
	legends = c_types
	last = np.zeros([4, num_of_types, 50])
	for i in range(4):
		plt.subplot(2,2,i+1)
		plt.bar(ind, data[i][0], width)
		last[i][0] = data[i][0]
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j], width,bottom=last[i][j-1])
			last[i][j] = last[i][j-1]+data[i][j]
		plt.legend(legends)
		if ylim == 'same':
			plt.ylim((min_v, max_v))
#		fig.text(0.30,0.50,legends[i],ha='center')
		plt.title(titles[i], va='bottom')
#	plt.show()
	plt.suptitle(title+"="+','.join(legends))
	fig.savefig(fig_path+title+"="+','.join(legends)+'-bar_chart.png')

def single_state_percentage_stacked_bar_chart_by_matrix(
	data, legends, 
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	ind = np.arange(plot_start_year, end_year, 1)
	num_of_types = len(legends)
	last = np.zeros([4, num_of_types, end_year - plot_start_year])
	if plot_start_year != start_year:
		data = data[:,:,plot_start_year - start_year:50]
	for i in range(4):
		fig=plt.figure(figsize=figsize)
		sm = np.sum(data[i], axis=0)
		plt.bar(ind, data[i][0]*100.0/sm, width)
		last[i][0] = data[i][0]*100.0/sm
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j]*100.0/sm, width,bottom=last[i][j-1])
			last[i][j] = last[i][j-1]+data[i][j]*100.0/sm
		plt.legend(legends)
		fig.savefig(fig_path+titles[i]+"-"+title+"-"+','.join(legends)+'-percentage.png')

def plot_percentage_stacked_bar_chart_by_matrix(
	data, legends, 
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	fig=plt.figure(figsize=figsize)
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	ind = np.arange(plot_start_year, end_year, 1)
	num_of_types = len(legends)
	last = np.zeros([4, num_of_types, end_year - plot_start_year])
	if plot_start_year != start_year:
		data = data[:,:,plot_start_year - start_year:50]
	for i in range(4):
		sm = np.sum(data[i], axis=0)
		plt.subplot(2,2,i+1)
		plt.bar(ind, data[i][0]*100.0/sm, width)
		last[i][0] = data[i][0]*100.0/sm
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j]*100.0/sm, width,bottom=last[i][j-1])
			last[i][j] = last[i][j-1]+data[i][j]*100.0/sm
		plt.legend(legends)
#		fig.text(0.30,0.50,legends[i],ha='center')
		plt.title(titles[i], va='bottom')
	plt.suptitle(title+"="+','.join(legends))
	fig.savefig(fig_path+title+"="+','.join(legends)+'-percentage.png')
#	plt.show()

def plot_percentage_stacked_bar_chart(
	change_type, c_types, 
	stable_type = ['sector', 'Unit'], s_type = ['TC','Billion Btu'],
	figsize = (16,10), width = 0.5, xlabel='Year', ylabel=None, title = ""):
	'''
	change_type : type name used to plot stacked graph
	c_types     : energy_types want to stack
	stable_type : type name which are same between msncodes
	s_type      : stable_type values
	width       : width of bar
	xlabel      : xlabel of graph
	ylabel      : ylabel of graph
	'''
	prepare()
	global X
	global tag
	global state
	fig = plt.figure(figsize=figsize)
	num_of_types = len(c_types)
	data = np.zeros([4, num_of_types, 50])
	for i in range(num_of_types):
		for row in X:
			info = tag[row['MSN']]
			flag = True
			for j in range(len(stable_type)):
				if info[stable_type[j]] != s_type[j]:
					flag = False
					break
			if info[change_type] == c_types[i] and flag == True:
				data[state[row['StateCode']]][i][int(row['Year']) - start_year] += float(row['Data'])
	ind = np.arange(start_year, end_year, 1)
	titles = ['Arizona','California','New Mexico', 'Texas']
	legends = c_types
	last = np.zeros([4, num_of_types, 50])
	for i in range(4):
		sm = np.sum(data[i], axis=0)
		plt.subplot(2,2,i+1)
		plt.bar(ind, data[i][0]*100.0/sm, width)
		last[i][0] = data[i][0]*100.0/sm
		for j in range(1, num_of_types):
			plt.bar(ind, data[i][j]*100.0/sm, width,bottom=last[i][j-1])
			last[i][j] = last[i][j-1]+data[i][j]*100.0/sm
		plt.legend(legends)
#		fig.text(0.30,0.50,legends[i],ha='center')
		plt.title(titles[i], va='bottom')
	plt.suptitle(title+"="+','.join(legends))
	fig.savefig(fig_path+title+"="+','.join(legends)+'-percentage.png')
#	plt.show()

def plot_state_percentage_stacked_bar_chart(
	stable_type, s_type,
	figsize = (16,10), width = 0.5, xlabel = 'Year', ylabel = None, title = ""):
	prepare()
	global X
	global tag
	global state
	fig = plt.figure(figsize=figsize)
	data = np.zeros([4,50])
	for row in X:
		info = tag[row['MSN']]
		flag = True
		for j in range(len(stable_type)):
			if info[stable_type[j]] != s_type[j]:
				flag = False
				break
		if flag == True:
			data[state[row['StateCode']]][int(row['Year'])-start_year] += float(row['Data'])
	last = np.zeros([4,50])
	ind  = np.arange(start_year,end_year)
	sm = np.sum(data, axis = 0)
	plt.bar(ind, data[0]*100.0/sm, width)
	last[0] = data[0]*100.0/sm
	for j in range(1,4):
		plt.bar(ind,data[j]*100.0/sm,width,bottom=last[j-1])
		last[j] = last[j-1]+data[j]*100.0/sm
	legends = ['Arizona','California','New Mexico', 'Texas']
	plt.legend(legends)
	plt.title(title)
	fig.savefig(fig_path+title+','.join(s_type)+' - state_percentage.png')
def prepare():
	global prepared
	if prepared == True:
		return
	else:
		prepared = True
	global tag
	global X
	with open(tag_file, 'r') as f:
		csv_reader = csv.DictReader(f)
		for row in csv_reader:
			tag[row['MSN']] = row
	with open(data_file, 'r') as f:
		csv_reader = csv.DictReader(f)
		for row in csv_reader:
			X.append(row)
'''
def main():
	prepare()
#			X.append([row['MSN'], row['StateCode'], int(row['Year']), float(row['Data'])])
#		plot_tag_unit(X, 'fossil fuel', 'total', 'Billion Btu', ylabel = 'Total Fossil fuel')
#		plot_tag_unit(X, 'aviation gasoline', 'industrial', 'Billion Btu')
	types = ['unclean energy', 'clean energy']
#	plot_percentage_stacked_bar_chart(
#		'sector',
#		['industrial', 'residential', 'transportation'],
#		['Energy type'],
#		['coal']
#		
#		)
#	print get_matrix('cleanliness', types)
	plot_stacked_bar_chart_by_matrix(data=get_matrix('cleanliness', types), legends=types)
	plot_stacked_bar_chart('cleanliness', types)
#	plot_percentage_stacked_bar_chart('cleanliness', types)
'''

if __name__=='__main__':
	main()
