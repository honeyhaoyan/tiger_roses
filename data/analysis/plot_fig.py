from analysis import *

replot_plotted = False

# plotted
if replot_plotted == True:
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['GD'],
		stable_type=['unit2'], s_type = ['X']),
		['GDP--2005'])
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['GD'],
		stable_type=['unit2'], s_type = ['V']),
		['GDP'])
	plot_tag_unit(
		'TP', 'T', 'Thousand', ylabel = 'Resident population')
	plot_tag_unit(
		'TE', 'T', 'Million Btu', ylabel = 'Total energy per capita')
	plot_percentage_stacked_bar_chart(
		'cleanliness',
		['clean energy', 'unclean energy total']
		)

	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', 'TE']) - 
		get_matrix('Energy type', ['ES', 'TN']) + 
		get_matrix('Energy type', ['ABC','ES']),
		['primary energy', 'secondary energy'])

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', 'TE']) - 
		get_matrix('Energy type', ['ES', 'TN']) + 
		get_matrix('Energy type', ['ABC','ES']),
		['primary energy', 'secondary energy'])

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', 'TE']) - 
		get_matrix('Energy type', ['ABC','TN']),
		['primary energy + electricity', 'other'])

'''
plot_tag_unit(
	'total energy', 'T', 'Million Btu')
'''


'''
plot_percentage_stacked_bar_chart(
	'sector',
	['S','T'],
	['Unit', 'Energy type'],
	['Billion Btu', 'TN']
	)

plot_percentage_stacked_bar_chart(
	'cleanliness',
	['clean energy', 'unclean energy total'],
	['Unit', 'sector'],
	['Billion Btu', 'T'],
	)

plot_stacked_bar_chart(
	'cleanliness',
	['clean energy', 'unclean energy total'],
	['Unit', 'sector'],
	['Billion Btu', 'T'],
	)
'''

'''
plot_percentage_stacked_bar_chart(
	'sector',
	['commercial', 'transportation', 'residential', 'industrial'],
	['Energy type', 'Unit'],
	['wood', 'Billion Btu']
	
	)

plot_stacked_bar_chart(
	'sector',
	['commercial', 'transportation', 'residential', 'industrial'],
	['Energy type', 'Unit'],
	['wood', 'Billion Btu'],
	ylim='same'
	)
'''
