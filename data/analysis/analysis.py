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
start_year = 1960
end_year = 2010
# year start from start_year

def set_start_year(year):
	global start_year
	start_year = year
def set_end_year(year):
	global end_year
	end_year = year

def autolabel(ax, rects, m):
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x() + rect.get_width()/2., 1.025*height,
				'%.2f'% float(height*m),
				ha='center', va='bottom')
def plot_AHP_chart():
	figsize = (16,10)
	fig,ax = plt.subplots(figsize = figsize)
	c = list([None for i in range(3)])
	c[0] = \
	get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +\
	get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B'])
	c[0] = c[0][:,:,49]
	sm = np.sum(c[0], axis = 1)
	c[0] = c[0][:,2]*100/sm
	c[1] = get_matrix('Energy type', ['TE'], stable_type=['sector','Unit'], s_type=['TP','Million Btu'])
	c[2] = get_matrix('Energy type', ['TE'], stable_type=['sector','Unit'], s_type=['TG','Thousand Btu per chained (2000) dollar'])
	c[1] = c[1][:,:,49]
	c[2] = c[2][:,:,49]
	c[1] = c[1][:,0]
	c[2] = c[2][:,0]
	m = list([np.sum(c[i]) for i in range(3)])
	for i in range(3):
		c[i] = c[i] / m[i]
	ind = np.arange(0.0,4.0,1.0)
	legends = ['Renewable energy percentage', 'Total energy per capita', 'Total energy per GDP']
	width = 0.2
	for i in range(0,3):
		print c[i]
		t = plt.bar(ind, c[i], width = width)
		ind += width
		autolabel(ax, t, m[i])
	ax.set_xticks(ind - 2.0*width)
	ax.set_yticks([])
	ax.set_xticklabels(['Arizona', 'California', 'New Mexico', 'Texas'])
	ax.legend(legends)
	ax.spines['top'].set_visible(False)  
	ax.spines['right'].set_visible(False)  
	ax.spines['left'].set_visible(False)  
	fig.savefig(fig_path+'AHP.png')

def plot_single_year_bar_chart_by_matrix(
	data, legends, plot_year,
	figsize=(16,10), width=0.75, xlabel = 'State', ylabel = None, plot_start_year = start_year, title = ""):
	ind = ['Arizona', 'California', 'New Mexico', 'Texas']
	num_of_types = len(legends)
	last = np.zeros([4, num_of_types])

	fig = plt.figure(figsize = figsize)
	plt.bar(ind, data[:,0,plot_year-start_year])
	last[:,0] = data[:,0,plot_year-start_year]
	for i in range(1, num_of_types):
		plt.bar(ind, data[:,i,plot_year-start_year], bottom=last[:,i-1])
		last[:,i] = last[:,i-1]+data[:,i,plot_year-start_year]
	plt.legend(legends)
	fig.savefig(fig_path + ','.join(legends) + str(plot_year) + 'bar_chart.png')

def plot_single_year_percentage_bar_chart_by_matrix(
	data, legends, plot_year,
	figsize=(16,10), width=0.75, xlabel = 'State', ylabel = None, plot_start_year = start_year, title = ""):
	ind = ['Arizona', 'California', 'New Mexico', 'Texas']
	num_of_types = len(legends)
	last = np.zeros([4, num_of_types])

	fig = plt.figure(figsize = figsize)
	sm = np.sum(data[:,:,plot_year-start_year], axis = 1)
	plt.bar(ind, data[:,0,plot_year-start_year]*100.0/sm)
	last[:,0] = data[:,0,plot_year-start_year]*100.0/sm
	for i in range(1, num_of_types):
		plt.bar(ind, data[:,i,plot_year-start_year]*100.0/sm, bottom=last[:,i-1])
		last[:,i] = last[:,i-1]+data[:,i,plot_year-start_year]*100.0/sm
	plt.legend(legends)
	fig.savefig(fig_path + ','.join(legends) + str(plot_year) + 'percentage.png')

def plot_tag_unit(
	e_type, s_type, unit,
	plot_start_year = start_year, figsize = (16,10), xlabel = 'Year', ylabel = None, title = ""):
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
	_ind = None,
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	if np.array(_ind == None).all():
		ind = np.arange(plot_start_year, end_year, 1)
	else:
		ind = _ind
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
	_ind = None,
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	fig = plt.figure(figsize=figsize)
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	num_of_types = len(legends)
	if np.array(_ind == None).all():
		ind = np.arange(plot_start_year, end_year, 1)
		last = np.zeros([4, num_of_types, end_year-plot_start_year])
		if plot_start_year > start_year:
			data = data[:,:,plot_start_year - start_year:50]
	else:
		ind = _ind
		last = np.zeros([4, num_of_types, len(_ind)])
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
	fig.savefig(fig_path+title+"="+','.join(legends)+'-bar_chart.png')

def single_state_percentage_stacked_bar_chart_by_matrix(
	data, legends, 
	_ind = None,
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	if np.array(_ind == None).all():
		ind = np.arange(plot_start_year, end_year, 1)
	else:
		ind = _ind
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
	_ind = None,
	figsize=(16,10), width=0.75, xlabel = 'Year', ylabel = None, plot_start_year = start_year, title = ""):
	fig=plt.figure(figsize=figsize)
	titles = ['Arizona', 'California', 'New Mexico', 'Texas']
	if np.array(_ind == None).all():
		ind = np.arange(plot_start_year, end_year, 1)
	else:
		ind = _ind
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
