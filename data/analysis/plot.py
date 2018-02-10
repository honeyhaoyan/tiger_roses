from analysis import *

plot_percentage_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC','EI','TC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','AC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','CC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','IC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','EI'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
	['Transportation','Commercial','Industrial','Residential','Electric power','Other'], title = "consumption")


plot_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC','EI','TC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','AC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','CC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','IC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
	get_matrix('sector',[',',',',',',',',',','EI'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
	['Transportation','Commercial','Industrial','Residential','Electric power','Other'], title = "consumption")

plot_percentage_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC','EI','TC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','AC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','CC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','IC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','EI'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
	['Transportation','Commercial','Industrial','Residential','Electric power','Other'], title = "expenditure")


plot_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC','EI','TC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','AC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','CC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','IC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
	get_matrix('sector',[',',',',',',',',',','EI'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
	['Transportation','Commercial','Industrial','Residential','Electric power','Other'], title = "expenditure")

replot_plotted = False
# plotted
if replot_plotted == True:
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['RE', 'TE']) - 
		get_matrix('Energy type', ['ABC','RE']),
		['renewable energy', 'other'])

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['RE', 'TE']) - 
		get_matrix('Energy type', ['ABC','RE']),
		['renewable energy', 'other'])

	plot_percentage_stacked_bar_chart(
		'cleanliness',
		['clean energy', 'unclean energy']
		)
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['GD'],
		stable_type=['unit2'], s_type = ['X']),
		['GDP--2005'])
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['GD'],
		stable_type=['unit2'], s_type = ['V']),
		['GDP'])
	plot_tag_unit(
		'TP', 'O', 'Thousand', ylabel = 'Resident population')
	plot_tag_unit(
		'TE', 'TC', 'Million Btu', ylabel = 'Total energy per capita')


	plot_tag_unit('TE','TC','Billion Btu', title='Total energy consumption.') # start from 1970
	plot_tag_unit('TE','TC','Million dollars', title='Total energy expenditures.') # start from 1970
	plot_tag_unit('TE','TC', 'Thousand Btu per chained (2000) dollar',
		title = 'Total energy consumed per dollar of real gross domestic product.') # start from 1977


	plot_percentage_stacked_bar_chart(
		'sector',
		['AC','CC', 'IC', 'RC', 'EI'],
		['Unit', 'Energy type'],
		['Billion Btu', 'TE']
		)

	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['ES', 'TN'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['ABC','ES'], stable_type=['sector','unit2'], s_type=['TC','B']),
		['primary energy', 'secondary energy'], title = "expenditure")

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['ES', 'TN'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['ABC','ES'], stable_type=['sector','unit2'], s_type=['TC','B']),
		['primary energy', 'secondary energy'], title = "expenditure")

	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['ES', 'TN'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['ABC','ES'], stable_type=['sector','unit2'], s_type=['TC','B']),
		['primary energy', 'secondary energy'], title = "consumption")

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['ES', 'TN'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['ABC','ES'], stable_type=['sector','unit2'], s_type=['TC','B']),
		['primary energy', 'secondary energy'], title = "consumption")
'''
plot_tag_unit(
	'total energy', 'TC', 'Million Btu')
'''


'''
plot_percentage_stacked_bar_chart(
	'sector',
	['S','TC'],
	['Unit', 'Energy type'],
	['Billion Btu', 'TN']
	)

plot_percentage_stacked_bar_chart(
	'cleanliness',
	['clean energy', 'unclean energy total'],
	['Unit', 'sector'],
	['Billion Btu', 'TC'],
	)

plot_stacked_bar_chart(
	'cleanliness',
	['clean energy', 'unclean energy total'],
	['Unit', 'sector'],
	['Billion Btu', 'TC'],
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