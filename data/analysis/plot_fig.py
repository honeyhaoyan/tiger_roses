from analysis import *
from grey_prediction import *

# plot_stacked_bar_chart_by_matrix(
# 	prediction(get_matrix('Energy type', ['EM','GE','HY','SO','WY','BM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
# 	['Fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'biomass'], title="consumption_prediction")

# plot_percentage_stacked_bar_chart_by_matrix(
# 	prediction(get_matrix('Energy type', ['EM','GE','HY','SO','WY','BM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
# 	['Fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'biomass'], title="consumption_prediction")

#plot_stacked_bar_chart_by_matrix(
#	get_matrix('Energy type', ['CL', 'NN', 'PM'],
#		stable_type = ['sector', 'unit2'], s_type=['TC', 'B'],
#		title = "")

plot_stacked_bar_chart_by_matrix(
	prediction(get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
	["Coal", "Natural gas", "Petroleum products"], title="consumption_prediction")

plot_percentage_stacked_bar_chart_by_matrix(
	prediction(get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
	["Coal", "Natural gas", "Petroleum products"], title="consumption_prediction")

replot_plotted = False
# plotted
if replot_plotted == True:


	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B']),
		["Coal", "Natural gas", "Petroleum products"], title="consumption")
	plot_tag_unit('NU','ET','Billion Btu', ylabel="nuclear power")

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B']),
		["Fossil fuel", "nuclear power", "renewable energy"], title="consumption")
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B']),
		["Fossil fuel", "nuclear power", "renewable energy"], title="consumption")
	plot_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
		['Transportation','Commercial','Industrial','Residential'], title = "consumption")
	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
		['Transportation','Commercial','Industrial','Residential'], title = "consumption")

	plot_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
		['Transportation','Commercial','Industrial','Residential'], title = "expenditure")

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
		['Transportation','Commercial','Industrial','Residential'], title = "expenditure")


	'''
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', '..'], stable_type=['sector','unit2'], s_type=['SC','B']) +
		get_matrix('Energy type', ['..', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['..', 'TN'], stable_type=['sector','unit2'], s_type=['SC','B']),
		['primary energy', 'secondary energy'], title = "expenditure", plot_start_year = 1970)

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', '..'], stable_type=['sector','unit2'], s_type=['SC','B']) +
		get_matrix('Energy type', ['..', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['..', 'TN'], stable_type=['sector','unit2'], s_type=['SC','B']),
		['primary energy', 'secondary energy'], title = "expenditure", plot_start_year = 1970)

	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', '..'], stable_type=['sector','unit2'], s_type=['SC','B']) +
		get_matrix('Energy type', ['..', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['..', 'TN'], stable_type=['sector','unit2'], s_type=['SC','B']),
		['primary energy', 'secondary energy'], title = "consumption", plot_start_year = 1970)

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['TN', '..'], stable_type=['sector','unit2'], s_type=['SC','B']) +
		get_matrix('Energy type', ['..', 'TE'], stable_type=['sector','unit2'], s_type=['TC','B']) -
		get_matrix('Energy type', ['..', 'TN'], stable_type=['sector','unit2'], s_type=['SC','B']),
		['primary energy', 'secondary energy'], title = "consumption", plot_start_year = 1970)

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC','TX'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'AC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'CC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'IC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
		['Transportation','Commercial','Industrial','Residential','Other'], title = "consumption")


	plot_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC','TX'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'AC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'CC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'IC'], stable_type=['Energy type','unit2'], s_type=['TE','B']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
		['Transportation','Commercial','Industrial','Residential','Other'], title = "consumption")

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC','TX'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'AC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'CC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'IC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
		['Transportation','Commercial','Industrial','Residential','Other'], title = "expenditure")


	plot_stacked_bar_chart_by_matrix(
		get_matrix('sector',['AC','CC','IC','RC','TX'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'AC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'CC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'IC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) -
		get_matrix('sector',[',' ,',' ,',' ,',' ,'RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
		['Transportation','Commercial','Industrial','Residential','Other'], title = "expenditure")

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

	'''
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
