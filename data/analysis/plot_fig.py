from analysis import *

plot_stacked_bar_chart_by_matrix(
	get_matrix('Energy type', ['EM','GE','HY','SO','WY','WW','EM'],
		stable_type=['sector','unit2'], s_type=['TC','B']) +
	get_matrix('Energy type', ['EM','GE','HY','SO','WY','WW','EM'],
		stable_type=['sector','unit2'], s_type=['LC','B']),
	['fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'wood and waste','energy losses and co-products...'], title="consumption")

plot_percentage_stacked_bar_chart_by_matrix(
	get_matrix('Energy type', ['EM','GE','HY','SO','WY','WW','EM'],
		stable_type=['sector','unit2'], s_type=['TC','B']) +
	get_matrix('Energy type', ['EM','GE','HY','SO','WY','WW','EM'],
		stable_type=['sector','unit2'], s_type=['LC','B']),
	['fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'wood and waste','energy losses and co-products...'], title="consumption")


#plot_tag_unit('
#plot_stacked_bar_chart_by_matrix(
#	get_matrix('Energy type', ['CL', 'NN', 'PM'],
#		stable_type = ['sector', 'unit2'], s_type=['TC', 'B'],
#		title = "")
replot_plotted = False
# plotted
if replot_plotted == True:

	plot_bar_chart(
		get_matrix('sector',['TC'],stable_type=['Energy type','unit2'], s_type=['TE','D']),
		['Total energy average price'],
		title = "total energy average price")
	plot_bar_chart(
		get_matrix('sector',['TC','PR'],stable_type=['Energy type','unit2'], s_type=['TE','B']),
		['Total consumption', 'Total production'],
		title = "consumption and production")
	plot_AHP_chart()
	plot_single_year_percentage_bar_chart_by_matrix(
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B']),
		plot_year = 2009, legends = ["Fossil fuel", "nuclear power", "renewable energy"])
	plot_single_year_bar_chart_by_matrix(
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B']),
		plot_year = 2009, legends = ["Fossil fuel", "nuclear power", "renewable energy"])
	plot_state_percentage_stacked_bar_chart(
		['Energy type','sector','unit2'],
		['TE','TC','B'], title = "Total Energy")

	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['EM','GE','HY','SO','WY','BM'], stable_type=['sector','unit2'], s_type=['TC','B']),
		['Fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'biomass'], title="consumption")

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['EM','GE','HY','SO','WY','BM'], stable_type=['sector','unit2'], s_type=['TC','B']),
		['Fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'biomass'], title="consumption")

	plot_tag_unit('NU','ET','Billion Btu', ylabel="nuclear power")

	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B']),
		["Coal", "Natural gas", "Petroleum products"], title="consumption")

	plot_percentage_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B']),
		["Coal", "Natural gas", "Petroleum products"], title="consumption")

	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['GD'],
		stable_type=['unit2'], s_type = ['X']),
		legends=['GDP--2005'])
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['GD'],
		stable_type=['unit2'], s_type = ['V']),
		legends=['GDP'])

	plot_tag_unit('TE','TC','Billion Btu', ylabel='Total energy consumption.') # start from 1970
	plot_tag_unit('TE','TC','Million dollars', ylabel='Total energy expenditures.') # start from 1970
	plot_tag_unit('TE','TG', 'Thousand Btu per chained (2000) dollar',
		ylabel = 'Total energy consumed per dollar of real gross domestic product.') # start from 1977
	plot_tag_unit('TP','OP','Thousand', ylabel = "Resident population")
	plot_tag_unit('TE','TP','Million Btu', ylabel = "Total energy per capita")

	plot_tag_unit('TE','TG','Thousand Btu per chained (2000) dollar', ylabel="Total energy per GDP",plot_start_year = 1977)
	plot_stacked_bar_chart_by_matrix(
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +
		get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B']),
		["Fossil fuel", "nuclear power", "renewable energy"], title="consumption")
	plot_percentage_stacked_bar_chart_by_matrix(
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

	plot_tag_unit('TE','TC','Billion Btu', title='Total Energy')


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
	plot_tag_unit(
		'TP', 'O', 'Thousand', ylabel = 'Resident population')
	plot_tag_unit(
		'TE', 'TC', 'Million Btu', ylabel = 'Total energy per capita')




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
